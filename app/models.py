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
    feedback      = db.relationship('feedback', backref='User', lazy='dynamic')
    outcome       = db.relationship('Result', backref='User_out', lazy='dynamic')
    posts         = db.relationship('Post', backref = 'author', lazy = 'dynamic')
    ques          = db.relationship('answers', backref='answer_user', lazy='dynamic')


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

# class question_level(db.Model):
#      id = db.Column(db.Integer, primary_key=True)
#      #user = db.Column(db.Integer, db.ForeignKey('User.id'))
#      level=db.Column(db.Text)
#      #question = db.Column(db.Text)
#      #question_type=db.relationship('Question', backref='question_level',lazy='dynamic')
          
#      def __repr__(self):
#         return '< %r>' % (self.level)

# class question_levelAdmin(ModelView):
#     form_columns = ['id','level']

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id =db.Column(db.Integer, db.ForeignKey('user.id'))
    result = db.Column(db.Integer, index=True)

    def __repr__(self):
        return 'Total {}: '.format(self.User.username)

#Creating question to be asked in data base
class Question(db.Model):

    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    question_marks=db.Column(db.Integer, index = True, default = "10")
    mcq      = db.relationship('MCQ', backref='Question', lazy='dynamic')
    #level    = db.Column(db.Integer, db.ForeignKey('question_level.id'))
    answer   = db.relationship('answers', backref='answers', lazy='dynamic')
    
    

    def __repr__(self):
        return "< Question - id: {} question: {}  {} {}   >".format(
            self.id,
            self.question,
            self.answer,
            self.question_marks
        )

class QuestionAdmin(ModelView):
    form_columns = ['question', 'answer', 'id','question_level']

class feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    Feedback = db.Column(db.String(256), index=True)
    user_id =db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<feedback %r>' % (self.user)

class answers(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    answer        = db.Column(db.String(256), index=True)
    user_id       = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id   = db.Column(db.Integer, db.ForeignKey('questions.id'))
    user_marks    = db.Column(db.Integer, index = True)


class MCQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    options_content = db.Column(db.Text, index=True)
    correct = db.Column(db.Boolean, default = False, nullable=False)
    question_id =db.Column(db.Integer, db.ForeignKey('questions.id'))

    def __repr__(self):
        return 'MCQ {}: '.format(self.options_content)