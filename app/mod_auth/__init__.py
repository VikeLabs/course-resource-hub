
from flask import redirect, render_template, request
import app

@app.route("/login")
def login():
    return render_template('/auth/signin.html')


@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    app.logger.info("username: " + username + " password: " + password)
    return redirect("/")
