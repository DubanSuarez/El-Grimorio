#Datos y consultas SQL

from database.conexion import mysql

# Obtener Lista de Libros
def obtener_libros():
    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT 
            libros.Id,
            autores.Nombre AS Autor,
            categorias.Nombre AS Categoria,
            libros.IdEditorial,
            libros.IdIdioma,
            libros.Nombre,
            libros.AñoPublicacion,
            libros.Paginas,
            libros.Descripcion,
            libros.FechaRegistro,
            libros.Imagen,
            libros.Url,
            libros.Cantidad,
            libros.Disponibles,
            libros.Estado
        FROM libros
        INNER JOIN autores 
            ON libros.IdAutor = autores.Id
        INNER JOIN categorias 
            ON libros.IdCategoria = categorias.Id
    """)

    libros = cursor.fetchall()

    cursor.close()
    conexion.close()

    return libros


# Obtener libro para editar
def obtener_libro(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            Id,
            IdAutor,
            IdCategoria,
            IdEditorial,
            IdIdioma,
            Nombre,
            AñoPublicacion,
            Paginas,
            Descripcion,
            FechaRegistro,
            Imagen,
            Url,
            Cantidad,
            Disponibles,
            Estado
        FROM libros
        WHERE Id = %s
    """, (id,))

    libro = cursor.fetchone()

    cursor.close()
    conexion.close()

    return libro


# FUNCIONES PARA LOS SELECT
def obtener_autores():
    conexion=mysql.connect()
    cursor=conexion.cursor()

    cursor.execute(""" SELECT id, Nombre FROM autores ORDER BY Nombre """)

    autores = cursor.fetchall()

    cursor.close()
    conexion.close()

    return autores

def obtener_categorias():
    conexion=mysql.connect()
    cursor=conexion.cursor()

    cursor.execute("""SELECT Id, Nombre FROM categorias ORDER BY Nombre""")

    categorias = cursor.fetchall()

    cursor.close()
    conexion.close()

    return categorias


def obtener_editoriales():
    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT Id, Nombre
        FROM editoriales
        ORDER BY Nombre
    """)

    editoriales = cursor.fetchall()

    cursor.close()
    conexion.close()

    return editoriales


def obtener_idiomas():
    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT Id, Nombre
        FROM idiomas
        ORDER BY Nombre
    """)

    idiomas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return idiomas


# Esta funcion es para mandar los datos a la base de datos
def insertar_libro(id_autor, id_categoria, id_editorial, id_idioma,
                   nombre, anio_publicacion, paginas, descripcion,
                   fecha_registro, imagen, url, cantidad, disponibles, estado):

    conexion=mysql.connect()
    cursor=conexion.cursor()

    cursor.execute("""
        INSERT INTO libros (
            IdAutor,
            IdCategoria,
            IdEditorial,
            IdIdioma,
            Nombre,
            AñoPublicacion,
            Paginas,
            Descripcion,
            FechaRegistro,
            Imagen,
            Url,
            Cantidad,
            Disponibles,
            Estado
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
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
    ))

    conexion.commit()  #MySQL necesita confirmar la transacción para guardar definitivamente el cambio.

    cursor.close()
    conexion.close()




# Función Editar Libro

def actualizar_libro(id, id_autor, id_categoria, id_editorial, id_idioma,
                     nombre, anio_publicacion, paginas, descripcion,
                     imagen, url, cantidad, disponibles, estado):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE libros
        SET
            IdAutor = %s,
            IdCategoria = %s,
            IdEditorial = %s,
            IdIdioma = %s,
            Nombre = %s,
            AñoPublicacion = %s,
            Paginas = %s,
            Descripcion = %s,
            Imagen = %s,
            Url = %s,
            Cantidad = %s,
            Disponibles = %s,
            Estado = %s
        WHERE Id = %s
    """, (
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
        estado,
        id
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


# Funcion Estado / Eliminar y Activar Libro

def eliminar_libro(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE libros
        SET Estado = '0'
        WHERE Id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()


def reactivar_libro(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE libros
        SET Estado = '1'
        WHERE Id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()


# Ver datos del libro

def obtener_libro_por_id(id):

    conexion = mysql.connect()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            libros.Id,
            autores.Nombre AS Autor,
            categorias.Nombre AS Categoria,
            libros.IdEditorial,
            libros.IdIdioma,
            libros.Nombre,
            libros.AñoPublicacion,
            libros.Paginas,
            libros.Descripcion,
            libros.FechaRegistro,
            libros.Imagen,
            libros.Url,
            libros.Cantidad,
            libros.Disponibles,
            libros.Estado
        FROM libros
        INNER JOIN autores
            ON libros.IdAutor = autores.Id
        INNER JOIN categorias
            ON libros.IdCategoria = categorias.Id
        WHERE libros.Id = %s
    """, (id,))

    libro = cursor.fetchone()

    cursor.close()
    conexion.close()

    return libro