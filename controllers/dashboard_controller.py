from flask import Blueprint, render_template
from datetime import datetime

from models.dashboard_model import (
    obtener_estadisticas,
    obtener_actividad_reciente,
    obtener_libros_mas_solicitados
)


dashboard_bp = Blueprint(
    'dashboard',
    __name__,
    url_prefix='/admin'
)


@dashboard_bp.route('/dashboard')
def dashboard():

    estadisticas = obtener_estadisticas()

    actividad = obtener_actividad_reciente()

    libros_populares = obtener_libros_mas_solicitados()

    ahora = datetime.now()

    return render_template(
        'admin/dashboard/index.html',
        estadisticas=estadisticas,
        actividad=actividad,
        libros_populares=libros_populares,
        now=ahora
    ) 