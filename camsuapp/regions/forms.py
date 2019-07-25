from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,SubmitField,PasswordField,BooleanField,ValidationError,IntegerField,DateField
from wtforms.validators import DataRequired,length,Email,EqualTo
from camsuapp.models import User

class RegionForm(FlaskForm):
    namebranche = StringField('Nom Branche',validators=[DataRequired(),length(min=2,max=200)])
    villebranche = StringField('Ville',validators=[DataRequired(),length(min=2,max=200)])
    siegebranche = StringField('Site',validators=[DataRequired(),length(min=2,max=200)])
    amirbranche = StringField('President',validators=[DataRequired(),length(min=2,max=200)])
    sousbranche = IntegerField('Sous branche', validators=[DataRequired(),length(min=2,max=200)])
    datebranche = DateField('date adhesion', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField("Enregistrer")


 
