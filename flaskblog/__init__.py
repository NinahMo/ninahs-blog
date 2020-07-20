from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = '6fc3f5630eabfc72446c3246558089f7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app )
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flaskblog import routes
