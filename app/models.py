from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView

# Load a user into our session 
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# Creating the User table in the database
class User(UserMixin, db.Model):

    # Initializing basic user info  
    id            = db.Column(db.Integer, primary_key = True)
    username      = db.Column(db.String(64),  index = True, unique = True)
    email         = db.Column(db.String(128), index = True, unique = True)
    password_hash = db.Column(db.String(128))

    question=db.relationship('Question', backref='admin',lazy='dynamic')
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    # Printing out which user is current
    def __repr__(self):
        return '<User {}>'.format(self.username)

    # Create a password hash 
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Get the original password back 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Useradmin(ModelView):
    form_columns = ['id','username','email']

# Create the Post table in the database 
class Post(db.Model):

    # Initializing basic post info 
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)

    # Printing out which post is current 
    def __repr__(self):
        return '<Post {}>'.format(self.body)


#Creating question to be asked in data base
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    admin_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Printing out which post is current 
    def __repr__(self):
        return '<Question {}>'.format(self.body)

class QuestionAdmin(ModelView):
    form_columns = ['question', 'answer', 'id']