import os
from flask import Flask
# https://github.com/pdybka-ep/flask-todoapp
# http://www.vertabelo.com/blog/technical-articles/web-app-development-with-flask-sqlalchemy-bootstrap-part-2
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


from views import *

if __name__ == '__main__':
    app.run()
