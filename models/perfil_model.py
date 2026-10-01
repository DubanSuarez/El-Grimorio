# =========================================================
# DATOS Y CONSULTAS SQL DEL PERFIL
# =========================================================

from database.conexion import mysql

from werkzeug.security import generate_password_hash


# =========================================================
# OBTENER PERFIL
# =========================================================

def obtener_perfil(id_usuario):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            usuario.Id,
            usuario.IdRol,
            rol.Nombre AS Rol,
            usuario.Usuario,
            usuario.NombreCompleto,
            usuario.Correo,
            usuario.Estado,
            usuario.FechaRegistro
        FROM usuario

        INNER JOIN rol
            ON usuario.IdRol = rol.Id

        WHERE usuario.Id = %s
    """, (id_usuario,))

    perfil = cursor.fetchone()

    cursor.close()
    conexion.close()

    return perfil


# =========================================================
# OBTENER CONTRASEÑA
# =========================================================

def obtener_contrasena(id_usuario):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT Contrasena
        FROM usuario
        WHERE Id = %s
    """, (id_usuario,))

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    return resultado


# =========================================================
# CAMBIAR CONTRASEÑA
# =========================================================

def cambiar_contrasena(
    id_usuario,
    nueva_contrasena
):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    # -----------------------------------------
    # GENERAR HASH
    # -----------------------------------------

    contrasena_hash = generate_password_hash(
        nueva_contrasena
    )

    # -----------------------------------------
    # ACTUALIZAR CONTRASEÑA
    # -----------------------------------------

    cursor.execute("""
        UPDATE usuario
        SET Contrasena = %s
        WHERE Id = %s
    """, (
        contrasena_hash,
        id_usuario
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


# =========================================================
# ACTUALIZAR PERFIL
# =========================================================

def actualizar_perfil(
    id_usuario,
    usuario,
    nombre_completo,
    correo
):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE usuario
        SET
            Usuario = %s,
            NombreCompleto = %s,
            Correo = %s
        WHERE Id = %s
    """, (
        usuario,
        nombre_completo,
        correo,
        id_usuario
    ))

    conexion.commit()

    cursor.close()
    conexion.close()