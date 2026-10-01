from database.conexion import mysql


def obtener_editoriales():

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            Id,
            Nombre,
            Pais,
            Ciudad,
            SitioWeb,
            Estado,
            FechaRegistro
        FROM editoriales
    """)

    editoriales = cursor.fetchall()

    cursor.close()
    conexion.close()

    return editoriales


def obtener_editorial(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            Id,
            Nombre,
            Pais,
            Ciudad,
            SitioWeb,
            Estado,
            FechaRegistro
        FROM editoriales
        WHERE Id = %s
    """, (id,))

    editorial = cursor.fetchone()

    cursor.close()
    conexion.close()

    return editorial


def insertar_editorial(nombre, pais, ciudad, sitio_web, estado, fecha_registro):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO editoriales (
            Nombre,
            Pais,
            Ciudad,
            SitioWeb,
            Estado,
            FechaRegistro
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        nombre,
        pais,
        ciudad,
        sitio_web,
        estado,
        fecha_registro
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


def actualizar_editorial(id, nombre, pais, ciudad, sitio_web, estado):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE editoriales
        SET
            Nombre = %s,
            Pais = %s,
            Ciudad = %s,
            SitioWeb = %s,
            Estado = %s
        WHERE Id = %s
    """, (
        nombre,
        pais,
        ciudad,
        sitio_web,
        estado,
        id
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


def eliminar_editorial(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE editoriales
        SET Estado = 0
        WHERE Id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()


def reactivar_editorial(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE editoriales
        SET Estado = 1
        WHERE Id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()