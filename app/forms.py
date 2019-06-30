from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,SubmitField,PasswordField,BooleanField,ValidationError,TextAreaField
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

class UpdateAccount(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),length(min=2,max=200)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    picture = FileField('Picture Profil',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField("Update Account")
    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That usernmae aleardy use, enter oder username please')
    
    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email aleardy use, enter oder username please')
#class pour la creation d'un post
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(),length(min=5,max=200)])
    content = TextAreaField('Content News',validators=[DataRequired()])
    submit = SubmitField('Add News Post')