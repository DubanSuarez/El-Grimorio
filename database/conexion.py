from flaskext.mysql import MySQL

mysql=MySQL()

def configurar_mysql(app):
    app.config['MYSQL_DATABASE_HOST']='localhost'
    app.config['MYSQL_DATABASE_USER']='root'
    app.config['MYSQL_DATABASE_PASSWORD']=''
    app.config['MYSQL_DATABASE_DB']='sitio'

    mysql.init_app(app)

