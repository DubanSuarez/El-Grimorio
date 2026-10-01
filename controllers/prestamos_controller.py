from flask import Blueprint, render_template, request, redirect, session
from datetime import datetime, date
from models.prestamo_model import (
    obtener_prestamos,
    obtener_prestamo,
    insertar_prestamo,
    actualizar_prestamo,
    registrar_devolucion,
    anular_prestamo,
    obtener_libros_prestamo,
    obtener_lectores_prestamo,
    obtener_usuarios_prestamo
)
 

prestamos_bp = Blueprint(
    'prestamos',
    __name__,
    url_prefix='/admin/prestamos'
)


# =========================
# LISTAR
# =========================

@prestamos_bp.route('')
@prestamos_bp.route('/')
def listar_prestamos():

    prestamos = obtener_prestamos()

    return render_template(
        'admin/prestamos/listar.html',
        prestamos=prestamos
    )


# ========================= 
# AGREGAR 
# ========================= 
 
@prestamos_bp.route('/agregar', methods=['GET', 'POST'])
def agregar_prestamo():

    if request.method == 'POST':

        id_libro = request.form['txtIdLibro']
        id_lector = request.form['txtIdLector']

        # Usuario que inició sesión
        id_usuario = session.get('id_usuario')

        fecha_prestamo = datetime.now()

        fecha_devolucion_programada = request.form[
            'txtFechaDevolucionProgramada'
        ]

        estado = 'Prestado'

        observaciones = request.form.get(
            'txtObservaciones'
        ) or None

        insertar_prestamo(
            id_libro,
            id_lector,
            id_usuario,
            fecha_prestamo,
            fecha_devolucion_programada,
            estado,
            observaciones
        )

        return redirect('/admin/prestamos')

    libros = obtener_libros_prestamo()
    lectores = obtener_lectores_prestamo()

    return render_template(
        'admin/prestamos/agregar.html',
        libros=libros,
        lectores=lectores
    )

# =========================
# VER
# =========================

@prestamos_bp.route('/ver/<int:id>')
def ver_prestamo(id):

    prestamo = obtener_prestamo(id)

    if prestamo is None:
        return redirect('/admin/prestamos')

    return render_template(
        'admin/prestamos/ver.html',
        prestamo=prestamo
    )

# =========================
# EDITAR
# =========================

@prestamos_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_prestamo(id):

    prestamo = obtener_prestamo(id)

    if prestamo is None:
        return redirect('/admin/prestamos')


    # =========================
    # PROCESAR FORMULARIO
    # =========================

    if request.method == 'POST':

        # Libro seleccionado
        id_libro = request.form.get('txtIdLibro')

        # Lector seleccionado
        id_lector = request.form.get('txtIdLector')

        # Verificar que lleguen los datos
        if not id_libro or not id_lector:
            return redirect(
                f'/admin/prestamos/editar/{id}'
            )


        # Usuario responsable original
        id_usuario = prestamo[3]

        # Fecha de devolución programada
        fecha_devolucion_programada = request.form.get(
            'txtFechaDevolucionProgramada'
        )

        # Fecha de devolución real
        # No se modifica desde editar
        fecha_devolucion_real = prestamo[7]

        # Estado actual
        # No se modifica desde editar
        estado = prestamo[8]

        # Observaciones
        observaciones = request.form.get(
            'txtObservaciones'
        ) or None


        # =========================
        # ACTUALIZAR PRÉSTAMO
        # =========================

        actualizar_prestamo(
            id,
            id_libro,
            id_lector,
            id_usuario,
            fecha_devolucion_programada,
            fecha_devolucion_real,
            estado,
            observaciones
        )

        return redirect('/admin/prestamos')


    # =========================
    # DATOS PARA EL FORMULARIO
    # =========================

    libros = obtener_libros_prestamo()

    lectores = obtener_lectores_prestamo()


    return render_template(
        'admin/prestamos/editar.html',
        prestamo=prestamo,
        libros=libros,
        lectores=lectores
    )


# =========================
# DEVOLVER PRÉSTAMO
# =========================

@prestamos_bp.route('/devolver/<int:id>')
def devolver_prestamo(id):

    prestamo = obtener_prestamo(id)

    if prestamo is None:
        return redirect('/admin/prestamos')

    fecha_devolucion = date.today()

    registrar_devolucion(
        id,
        fecha_devolucion
    )

    return redirect('/admin/prestamos')


# =========================
# ANULAR
# =========================

@prestamos_bp.route('/anular/<int:id>', methods=['POST'])
def anular_prestamo_controller(id):

    anular_prestamo(id)

    return redirect('/admin/prestamos')