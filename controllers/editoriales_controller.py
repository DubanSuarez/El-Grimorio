from flask import Blueprint, render_template, request, redirect

from models.editorial_model import (
    obtener_editoriales,
    obtener_editorial,
    insertar_editorial,
    actualizar_editorial,
    eliminar_editorial,
    reactivar_editorial
)


editoriales_bp = Blueprint(
    'editoriales',
    __name__,
    url_prefix='/admin/editoriales'
)


# LISTAR
@editoriales_bp.route('')
@editoriales_bp.route('/')
def listar_editoriales():

    editoriales = obtener_editoriales()

    return render_template(
        'admin/editoriales/listar.html',
        editoriales=editoriales
    )


# AGREGAR
@editoriales_bp.route('/agregar', methods=['GET', 'POST'])
def agregar_editorial():

    if request.method == 'POST':

        nombre = request.form['txtNombre']
        pais = request.form['txtPais']
        ciudad = request.form['txtCiudad']
        sitio_web = request.form['txtSitioWeb']
        estado = request.form['txtEstado']
        fecha_registro = request.form['txtFechaRegistro']

        insertar_editorial(
            nombre,
            pais,
            ciudad,
            sitio_web,
            estado,
            fecha_registro
        )

        return redirect('/admin/editoriales')

    return render_template('admin/editoriales/agregar.html')


# VER
@editoriales_bp.route('/ver/<int:id>')
def ver_editorial(id):

    editorial = obtener_editorial(id)

    return render_template(
        'admin/editoriales/ver.html',
        editorial=editorial
    )


# EDITAR
@editoriales_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_editorial(id):

    if request.method == 'POST':

        nombre = request.form['txtNombre']
        pais = request.form['txtPais']
        ciudad = request.form['txtCiudad']
        sitio_web = request.form['txtSitioWeb']
        estado = request.form['txtEstado']

        actualizar_editorial(
            id,
            nombre,
            pais,
            ciudad,
            sitio_web,
            estado
        )

        return redirect('/admin/editoriales')

    editorial = obtener_editorial(id)

    return render_template(
        'admin/editoriales/editar.html',
        editorial=editorial
    )


# DESACTIVAR
@editoriales_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_editorial_controller(id):

    eliminar_editorial(id)

    return redirect('/admin/editoriales')


# REACTIVAR
@editoriales_bp.route('/reactivar/<int:id>', methods=['POST'])
def reactivar_editorial_controller(id):

    reactivar_editorial(id)

    return redirect('/admin/editoriales')