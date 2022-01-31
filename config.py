import os


class Config(object):
    DEBUG = True

    SECRET_KEY = os.environ.get('SECRET_KEY') or "this_is_a_secret(shh)"

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    THREADS_PER_PAGE = 2
    
    CSRF_ENABLED     = True
    CSRF_SESSION_KEY = "secret"

    SQLALCHEMY_DATABASE_URI = 'mysql://root:pass@localhost/course_resource_hub'
