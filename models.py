
#---------+
# Imports |
#-----------------------------------------------------------------------------------------
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy 
from werkzeug import generate_password_hash, check_password_hash



#-------------------------------------------------+
# Instantiate an instance of the class SQLAlchemy |
#-----------------------------------------------------------------------------------------
db = SQLAlchemy()



#----------------------------------------------+
# Define a class for our database 'user' table |
#-----------------------------------------------------------------------------------------
class User(db.Model):

    # Global class variables
    __tablename__ = 'users'
    uid           = db.Column(db.Integer, primary_key = True)
    firstname     = db.Column(db.String(100))
    lastname      = db.Column(db.String(100))
    email         = db.Column(db.String(120), unique=True)
    pwdhash       = db.Column(db.String(54))


    # Initializer
    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname.title()
        self.lastname  = lastname.title()
        self.email     = email.lower()
        self.set_password(password)

     
    # Utility function
    def set_password(self, password):
        self.pwdhash   = generate_password_hash(password, method='pbkdf2:sha256')


    # Utility function
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)
