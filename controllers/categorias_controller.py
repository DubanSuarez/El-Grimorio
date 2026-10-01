# Rutas y lógica de petición

from flask import Blueprint, render_template, request, redirect, flash

from models.categoria_model import (
    obtener_categorias,
    insertar_categoria,
    obtener_categoria,
    actualizar_categoria,
    eliminar_categoria,
    reactivar_categoria
)


categorias_bp = Blueprint(
    'categorias',
    __name__,
    url_prefix='/admin/categorias'
)


# ==========================================================
# LISTAR CATEGORÍAS
# ==========================================================

@categorias_bp.route('')
@categorias_bp.route('/')
def listar_categorias():

    categorias = obtener_categorias()

    return render_template(
        'admin/categorias/listar.html',
        categorias=categorias
    )


# ==========================================================
# AGREGAR CATEGORÍA
# ==========================================================

@categorias_bp.route('/agregar', methods=['GET', 'POST'])
def agregar_categoria():

    if request.method == 'POST':

        nombre = request.form['txtNombre']
        descripcion = request.form['txtDescripcion']
        fecha_registro = request.form['txtFechaRegistro']
        estado = request.form['txtEstado']

        insertar_categoria(
            nombre,
            descripcion,
            fecha_registro,
            estado
        )

        flash(
            'La categoría se registró correctamente.',
            'success'
        )

        return redirect('/admin/categorias')

    return render_template(
        'admin/categorias/agregar.html'
    )


# ==========================================================
# EDITAR CATEGORÍA
# ==========================================================

@categorias_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_categoria(id):

    if request.method == 'POST':

        nombre = request.form['txtNombre']
        descripcion = request.form['txtDescripcion']
        estado = request.form['txtEstado']

        actualizar_categoria(
            id,
            nombre,
            descripcion,
            estado
        )

        flash(
            'La categoría se actualizó correctamente.',
            'success'
        )

        return redirect('/admin/categorias')

    categoria = obtener_categoria(id)

    if categoria is None:
        flash(
            'La categoría no existe.',
            'danger'
        )

        return redirect('/admin/categorias')

    return render_template(
        'admin/categorias/editar.html',
        categoria=categoria
    )


# ==========================================================
# VER CATEGORÍA
# ==========================================================

@categorias_bp.route('/ver/<int:id>')
def ver_categoria(id):

    categoria = obtener_categoria(id)

    if categoria is None:
        flash(
            'La categoría no existe.',
            'danger'
        )

        return redirect('/admin/categorias')

    return render_template(
        'admin/categorias/ver.html',
        categoria=categoria
    )


# ==========================================================
# DESACTIVAR CATEGORÍA
# ==========================================================

@categorias_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_categoria_controller(id):

    eliminar_categoria(id)

    flash(
        'La categoría se desactivó correctamente.',
        'success'
    )

    return redirect('/admin/categorias')


# ==========================================================
# REACTIVAR CATEGORÍA
# ==========================================================

@categorias_bp.route('/reactivar/<int:id>', methods=['POST'])
def reactivar_categoria_controller(id):

    reactivar_categoria(id)

    flash(
        'La categoría se reactivó correctamente.',
        'success'
    )

    return redirect('/admin/categorias')