from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

bcrypt = Bcrypt()
db = SQLAlchemy()
mailer = Mail()