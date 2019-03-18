from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class ProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField("Gender", choices=[("None", "Select Gender"), ("Male", "Male"), ("Female", "Female")], validators=[DataRequired()])
    email = StringField("Email", validators = [DataRequired(), Email()])
    location = StringField("Location", validators = [DataRequired()])
    bio = TextAreaField("Biography", validators = [DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], message="That's not a photo")])
    
    submit = SubmitField('Add Profile')
    
    
    

