from flask import Blueprint, render_template, request, redirect
# Importamos DataTime para fecha acutal
from datetime import datetime
from models.idioma_model import (
    obtener_idiomas,
    obtener_idioma,
    insertar_idioma,
    actualizar_idioma,
    eliminar_idioma,
    reactivar_idioma
)


idiomas_bp = Blueprint(
    'idiomas',
    __name__,
    url_prefix='/admin/idiomas'
)


# LISTAR
@idiomas_bp.route('')
@idiomas_bp.route('/')
def listar_idiomas():

    idiomas = obtener_idiomas()

    return render_template(
        'admin/idiomas/listar.html',
        idiomas=idiomas
    )


# AGREGAR
@idiomas_bp.route('/agregar', methods=['GET', 'POST'])
def agregar_idioma():

    if request.method == 'POST':

        nombre = request.form['txtNombre']
        codigo_iso = request.form['txtCodigoISO']
        estado = request.form['txtEstado']
        fecha_registro = datetime.now() # El sistema toma automaticamente la Fecha de Hoy

        insertar_idioma(
            nombre,
            codigo_iso,
            estado,
            fecha_registro
        )

        return redirect('/admin/idiomas')

    return render_template('admin/idiomas/agregar.html')


# VER
@idiomas_bp.route('/ver/<int:id>')
def ver_idioma(id):

    idioma = obtener_idioma(id)

    return render_template(
        'admin/idiomas/ver.html',
        idioma=idioma
    )


# EDITAR
@idiomas_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_idioma(id):

    if request.method == 'POST':

        nombre = request.form['txtNombre']
        codigo_iso = request.form['txtCodigoISO']
        estado = request.form['txtEstado']

        actualizar_idioma(
            id,
            nombre,
            codigo_iso,
            estado
        )

        return redirect('/admin/idiomas')

    idioma = obtener_idioma(id)

    return render_template(
        'admin/idiomas/editar.html',
        idioma=idioma
    )


# DESACTIVAR
@idiomas_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_idioma_controller(id):

    eliminar_idioma(id)

    return redirect('/admin/idiomas')


# REACTIVAR
@idiomas_bp.route('/reactivar/<int:id>', methods=['POST'])
def reactivar_idioma_controller(id):

    reactivar_idioma(id)

    return redirect('/admin/idiomas')