from flask import Flask, session, flash
from functools import wraps
from flask import render_template, request, redirect

from database.conexion import configurar_mysql, mysql

# Para verificar contraseñas
from werkzeug.security import check_password_hash

# Modelo de usuarios
from models.usuario_model import obtener_usuario_login

# Importamos los controladores
from controllers.libros_controller import libros_bp
from controllers.autores_controller import autores_bp
from controllers.categorias_controller import categorias_bp
from controllers.editoriales_controller import editoriales_bp
from controllers.idiomas_controller import idiomas_bp
from controllers.lectores_controller import lectores_bp
from controllers.prestamos_controller import prestamos_bp
from controllers.usuarios_controller import usuarios_bp
from controllers.dashboard_controller import dashboard_bp
from controllers.perfil_controller import perfil_bp


# ==========================================
# CREAR APLICACIÓN
# ==========================================

app = Flask(__name__)

app.secret_key = "develoteca"

# ==========================================
# VERIFICAR SESIÓN
# ==========================================

def usuario_autenticado():

    return session.get('login') is True



# ==========================================
# CONFIGURAR MYSQL
# ==========================================

configurar_mysql(app)


# ==========================================
# REGISTRAR BLUEPRINTS
# ==========================================

app.register_blueprint(libros_bp)
app.register_blueprint(autores_bp)
app.register_blueprint(categorias_bp)
app.register_blueprint(editoriales_bp)
app.register_blueprint(idiomas_bp)
app.register_blueprint(lectores_bp)
app.register_blueprint(prestamos_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(perfil_bp)





# ==========================================
# PROTEGER PANEL ADMINISTRATIVO
# ==========================================

@app.before_request
def proteger_admin():

    # Solo protegemos rutas que comiencen por /admin
    if request.path.startswith('/admin'):

        # Estas rutas NO requieren sesión
        rutas_publicas = [
            '/admin/',
            '/admin/login'
        ]

        # Si no es login y no existe sesión
        if request.path not in rutas_publicas:

            if not session.get('login'):
                return redirect('/admin/')

            

# ==========================================
# PÁGINA PRINCIPAL
# ==========================================

@app.route('/')
def inicio():

    return render_template('sitio/index.html')


# ==========================================
# CATÁLOGO
# ==========================================

@app.route('/libros')
def libros():

    return render_template('sitio/catalogo.html')


# ==========================================
# NOSOTROS
# ==========================================

@app.route('/nosotros')
def nosotros():

    return render_template('sitio/nosotros.html')


# ==========================================
# CONTACTO
# ==========================================

@app.route('/contactos')
def contactos():

    return render_template('sitio/contacto.html')


# ==========================================
# LOGIN - MOSTRAR FORMULARIO
# ==========================================

@app.route('/admin/')
def admin_index():

    return render_template('admin/auth/login.html')


# ==========================================
# LOGIN - PROCESAR FORMULARIO
# ==========================================

@app.route('/admin/login', methods=['POST'])
def admin_login():

    usuario = request.form['txtUsuario']
    contrasena = request.form['txtPassword']

    # Buscar usuario en la base de datos
    usuario_db = obtener_usuario_login(usuario)

    # ------------------------------------------
    # USUARIO NO EXISTE
    # ------------------------------------------

    if usuario_db is None:

        flash(
            'Usuario o contraseña incorrectos.',
            'danger'
        )

        return redirect('/admin/')


    # ------------------------------------------
    # COMPROBAR ESTADO
    # ------------------------------------------

    if usuario_db[6] != 1:

        flash(
            'El usuario se encuentra inactivo.',
            'warning'
        )

        return redirect('/admin/')


    # ------------------------------------------
    # COMPROBAR CONTRASEÑA
    # ------------------------------------------

    if not check_password_hash(
        usuario_db[4],
        contrasena
    ):

        flash(
            'Usuario o contraseña incorrectos.',
            'danger'
        )

        return redirect('/admin/')


    # ==========================================
    # CREAR SESIÓN
    # ==========================================

    session['login'] = True

    session['id_usuario'] = usuario_db[0]

    session['id_rol'] = usuario_db[1]

    session['usuario'] = usuario_db[2]

    session['nombre_completo'] = usuario_db[3]

    session['correo'] = usuario_db[5]


    # ==========================================
    # REDIRIGIR AL DASHBOARD
    # ==========================================

    return redirect('/admin/dashboard')


# ==========================================
# CERRAR SESIÓN
# ==========================================

@app.route('/admin/logout')
def admin_logout():

    session.clear()

    return redirect('/admin/')




# ==========================================
# EJECUTAR APLICACIÓN
# ==========================================

if __name__ == '__main__':

    app.run(debug=True)