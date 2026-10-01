# Datos y consultas SQL

from database.conexion import mysql
from werkzeug.security import generate_password_hash

# =========================
# LOGIN
# =========================

def obtener_usuario_login(usuario):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            Id,
            IdRol,
            Usuario,
            NombreCompleto,
            Contrasena,
            Correo,
            Estado
        FROM usuario
        WHERE Usuario = %s
        LIMIT 1
    """, (usuario,))

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    return resultado


# =========================
# LISTAR USUARIOS
# =========================

def obtener_usuarios():

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            usuario.Id,
            rol.Nombre AS Rol,
            usuario.Usuario,
            usuario.NombreCompleto,
            usuario.Correo,
            usuario.Estado,
            usuario.FechaRegistro
        FROM usuario
        INNER JOIN rol
            ON usuario.IdRol = rol.Id
        ORDER BY usuario.Id DESC
    """)

    usuarios = cursor.fetchall()

    cursor.close()
    conexion.close()

    return usuarios


# =========================
# OBTENER USUARIO
# =========================

def obtener_usuario(id):

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
    """, (id,))

    usuario = cursor.fetchone()

    cursor.close()
    conexion.close()

    return usuario


# =========================
# OBTENER ROLES
# =========================

def obtener_roles():

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            Id,
            Nombre
        FROM rol
        ORDER BY Nombre
    """)

    roles = cursor.fetchall()

    cursor.close()
    conexion.close()

    return roles


# =========================
# INSERTAR USUARIO
# =========================

def insertar_usuario(
    id_rol,
    usuario,
    contrasena,
    nombre_completo,
    correo,
    estado
):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    # Encriptar contraseña
    contrasena_hash = generate_password_hash(contrasena)

    cursor.execute("""
        INSERT INTO usuario (
            IdRol,
            Usuario,
            Contrasena,
            NombreCompleto,
            Correo,
            Estado,
            FechaRegistro
        )
        VALUES (%s, %s, %s, %s, %s, %s, CURDATE())
    """, (
        id_rol,
        usuario,
        contrasena_hash,
        nombre_completo,
        correo,
        estado
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


# =========================
# EDITAR USUARIO
# =========================

def editar_usuario(
    id,
    id_rol,
    usuario,
    nombre_completo,
    correo,
    estado,
    contrasena=None
):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    # Si se escribió una nueva contraseña
    if contrasena:

        contrasena_hash = generate_password_hash(contrasena)

        cursor.execute("""
            UPDATE usuario
            SET
                IdRol = %s,
                Usuario = %s,
                Contrasena = %s,
                NombreCompleto = %s,
                Correo = %s,
                Estado = %s
            WHERE Id = %s
        """, (
            id_rol,
            usuario,
            contrasena_hash,
            nombre_completo,
            correo,
            estado,
            id
        ))

    # Si no se modificó la contraseña
    else:

        cursor.execute("""
            UPDATE usuario
            SET
                IdRol = %s,
                Usuario = %s,
                NombreCompleto = %s,
                Correo = %s,
                Estado = %s
            WHERE Id = %s
        """, (
            id_rol,
            usuario,
            nombre_completo,
            correo,
            estado,
            id
        ))

    conexion.commit()

    cursor.close()
    conexion.close()


# =========================
# DESACTIVAR USUARIO
# =========================

def eliminar_usuario(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE usuario
        SET Estado = 0
        WHERE Id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()


# =========================
# REACTIVAR USUARIO
# =========================

def reactivar_usuario(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE usuario
        SET Estado = 1
        WHERE Id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()