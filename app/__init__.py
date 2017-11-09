from flask import Flask

app = Flask(__name__)
Bootstrap(app)

from app import views
