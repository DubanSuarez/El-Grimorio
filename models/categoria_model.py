from database.conexion import mysql


# Obtener todas las categorías
def obtener_categorias():

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            Id,
            Nombre,
            Descripcion,
            Estado,
            FechaRegistro
        FROM categorias
    """)

    categorias = cursor.fetchall()

    cursor.close()
    conexion.close()

    return categorias


# Obtener una categoría por ID
def obtener_categoria(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            Id,
            Nombre,
            Descripcion,
            Estado,
            FechaRegistro
        FROM categorias
        WHERE Id = %s
    """, (id,))

    categoria = cursor.fetchone()

    cursor.close()
    conexion.close()

    return categoria


# Registrar categoría
def insertar_categoria(nombre, descripcion, fecha_registro, estado):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO categorias (
            Nombre,
            Descripcion,
            Estado,
            FechaRegistro
        )
        VALUES (%s, %s, %s, %s)
    """, (
        nombre,
        descripcion,
        estado,
        fecha_registro
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


# Actualizar categoría
def actualizar_categoria(id, nombre, descripcion, estado):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE categorias
        SET Nombre = %s,
            Descripcion = %s,
            Estado = %s
        WHERE Id = %s
    """, (
        nombre,
        descripcion,
        estado,
        id
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


# Desactivar categoría
def eliminar_categoria(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE categorias
        SET Estado = 0
        WHERE Id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()


# Reactivar categoría
def reactivar_categoria(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE categorias
        SET Estado = 1
        WHERE Id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()