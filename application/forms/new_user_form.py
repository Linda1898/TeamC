from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField


class SignUpForm (FlaskForm):
    user_name = StringField('Username')
    user_password = PasswordField('Password')
    user_age = IntegerField ('Age')
    submit = SubmitField ('Sign up')