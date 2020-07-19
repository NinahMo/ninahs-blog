from flask_wtf import FlaskForm

class RegistrationForm(FlaskForm):
    username = StringField('Username')