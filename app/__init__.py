from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from app.homepage import following_section

app = Flask(__name__)
app.register_blueprint(following_section.homepage)

# Configurations
app.config.from_object('config')

@app.route('/')
def index():
    return render_template("index.html")

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
