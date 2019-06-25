from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField,ValidationError
from wtforms.validators import DataRequired,length,Email,EqualTo
from .models import User

class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),length(min=2,max=200)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField("Sign up website")

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That usernmae aleardy use, enter oder username please')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email aleardy use, enter oder username please')



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember= BooleanField("remember for me")
    submit = SubmitField("Sign up website")