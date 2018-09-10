from flask import Flask # import the class Flask from the module flask

# creating an app variable to be used throughout Flask application
app = Flask(__name__) # __name__ is the project folder name "basic_folder"

# ROUTES HAVE TO BE IMPORTED AFTER APP VARIABLE CREATED, OTHERWISE WILL BREAK
from app import routes
