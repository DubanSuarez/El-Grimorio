from flask import Blueprint, render_template, request, redirect, flash
# Importamos autor_model.py
from models.autor_model import (
    obtener_autores,
    insertar_autor,
    obtener_autor,
    actualizar_autor,
    tiene_libros,
    eliminar_autor
)

autores_bp = Blueprint('autores',__name__,url_prefix='/admin/autores')


@autores_bp.route('')
@autores_bp.route('/')
def listar_autores():

    autores = obtener_autores()

    return render_template(
        'admin/autores/listar.html',
        autores=autores
    )



# Registrar Autor

@autores_bp.route('/agregar', methods=['GET', 'POST'])
def agregar_autor():

    if request.method == 'POST':

        nombre = request.form['txtNombre']
        nacionalidad = request.form['txtNacionalidad']
        fecha_nacimiento = request.form['txtFechaNacimiento']
        fecha_fallecimiento = request.form['txtFechaFallecimiento']
        biografia = request.form['txtBiografia']

        insertar_autor(
            nombre,
            nacionalidad,
            fecha_nacimiento,
            fecha_fallecimiento,
            biografia
        )

        flash('El autor se registró correctamente.', 'success')
        return redirect('/admin/autores')

    return render_template('admin/autores/agregar.html')


# Actualizar Autor

@autores_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_autor(id):

    if request.method == 'POST':

        nombre = request.form['txtNombre']
        nacionalidad = request.form['txtNacionalidad']
        fecha_nacimiento = request.form['txtFechaNacimiento']
        fecha_fallecimiento = request.form.get('txtFechaFallecimiento')
        biografia = request.form['txtBiografia']

        actualizar_autor(
            id,
            nombre,
            nacionalidad,
            fecha_nacimiento,
            fecha_fallecimiento,
            biografia
        )

        flash('El autor se actualizó correctamente.', 'success')
        return redirect('/admin/autores')

    autor = obtener_autor(id)

    return render_template(
        'admin/autores/editar.html',
        autor=autor
    )


# Ruta de eliminar

@autores_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_autor_controller(id):

    if tiene_libros(id):

        flash(
        'No se puede eliminar el autor porque tiene libros asociados.',
        'warning'
    )
        return redirect('/admin/autores')

    eliminar_autor(id)

    flash('El autor se eliminó correctamente.', 'success')
    return redirect('/admin/autores')


# Ruta ver autor

@autores_bp.route('/ver/<int:id>')
def ver_autor(id):

    autor = obtener_autor(id)

    if autor is None:
        return redirect('/admin/autores')

    return render_template(
        'admin/autores/ver.html',
        autor=autor
    )