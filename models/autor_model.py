# Datos y consultas SQL

from database.conexion import mysql


def obtener_autores():

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            Id,
            Nombre,
            nacionalidad,
            fecha_nacimiento,
            fecha_fallecimiento,
            biografia
        FROM autores
    """)

    autores = cursor.fetchall()

    cursor.close()
    conexion.close()

    return autores


# Registrar autor

def insertar_autor(nombre, nacionalidad, fecha_nacimiento,
                   fecha_fallecimiento, biografia):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO autores (
            Nombre,
            nacionalidad,
            fecha_nacimiento,
            fecha_fallecimiento,
            biografia
        )
        VALUES (%s, %s, %s, %s, %s)
    """, (
        nombre,
        nacionalidad,
        fecha_nacimiento,
        fecha_fallecimiento,
        biografia
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


# Actualizar autor

def obtener_autor(id):
    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT Id, Nombre, nacionalidad, fecha_nacimiento,
               fecha_fallecimiento, biografia
        FROM autores
        WHERE Id = %s
    """, (id,))

    autor = cursor.fetchone()

    cursor.close()
    conexion.close()

    return autor


def actualizar_autor(id, nombre, nacionalidad, fecha_nacimiento,
                     fecha_fallecimiento, biografia):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE autores
        SET Nombre = %s,
            nacionalidad = %s,
            fecha_nacimiento = %s,
            fecha_fallecimiento = %s,
            biografia = %s
        WHERE Id = %s
    """, (
        nombre,
        nacionalidad,
        fecha_nacimiento,
        fecha_fallecimiento,
        biografia,
        id
    ))

    conexion.commit()

    cursor.close()
    conexion.close()



# ELiminar autor

def tiene_libros(id_autor):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM libros
        WHERE IdAutor = %s
    """, (id_autor,))

    cantidad = cursor.fetchone()[0]

    cursor.close()
    conexion.close()

    return cantidad > 0


def eliminar_autor(id_autor):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM autores
        WHERE Id = %s
    """, (id_autor,))

    conexion.commit()

    cursor.close()
    conexion.close()


# Ver autor

def obtener_autor(id):
    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT Id, Nombre, nacionalidad, fecha_nacimiento,
               fecha_fallecimiento, biografia
        FROM autores
        WHERE Id = %s
    """, (id,))

    autor = cursor.fetchone()

    cursor.close()
    conexion.close()

    return autor