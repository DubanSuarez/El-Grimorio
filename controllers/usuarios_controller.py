# Rutas y lógica de petición
from flask import Blueprint, render_template, request, redirect, session

from models.usuario_model import (
    obtener_usuarios,
    obtener_usuario,
    obtener_roles,
    insertar_usuario,
    editar_usuario,
    eliminar_usuario,
    reactivar_usuario
)


usuarios_bp = Blueprint(
    'usuarios',
    __name__,
    url_prefix='/admin/usuarios'
)


# =========================
# LISTAR
# =========================

@usuarios_bp.route('')
@usuarios_bp.route('/')
def listar_usuarios():

    usuarios = obtener_usuarios()

    # ID del usuario que está actualmente conectado
    usuario_actual = session.get('id_usuario')

    # Excluir al usuario que está conectado
    usuarios = [
        usuario for usuario in usuarios
        if usuario[0] != usuario_actual
    ]

    return render_template(
        'admin/usuarios/listar.html',
        usuarios=usuarios
    )


# =========================
# AGREGAR
# =========================

@usuarios_bp.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():

    if request.method == 'POST':

        id_rol = request.form['txtIdRol']
        usuario = request.form['txtUsuario']
        contrasena = request.form['txtContrasena']
        nombre_completo = request.form['txtNombreCompleto']
        correo = request.form['txtCorreo']
        estado = request.form['txtEstado']

        insertar_usuario(
            id_rol,
            usuario,
            contrasena,
            nombre_completo,
            correo,
            estado
        )

        return redirect('/admin/usuarios')

    roles = obtener_roles()

    return render_template(
        'admin/usuarios/agregar.html',
        roles=roles
    )


# =========================
# VER
# =========================

@usuarios_bp.route('/ver/<int:id>')
def ver_usuario(id):

    usuario = obtener_usuario(id)

    return render_template(
        'admin/usuarios/ver.html',
        usuario=usuario
    )


# =========================
# EDITAR
# =========================

@usuarios_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario_controller(id):

    if request.method == 'POST':

        id_rol = request.form['txtIdRol']
        usuario = request.form['txtUsuario']
        nombre_completo = request.form['txtNombreCompleto']
        correo = request.form['txtCorreo']
        estado = request.form['txtEstado']

        # La contraseña es opcional al editar
        contrasena = request.form.get('txtContrasena')

        editar_usuario(
            id,
            id_rol,
            usuario,
            nombre_completo,
            correo,
            estado,
            contrasena
        )

        return redirect('/admin/usuarios')

    usuario = obtener_usuario(id)
    roles = obtener_roles()

    return render_template(
        'admin/usuarios/editar.html',
        usuario=usuario,
        roles=roles
    )

# =========================
# DESACTIVAR
# =========================

@usuarios_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_usuario_controller(id):

    eliminar_usuario(id)

    return redirect('/admin/usuarios')


# =========================
# REACTIVAR
# =========================

@usuarios_bp.route('/reactivar/<int:id>', methods=['POST'])
def reactivar_usuario_controller(id):

    reactivar_usuario(id)

    return redirect('/admin/usuarios')