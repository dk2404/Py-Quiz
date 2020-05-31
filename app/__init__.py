from flask import Flask
#from config import TestConfig
from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager 
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

admin = Admin(app,name='Control Panel')
login = LoginManager(app)
login.login_view = 'login'

#admin.add_view(ModelView())

from app import routes, models