from database.conexion import mysql
from datetime import datetime, date


# ==========================================
# CONVERTIR FECHA
# ==========================================

def convertir_fecha(fecha):

    if fecha is None:
        return datetime.min

    # Si ya es datetime
    if isinstance(fecha, datetime):
        return fecha

    # Si es date
    if isinstance(fecha, date):
        return datetime.combine(fecha, datetime.min.time())

    # Si viene como texto
    if isinstance(fecha, str):

        formatos = [
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d",
            "%d/%m/%Y %H:%M:%S",
            "%d/%m/%Y"
        ]

        for formato in formatos:

            try:
                return datetime.strptime(fecha, formato)

            except ValueError:
                continue

    return datetime.min


# ==========================================
# ESTADÍSTICAS GENERALES
# ==========================================

def obtener_estadisticas():

    conexion = mysql.connect()
    cursor = conexion.cursor()

    estadisticas = {}

    # --------------------------------------
    # LIBROS
    # --------------------------------------

    cursor.execute("""
        SELECT COUNT(*)
        FROM libros
        WHERE Estado = 1
    """)

    estadisticas['libros'] = cursor.fetchone()[0]


    # --------------------------------------
    # AUTORES
    # --------------------------------------

    cursor.execute("""
        SELECT COUNT(*)
        FROM autores
    """)

    estadisticas['autores'] = cursor.fetchone()[0]


    # --------------------------------------
    # LECTORES ACTIVOS
    # --------------------------------------

    cursor.execute("""
        SELECT COUNT(*)
        FROM lectores
        WHERE Estado = 'Activo'
    """)

    estadisticas['lectores'] = cursor.fetchone()[0]


    # --------------------------------------
    # PRÉSTAMOS ACTIVOS
    # --------------------------------------

    cursor.execute("""
        SELECT COUNT(*)
        FROM prestamos
        WHERE Estado = 'Prestado'
    """)

    estadisticas['prestamos'] = cursor.fetchone()[0]


    # --------------------------------------
    # PRÉSTAMOS VENCIDOS
    # --------------------------------------

    cursor.execute("""
        SELECT COUNT(*)
        FROM prestamos
        WHERE Estado = 'Vencido'
    """)

    estadisticas['vencidos'] = cursor.fetchone()[0]


    # --------------------------------------
    # PRÉSTAMOS DEVUELTOS
    # --------------------------------------

    cursor.execute("""
        SELECT COUNT(*)
        FROM prestamos
        WHERE Estado = 'Devuelto'
    """)

    estadisticas['devueltos'] = cursor.fetchone()[0]


    # --------------------------------------
    # USUARIOS ACTIVOS
    # --------------------------------------

    # IMPORTANTE:
    # Tu tabla se llama "usuario", no "usuarios".

    cursor.execute("""
        SELECT COUNT(*)
        FROM usuario
        WHERE Estado = 1
    """)

    estadisticas['usuarios'] = cursor.fetchone()[0]


    cursor.close()
    conexion.close()

    return estadisticas


# ==========================================
# ACTIVIDAD RECIENTE
# ==========================================

def obtener_actividad_reciente():

    conexion = mysql.connect()
    cursor = conexion.cursor()

    actividades = []


    # --------------------------------------
    # ÚLTIMOS LIBROS
    # --------------------------------------

    cursor.execute("""
        SELECT
            'Libro agregado' AS tipo,
            Nombre AS nombre,
            FechaRegistro AS fecha
        FROM libros
        ORDER BY FechaRegistro DESC
        LIMIT 3
    """)

    libros = cursor.fetchall()

    for libro in libros:

        actividades.append({
            'tipo': libro[0],
            'nombre': libro[1],
            'fecha': convertir_fecha(libro[2])
        })


    # --------------------------------------
    # ÚLTIMOS LECTORES
    # --------------------------------------

    cursor.execute("""
        SELECT
            'Nuevo lector registrado' AS tipo,
            NombreCompleto AS nombre,
            FechaRegistro AS fecha
        FROM lectores
        ORDER BY FechaRegistro DESC
        LIMIT 3
    """)

    lectores = cursor.fetchall()

    for lector in lectores:

        actividades.append({
            'tipo': lector[0],
            'nombre': lector[1],
            'fecha': convertir_fecha(lector[2])
        })


    # --------------------------------------
    # ÚLTIMOS USUARIOS
    # --------------------------------------

    cursor.execute("""
        SELECT
            'Nuevo usuario registrado' AS tipo,
            NombreCompleto AS nombre,
            FechaRegistro AS fecha
        FROM usuario
        ORDER BY FechaRegistro DESC
        LIMIT 3
    """)

    usuarios = cursor.fetchall()

    for usuario in usuarios:

        actividades.append({
            'tipo': usuario[0],
            'nombre': usuario[1],
            'fecha': convertir_fecha(usuario[2])
        })


    # --------------------------------------
    # ORDENAR ACTIVIDADES
    # --------------------------------------

    actividades.sort(
        key=lambda x: x['fecha'],
        reverse=True
    )


    cursor.close()
    conexion.close()

    return actividades[:5]


# ==========================================
# LIBROS MÁS SOLICITADOS
# ==========================================

def obtener_libros_mas_solicitados():

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            libros.Nombre,
            COUNT(prestamos.IdLibro) AS cantidad
        FROM prestamos

        INNER JOIN libros
            ON prestamos.IdLibro = libros.Id

        GROUP BY
            libros.Id,
            libros.Nombre

        ORDER BY cantidad DESC

        LIMIT 5
    """)

    libros = cursor.fetchall()

    cursor.close()
    conexion.close()
 
    return libros