
#---------+
# Imports |
#-----------------------------------------------------------------------------------------
from flask_wtf          import Form 
from wtforms            import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length



#------------+
# SignupForm |
#-----------------------------------------------------------------------------------------
class SignupForm(Form):
    first_name = StringField('First name',
        validators=[
            DataRequired("Please enter your first name.")])
    last_name  = StringField('Last name',
        validators=[
            DataRequired("Please enter your last name.")])
    email      = StringField('Email',
        validators=[
            DataRequired("Please enter your email address."),
            Email("This doesn't look like a valid email address.")])
    password   = PasswordField('Password',
        validators=[
            DataRequired("Please enter a password."),
            Length(min=6, message="Passwords must be 6 characters or more.")])
    #----------------------
    submit = SubmitField('Sign up')



#------------+
# LoginForm |
#-----------------------------------------------------------------------------------------
class LoginForm(Form):
    email = StringField('Email',
        validators=[
            DataRequired("Please enter your email address."),
            Email("This doesn't look like a valid email address.")])
    password   = PasswordField('Password',
        validators=[
            DataRequired("Please enter a password."),
            Length(min=6, message="Passwords must be 6 characters or more.")])
    #----------------------
    submit = SubmitField('Log In')
