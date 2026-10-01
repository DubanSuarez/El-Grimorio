from database.conexion import mysql


# =========================
# OBTENER PRÉSTAMOS
# =========================

def obtener_prestamos():

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            prestamos.Id,
            libros.Nombre AS Libro,
            lectores.NombreCompleto AS Lector,
            prestamos.IdUsuario,
            prestamos.FechaPrestamo,
            prestamos.FechaDevolucionProgramada,
            prestamos.FechaDevolucionReal,
            prestamos.Estado,
            prestamos.Observaciones,
            prestamos.FechaRegistro
        FROM prestamos
        INNER JOIN libros
            ON prestamos.IdLibro = libros.Id
        INNER JOIN lectores
            ON prestamos.IdLector = lectores.Id
        ORDER BY prestamos.Id DESC
    """)

    prestamos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return prestamos


# =========================
# OBTENER UN PRÉSTAMO
# =========================

def obtener_prestamo(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            prestamos.Id,
            libros.Nombre AS Libro,
            lectores.NombreCompleto AS Lector,
            prestamos.IdUsuario,
            usuario.NombreCompleto AS UsuarioResponsable,
            prestamos.FechaPrestamo,
            prestamos.FechaDevolucionProgramada,
            prestamos.FechaDevolucionReal,
            prestamos.Estado,
            prestamos.Observaciones,
            prestamos.FechaRegistro

        FROM prestamos

        INNER JOIN libros
            ON prestamos.IdLibro = libros.Id

        INNER JOIN lectores
            ON prestamos.IdLector = lectores.Id

        INNER JOIN usuario
            ON prestamos.IdUsuario = usuario.Id

        WHERE prestamos.Id = %s

    """, (id,))

    prestamo = cursor.fetchone()

    cursor.close()
    conexion.close()

    return prestamo


# =========================
# INSERTAR PRÉSTAMO
# =========================

def insertar_prestamo(
    id_libro,
    id_lector,
    id_usuario,
    fecha_prestamo,
    fecha_devolucion_programada,
    estado,
    observaciones
):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO prestamos (
            IdLibro,
            IdLector,
            IdUsuario,
            FechaPrestamo,
            FechaDevolucionProgramada,
            Estado,
            Observaciones
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        id_libro,
        id_lector,
        id_usuario,
        fecha_prestamo,
        fecha_devolucion_programada,
        estado,
        observaciones
    ))

    cursor.execute("""
        UPDATE libros
        SET Disponibles = Disponibles - 1
        WHERE Id = %s
        AND Disponibles > 0
    """, (
        id_libro,
    ))

    conexion.commit()

    cursor.close()
    conexion.close()




# =========================
# ACTUALIZAR PRÉSTAMO
# =========================

# =========================
# ACTUALIZAR PRÉSTAMO
# =========================

def actualizar_prestamo(
    id,
    id_libro,
    id_lector,
    fecha_prestamo,
    fecha_devolucion_programada,
    fecha_devolucion_real,
    estado,
    observaciones
):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    # Obtener información actual del préstamo
    cursor.execute("""
        SELECT
            IdLibro,
            Estado
        FROM prestamos
        WHERE Id = %s
    """, (id,))

    prestamo_actual = cursor.fetchone()

    if prestamo_actual is None:
        cursor.close()
        conexion.close()
        return

    id_libro_anterior = prestamo_actual[0]
    estado_anterior = prestamo_actual[1]

    # ==========================================
    # ACTUALIZAR DISPONIBILIDAD
    # ==========================================

    # Si estaba prestado
    if estado_anterior == 'Prestado':

        # Si cambió el libro
        if int(id_libro_anterior) != int(id_libro):

            # Devolver disponibilidad del libro anterior
            cursor.execute("""
                UPDATE libros
                SET Disponibles = Disponibles + 1
                WHERE Id = %s
            """, (id_libro_anterior,))

            # Quitar disponibilidad del nuevo libro
            cursor.execute("""
                UPDATE libros
                SET Disponibles = Disponibles - 1
                WHERE Id = %s
                AND Disponibles > 0
            """, (id_libro,))


    # Si antes estaba devuelto y ahora vuelve a estar prestado
    elif estado_anterior == 'Devuelto' and estado == 'Prestado':

        cursor.execute("""
            UPDATE libros
            SET Disponibles = Disponibles - 1
            WHERE Id = %s
            AND Disponibles > 0
        """, (id_libro,))


    # Si antes estaba prestado y ahora lo marcamos como devuelto
    elif estado_anterior == 'Prestado' and estado == 'Devuelto':

        cursor.execute("""
            UPDATE libros
            SET Disponibles = Disponibles + 1
            WHERE Id = %s
        """, (id_libro,))


    # =========================
