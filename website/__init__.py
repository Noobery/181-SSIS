from flask import Flask
from flask_mysql_connector import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Baptist69!'
app.config['MYSQL_DATABASE'] = 'SSIS'

mysql = MySQL(app)

# Import and register blueprints here
from website.routes.collegeRoute import collegeRoute
app.register_blueprint(collegeRoute)

from website.routes.courseRoute import courseRoute
app.register_blueprint(courseRoute)
