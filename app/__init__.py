import logging
import sys
from extensions import bcrypt, db, mailer
from flask import Flask, redirect, render_template, request
from app.mod_auth import mod_auth

app = Flask(__name__)
# from app.mod_auth import mod_auth
app.register_blueprint(mod_auth.login_page)

# Configurations
app.config.from_object('config')

def init_extensions():
    """initialize extensions to be used throughout the project"""
    bcrypt.init_app(app)
    db.init_app(app)
    mailer.init_app(app)

def configure_logger(app):
    """configure the default logging stream"""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)

@app.route('/')
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

init_extensions()