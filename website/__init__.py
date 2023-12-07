from flask import Flask
from flask_mysql_connector import MySQL
import os
from dotenv import load_dotenv
from config import Config, cloudConfig  # Import Config from the correct location
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary
import cloudinary.api

load_dotenv()

# Create the MySQL instance outside the Flask app
mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Use Config directly, not as a string
    #print(app.config)


    cloudinary.config(
        cloud_name=cloudConfig.CLOUD_NAME,
        api_key=cloudConfig.API_KEY,
        api_secret=cloudConfig.API_SECRET
    )
    # Initialize the MySQL extension
    mysql.init_app(app)
    #print(app.config)
    # Import and register blueprints here
    from website.routes.collegeRoute import collegeRoute
    app.register_blueprint(collegeRoute)

    from website.routes.courseRoute import courseRoute
    app.register_blueprint(courseRoute)

    from website.routes.studentRoute import studentRoute
    app.register_blueprint(studentRoute)

    return app
