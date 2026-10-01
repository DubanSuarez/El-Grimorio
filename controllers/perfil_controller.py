from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    request,
    flash,
    url_for
)

from werkzeug.security import check_password_hash

from models.perfil_model import (
    obtener_perfil,
    obtener_contrasena,
    cambiar_contrasena,
    actualizar_perfil
)


# =========================================================
# BLUEPRINT
# =========================================================

perfil_bp = Blueprint(
    'perfil',
    __name__,
    url_prefix='/admin/perfil'
)


# =========================================================
# PERFIL
# =========================================================

@perfil_bp.route('/')
def perfil():

    if not session.get('login'):
        return redirect('/admin/')

    id_usuario = session['id_usuario']

    datos_perfil = obtener_perfil(
        id_usuario
    )

    return render_template(
        'admin/perfil/index.html',
        perfil=datos_perfil
    )


# =========================================================
# CAMBIAR CONTRASEÑA
# =========================================================

@perfil_bp.route(
    '/cambiar-contrasena',
    methods=['GET', 'POST']
)
def cambiar_password():

    if not session.get('login'):
        return redirect('/admin/')

    if request.method == 'POST':

        id_usuario = session['id_usuario']

        contrasena_actual = request.form[
            'txtContrasenaActual'
        ]

        nueva_contrasena = request.form[
            'txtNuevaContrasena'
        ]

        confirmar_contrasena = request.form[
            'txtConfirmarContrasena'
        ]


        # =================================================
        # OBTENER CONTRASEÑA ACTUAL
        # =================================================

        resultado = obtener_contrasena(
            id_usuario
        )


        if resultado is None:

            flash(
                'No se pudo obtener la contraseña del usuario.',
                'danger'
            )

            return redirect(
                url_for('perfil.cambiar_password')
            )


        # =================================================
        # VALIDAR CONTRASEÑA ACTUAL
        # =================================================

        if not check_password_hash(
            resultado[0],
            contrasena_actual
        ):

            flash(
                'La contraseña actual es incorrecta.',
                'danger'
            )

            return redirect(
                url_for('perfil.cambiar_password')
            )


        # =================================================
        # VALIDAR CONFIRMACIÓN
        # =================================================

        if nueva_contrasena != confirmar_contrasena:

            flash(
                'Las nuevas contraseñas no coinciden.',
                'danger'
            )

            return redirect(
                url_for('perfil.cambiar_password')
            )


        # =================================================
        # ACTUALIZAR CONTRASEÑA
        # =================================================

        cambiar_contrasena(
            id_usuario,
            nueva_contrasena
        )


        # =================================================
        # MENSAJE
        # =================================================

        flash(
            'Contraseña actualizada correctamente.',
            'success'
        )


        return redirect(
            url_for('perfil.perfil')
        )


    # =====================================================
    # MOSTRAR FORMULARIO
    # =====================================================

    return render_template(
        'admin/perfil/cambiar_contrasena.html'
    )


# =========================================================
# EDITAR PERFIL
# =========================================================

@perfil_bp.route(
    '/editar',
    methods=['GET', 'POST']
)
def editar():

    if not session.get('login'):
        return redirect('/admin/')

    id_usuario = session['id_usuario']


    # =====================================================
    # PROCESAR FORMULARIO
    # =====================================================

    if request.method == 'POST':

        usuario = request.form[
            'txtUsuario'
        ].strip()

        nombre_completo = request.form[
            'txtNombreCompleto'
        ].strip()

        correo = request.form[
            'txtCorreo'
        ].strip()


        # =================================================
        # VALIDAR CAMPOS
        # =================================================

        if not usuario or not nombre_completo or not correo:

            flash(
                'Todos los campos son obligatorios.',
                'danger'
            )

            return redirect(
                url_for('perfil.editar')
            )


        # =================================================
        # ACTUALIZAR BASE DE DATOS
        # =================================================

        actualizar_perfil(
            id_usuario,
            usuario,
            nombre_completo,
            correo
        )


        # =================================================
        # ACTUALIZAR SESIÓN
        # =================================================

        session['usuario'] = usuario

        session['nombre_completo'] = nombre_completo

        session['correo'] = correo


        # =================================================
        # MENSAJE
        # =================================================

        flash(
            'Perfil actualizado correctamente.',
            'success'
        )


        return redirect(
            url_for('perfil.perfil')
        )


    # =====================================================
    # MOSTRAR FORMULARIO
    # =====================================================

    datos_perfil = obtener_perfil(
        id_usuario
    )

    return render_template(
        'admin/perfil/editar.html',
        perfil=datos_perfil
    )