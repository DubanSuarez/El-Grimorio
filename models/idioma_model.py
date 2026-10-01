from database.conexion import mysql

def obtener_idiomas():

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            Id,
            Nombre,
            CodigoISO,
            Estado,
            FechaRegistro
        FROM idiomas
    """)

    idiomas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return idiomas


def obtener_idioma(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            Id,
            Nombre,
            CodigoISO,
            Estado,
            FechaRegistro
        FROM idiomas
        WHERE Id = %s
    """, (id,))

    idioma = cursor.fetchone()

    cursor.close()
    conexion.close()

    return idioma


def insertar_idioma(nombre, codigo_iso, estado,fecha_registro):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO idiomas (
            Nombre,
            CodigoISO,
            Estado,
            FechaRegistro
        )
        VALUES (%s, %s, %s, %s)
    """, (
        nombre,
        codigo_iso,
        estado,
        fecha_registro
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


def actualizar_idioma(id, nombre, codigo_iso, estado):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE idiomas
        SET
            Nombre = %s,
            CodigoISO = %s,
            Estado = %s
        WHERE Id = %s
    """, (
        nombre,
        codigo_iso,
        estado,
        id
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


def eliminar_idioma(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE idiomas
        SET Estado = 0
        WHERE Id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()


def reactivar_idioma(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE idiomas
        SET Estado = 1
        WHERE Id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()