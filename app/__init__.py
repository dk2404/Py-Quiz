from flask import Flask
#from config import TestConfig
from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager 
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView



app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(Config)

migrate = Migrate(app, db)

admin = Admin(app,name='Dash Board')
login = LoginManager(app)
login.login_view = 'login'

from app.models import User, Post
admin.add_view(ModelView(User,db.session))

from app import routes, models