
from extensions import bcrypt
from flask import Blueprint, render_template, request, redirect
from app.mod_auth.user import User

login_page = Blueprint('login', __name__,
                        template_folder='templates')

@login_page.route("/login")
def login():
    return render_template('/auth/signin.html')

@login_page.route('/login', methods=['POST'])
def login_post():
    """attempt to login. if it fails, refresh page so user can try again"""
    username = request.form['username']
    pass_hash = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
    try:
        User.query.filter(User.username == username).exists()

        return redirect("/")
    except Exception as e:

        return login_page.validate()

@login_page.route('/signup')
def signup():
    return render_template('/auth/signup.html')

@login_page.route('/signup', methods=['POST'])
def signup_post():
    """attempt to sign up. if info provided is incorrect, refresh page so user can try again"""

    username = request.form['username']
    email = request.form['email']
    pass_hash = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
    User(username, email, pass_hash) # check if username and email are unique? maybe it throws an error 
    return render_template('/auth/signup.html')

@login_page.route('/forgot_password')
def forgot_password():
    return render_template('/auth/forgot_password.html')
