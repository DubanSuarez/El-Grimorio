# Esto para Imagenes
import os
from werkzeug.utils import secure_filename
#Rutas y lógica de petición
from flask import Blueprint, render_template, request, redirect, flash
# Importamos las funciones que tenemos en el archivo libro_model
from models.libro_model import (
    obtener_libros,
    insertar_libro,
    obtener_libro,
    obtener_libro_por_id,
    actualizar_libro,
    eliminar_libro,
    reactivar_libro,
    obtener_autores,
    obtener_categorias,
    obtener_editoriales,
    obtener_idiomas
)
# Importamos DataTime para fecha acutal
from datetime import datetime


libros_bp = Blueprint('libros',__name__,url_prefix='/admin/libros')

@libros_bp.route('')
@libros_bp.route('/')
def listar_libros():

    libros = obtener_libros()

    return render_template('admin/libros/listar.html',libros=libros)



# Agregar Libro
# Creamos la ruta que acepta dos tipos de petición 
# Get = Mostrar el formulario
# Post = Recibir los datos y guardarlos

@libros_bp.route('/agregar', methods=['GET', 'POST'])
def agregar_libro():

    if request.method == 'POST':

# El request.form obtiene los datos del form del html

        id_autor = request.form['txtIdAutor']
        id_categoria = request.form['txtIdCategoria']
        id_editorial = request.form['txtIdEditorial']
        id_idioma = request.form['txtIdIdioma']
        nombre = request.form['txtNombre']
        anio_publicacion = request.form['txtAnioPublicacion']
        paginas = request.form['txtPaginas']
        descripcion = request.form['txtDescripcion']
        fecha_registro = datetime.now() # El sistema toma automaticamente la Fecha de Hoy
        url = request.form['txtUrl']
        cantidad = request.form['txtCantidad']
        disponibles = request.form['txtDisponibles']
        estado = request.form['txtEstado']

        
        imagen = request.files['Imagen'] #Recibe el archivo
        if imagen and imagen.filename:
            nombre_imagen = secure_filename(imagen.filename) #Limpia el nombre para evitar caracteres problemáticos
            ruta = os.path.join('static','img','libros',nombre_imagen) #os.path construye la url ('static/img/libros/nombre_imagen.jpg')
            imagen.save(ruta) #guarda físicamente la imagen
            imagen=nombre_imagen #imagen deja de ser el archivo y pasa a acontener solamente el nombre (harry-potter.jpg)
        else:
            imagen=None
        

# El insertar_ libro lleva la informacion al archivo libro_model.py
        insertar_libro(
            id_autor,
            id_categoria,
            id_editorial,
            id_idioma,
            nombre,
            anio_publicacion,
            paginas,
            descripcion,
            fecha_registro,
            imagen,
            url,
            cantidad,
            disponibles,
            estado
        )

        flash('El libro se registró correctamente.', 'success')

        return redirect('/admin/libros')

    autores = obtener_autores()
    categorias = obtener_categorias()
    editoriales = obtener_editoriales()
    idiomas = obtener_idiomas()

    #Enviamos los datos Python a Html
    return render_template(
        'admin/libros/agregar.html',
        autores=autores,
        categorias=categorias,
        editoriales=editoriales,
        idiomas=idiomas
    )



# Actualizar Libro

@libros_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_libro(id):

    if request.method == 'POST':

        id_autor = request.form['txtIdAutor']
        id_categoria = request.form['txtIdCategoria']
        id_editorial = request.form['txtIdEditorial']
        id_idioma = request.form['txtIdIdioma']
        nombre = request.form['txtNombre']
        anio_publicacion = request.form['txtAnioPublicacion']
        paginas = request.form['txtPaginas']
        descripcion = request.form['txtDescripcion']
        url = request.form['txtUrl']
        cantidad = request.form['txtCantidad']
        disponibles = request.form['txtDisponibles']
        estado = request.form['txtEstado']

        # Imagen nueva
        imagen_archivo = request.files.get('Imagen')

        if imagen_archivo and imagen_archivo.filename:

            from werkzeug.utils import secure_filename
            import os

            nombre_imagen = secure_filename(imagen_archivo.filename)

            ruta = os.path.join(
                'static',
                'img',
                'libros',
                nombre_imagen
            )

            imagen_archivo.save(ruta)

            imagen = nombre_imagen

        else:
            # Si no selecciona una imagen nueva,
            # conservamos la imagen actual
            libro_actual = obtener_libro(id)
            imagen = libro_actual[10]

        actualizar_libro(
            id,
            id_autor,
            id_categoria,
            id_editorial,
            id_idioma,
            nombre,
            anio_publicacion,
            paginas,
            descripcion,
            imagen,
            url,
            cantidad,
            disponibles,
            estado
        )

        flash('El libro se actualizó correctamente.', 'success')

        return redirect('/admin/libros')

    # Obtener el libro actual
    libro = obtener_libro(id)

    # Obtener opciones de los selects
    autores = obtener_autores()
    categorias = obtener_categorias()
    editoriales = obtener_editoriales()
    idiomas = obtener_idiomas()

    return render_template(
        'admin/libros/editar.html',
        libro=libro,
        autores=autores,
        categorias=categorias,
        editoriales=editoriales,
        idiomas=idiomas
    )


# Ruta para Eliminar libro

@libros_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_libro_controller(id):

    eliminar_libro(id)

    return redirect('/admin/libros')


@libros_bp.route('/reactivar/<int:id>', methods=['POST'])
def reactivar_libro_controller(id):

    reactivar_libro(id)

    return redirect('/admin/libros')


# Ver información de un libro

@libros_bp.route('/ver/<int:id>')
def ver_libro(id):

    libro = obtener_libro_por_id(id)

    return render_template(
        'admin/libros/ver.html',
        libro=libro
    )