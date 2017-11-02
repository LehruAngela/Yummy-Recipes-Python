from flask import Flask
app = Flask(__name__)

# App configs
app.config['SESSION_TYPE'] = "filesystem"

# Load the views
from app import views

# load the config file
app.config.from_object('config')









