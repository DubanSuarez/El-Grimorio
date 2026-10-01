from datetime import date
from flask import Blueprint, render_template, request, redirect
from models.lector_model import (
    obtener_lectores,
    obtener_lector,
    insertar_lector,
    actualizar_lector,
    desactivar_lector,
    reactivar_lector
)

lectores_bp = Blueprint(
    'lectores',
    __name__,
    url_prefix='/admin/lectores'
)


# =========================
# LISTAR LECTORES
# =========================

@lectores_bp.route('')
@lectores_bp.route('/')
def listar_lectores():

    lectores = obtener_lectores()

    return render_template(
        'admin/lectores/listar.html',
        lectores=lectores
    )


# =========================
# AGREGAR LECTOR
# =========================

@lectores_bp.route('/agregar', methods=['GET', 'POST'])
def agregar_lector():

    if request.method == 'POST':

        tipo_documento = request.form['txtTipoDocumento']
        numero_documento = request.form['txtNumeroDocumento']
        nombre_completo = request.form['txtNombreCompleto']

        telefono = request.form.get('txtTelefono') or None
        correo = request.form.get('txtCorreo') or None
        direccion = request.form.get('txtDireccion') or None

        tipo_lector = request.form['txtTipoLector']
        estado = request.form['txtEstado']

        fecha_registro = date.today()

        insertar_lector(
            tipo_documento,
            numero_documento,
            nombre_completo,
            telefono,
            correo,
            direccion,
            tipo_lector,
            estado,
            fecha_registro
        )

        return redirect('/admin/lectores')

    return render_template(
        'admin/lectores/agregar.html'
    )


# =========================
# VER LECTOR
# =========================

@lectores_bp.route('/ver/<int:id>')
def ver_lector(id):

    lector = obtener_lector(id)

    if lector is None:
        return redirect('/admin/lectores')

    return render_template(
        'admin/lectores/ver.html',
        lector=lector
    )


# =========================
# EDITAR LECTOR
# =========================

@lectores_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_lector(id):

    lector = obtener_lector(id)

    if lector is None:
        return redirect('/admin/lectores')


    if request.method == 'POST':

        tipo_documento = request.form['txtTipoDocumento']
        numero_documento = request.form['txtNumeroDocumento']
        nombre_completo = request.form['txtNombreCompleto']

        telefono = request.form.get('txtTelefono') or None
        correo = request.form.get('txtCorreo') or None
        direccion = request.form.get('txtDireccion') or None

        tipo_lector = request.form['txtTipoLector']
        estado = request.form['txtEstado']

        actualizar_lector(
            id,
            tipo_documento,
            numero_documento,
            nombre_completo,
            telefono,
            correo,
            direccion,
            tipo_lector,
            estado
        )

        return redirect('/admin/lectores')


    return render_template(
        'admin/lectores/editar.html',
        lector=lector
    )


# =========================
# DESACTIVAR LECTOR
# =========================

@lectores_bp.route('/eliminar/<int:id>', methods=['POST'])
def desactivar_lector_controller(id):

    desactivar_lector(id)

    return redirect('/admin/lectores')


# =========================
# REACTIVAR LECTOR
# =========================

@lectores_bp.route('/reactivar/<int:id>', methods=['POST'])
def reactivar_lector_controller(id):

    reactivar_lector(id)

    return redirect('/admin/lectores')