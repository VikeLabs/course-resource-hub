from flask import Flask, render_template
from flask import Blueprint

homepage = Blueprint('homepage', __name__, template_folder='templates')

@homepage.route("/widget")

def widget():
    return  render_template("Following_widget.html")