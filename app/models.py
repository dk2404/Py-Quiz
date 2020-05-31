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
    #Answers       = db.Column(db.String(256))
    #level_id      = db.Column(db.Integer, db.ForeignKey('question_level.id'))

    #question=db.relationship('Question', backref='admin',lazy='dynamic')
    #level=db.relationship('question_level', foreign_keys=[level_id])
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

class question_level(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     #user = db.Column(db.Integer, db.ForeignKey('User.id'))
     level=db.Column(db.Text)
     #question = db.Column(db.Text)
     question_type=db.relationship('Question', backref='question_level',lazy='dynamic')
          
     def __repr__(self):
        return '< %r>' % (self.level)

class question_levelAdmin(ModelView):
    form_columns = ['id','level']

#Creating question to be asked in data base
class Question(db.Model):

    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    #answer = db.Column(db.Text)
    level   = db.Column(db.Integer, db.ForeignKey('question_level.id'))
    choice1 = db.Column(db.String(128), unique=False, nullable=False)
    choice2 = db.Column(db.String(128), unique=False, nullable=False)
    choice3 = db.Column(db.String(128), unique=False, nullable=False)
    choice4 = db.Column(db.String(128), unique=False, nullable=False)
    correct = db.Column(db.Integer, unique=False, nullable=False)
    #admin_id = db.Column(db.Integer, db.ForeignKey('question_level.id'))

    # Printing out which post is current 
    # def __repr__(self):
    #     return '<Question %r>' % (self.id)

    def __repr__(self):
        return "< Question - id: {} question: {}  {} {} {} {} {} {} >".format(
            self.id,
            self.question,
            self.choice1,
            self.choice2,
            self.choice3,
            self.choice4,
            self.correct
        )

class QuestionAdmin(ModelView):
    form_columns = ['question', 'answer', 'id','question_level']

# class QuizForm(ModelView):
#   q1 = RadioField(validators=[InputRequired()])
#   q2 = RadioField(validators=[InputRequired()])
#   q3 = RadioField(validators=[InputRequired()])
#   q4 = RadioField(validators=[InputRequired()])

#   cancel = SubmitField("Cancel")

# form = QuizForm(request.form)
# form.q1.choices = [
#     ("1", questions[0].choice1),
#     ("2", questions[0].choice2),
#     ("3", questions[0].choice3),
#     ("4", questions[0].choice4)
#   ]
# form.q2.choices = [
#     ("1", questions[1].choice1),
#     ("2", questions[1].choice2),
#     ("3", questions[1].choice3),
#     ("4", questions[1].choice4)
#   ]
  

  