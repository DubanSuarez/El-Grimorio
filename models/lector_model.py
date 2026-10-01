from database.conexion import mysql


# =========================
# OBTENER TODOS LOS LECTORES
# =========================

def obtener_lectores():

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            Id,
            TipoDocumento,
            NumeroDocumento,
            NombreCompleto,
            Telefono,
            Correo,
            Direccion,
            TipoLector,
            Estado,
            FechaRegistro
        FROM lectores
        ORDER BY Id DESC
    """)

    lectores = cursor.fetchall()

    cursor.close()
    conexion.close()

    return lectores


# =========================
# OBTENER UN LECTOR
# =========================

def obtener_lector(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            Id,
            TipoDocumento,
            NumeroDocumento,
            NombreCompleto,
            Telefono,
            Correo,
            Direccion,
            TipoLector,
            Estado,
            FechaRegistro
        FROM lectores
        WHERE Id = %s
    """, (id,))

    lector = cursor.fetchone()

    cursor.close()
    conexion.close()

    return lector


# =========================
# INSERTAR LECTOR
# =========================

def insertar_lector(tipo_documento, numero_documento, nombre_completo,
                    telefono, correo, direccion, tipo_lector,
                    estado, fecha_registro):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO lectores (
            TipoDocumento,
            NumeroDocumento,
            NombreCompleto,
            Telefono,
            Correo,
            Direccion,
            TipoLector,
            Estado,
            FechaRegistro
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        tipo_documento,
        numero_documento,
        nombre_completo,
        telefono,
        correo,
        direccion,
        tipo_lector,
        estado,
        fecha_registro
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


# =========================
# ACTUALIZAR LECTOR
# =========================

def actualizar_lector(id, tipo_documento, numero_documento,
                      nombre_completo, telefono, correo,
                      direccion, tipo_lector, estado):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE lectores
        SET
            TipoDocumento = %s,
            NumeroDocumento = %s,
            NombreCompleto = %s,
            Telefono = %s,
            Correo = %s,
            Direccion = %s,
            TipoLector = %s,
            Estado = %s
        WHERE Id = %s
    """, (
        tipo_documento,
        numero_documento,
        nombre_completo,
        telefono,
        correo,
        direccion,
        tipo_lector,
        estado,
        id
    ))

    conexion.commit()

    cursor.close()
    conexion.close()



# =========================
# DESACTIVAR LECTOR
# =========================

def desactivar_lector(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE lectores
        SET Estado = 'Inactivo'
        WHERE Id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()


# =========================
# REACTIVAR LECTOR
# =========================

def reactivar_lector(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE lectores
        SET Estado = 'Activo'
        WHERE Id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()