# ACTUALIZAR PRÉSTAMO
# =========================

def actualizar_prestamo(
    id,
    id_libro,
    id_lector,
    id_usuario,
    fecha_devolucion_programada,
    fecha_devolucion_real,
    estado,
    observaciones
):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE prestamos
        SET
            IdLibro = %s,
            IdLector = %s,
            IdUsuario = %s,
            FechaDevolucionProgramada = %s,
            FechaDevolucionReal = %s,
            Estado = %s,
            Observaciones = %s

        WHERE Id = %s
    """, (
        id_libro,
        id_lector,
        id_usuario,
        fecha_devolucion_programada,
        fecha_devolucion_real,
        estado,
        observaciones,
        id
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


# =========================
# ANULAR PRÉSTAMO
# =========================

def anular_prestamo(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    # Buscar información del préstamo
    cursor.execute("""
        SELECT
            IdLibro,
            Estado
        FROM prestamos
        WHERE Id = %s
    """, (id,))

    prestamo = cursor.fetchone()

    # Si no existe el préstamo, no hacemos nada
    if not prestamo:
        cursor.close()
        conexion.close()
        return

    id_libro = prestamo[0]
    estado = prestamo[1]

    # Solo se pueden anular préstamos
    # que todavía tengan el libro prestado
    if estado in ('Prestado', 'Vencido'):

        # Cambiar estado del préstamo
        cursor.execute("""
            UPDATE prestamos
            SET Estado = 'Anulado'
            WHERE Id = %s
        """, (id,))

        # Devolver el libro al inventario
        cursor.execute("""
            UPDATE libros
            SET Disponibles = Disponibles + 1
            WHERE Id = %s
        """, (id_libro,))

        conexion.commit()

    cursor.close()
    conexion.close()



# =========================
# OBTENER LIBROS PARA PRÉSTAMO
# =========================

def obtener_libros_prestamo():

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT 
            Id,
            Nombre
        FROM libros
        WHERE Estado = '1'
        AND Disponibles > 0
        ORDER BY Nombre ASC
    """)

    libros = cursor.fetchall()

    cursor.close()
    conexion.close()

    return libros


# =========================
# OBTENER LECTORES PARA PRÉSTAMO
# =========================

def obtener_lectores_prestamo():

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT 
            Id,
            NombreCompleto,
            NumeroDocumento
        FROM lectores
        WHERE Estado = 'Activo'
        ORDER BY NombreCompleto ASC
    """)

    lectores = cursor.fetchall()

    cursor.close()
    conexion.close()

    return lectores


# =========================
# OBTENER USUARIOS PARA PRÉSTAMO
# =========================

def obtener_usuarios_prestamo():

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            Id,
            NombreCompleto,
            Usuario
        FROM usuario
        WHERE Estado = 1
        ORDER BY NombreCompleto ASC
    """)

    usuarios = cursor.fetchall()

    cursor.close()
    conexion.close()

    return usuarios


# =========================
# REGISTRAR DEVOLUCIÓN
# =========================

def registrar_devolucion(id, fecha_devolucion_real):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    # Buscar el libro asociado al préstamo
    cursor.execute("""
        SELECT IdLibro
        FROM prestamos
        WHERE Id = %s
        AND Estado = 'Prestado'
    """, (id,))

    prestamo = cursor.fetchone()

    # Si el préstamo existe y está prestado
    if prestamo:

        id_libro = prestamo[0]

        # Registrar la devolución
        cursor.execute("""
            UPDATE prestamos
            SET
                FechaDevolucionReal = %s,
                Estado = 'Devuelto'
            WHERE Id = %s
        """, (
            fecha_devolucion_real,
            id
        ))

        # Aumentar la cantidad disponible del libro
        cursor.execute("""
            UPDATE libros
            SET Disponibles = Disponibles + 1
            WHERE Id = %s
        """, (
            id_libro,
        ))

        conexion.commit()

    cursor.close()
    conexion.close()