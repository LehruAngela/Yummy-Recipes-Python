from flask import Flask
app = Flask(__name__)

app.config['SESSION_TYPE'] = "filesystem"

# Load the views
from app import views











