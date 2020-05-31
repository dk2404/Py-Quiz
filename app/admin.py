from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'admin.db')
app.config['SECRET_KEY'] = 'mysecret'

db = SQLAlchemy(app)

print('running from admin')

admin = Admin(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

admin.add_view(ModelView(Person, db.session))

if __name__ == '__main__':
    app.run(debug=True)