#Eigenentwicklung
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

#Übernommen
class LoginForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    remember_me = BooleanField('Eingabe merken')
    submit = SubmitField('Einloggen')

#Übernommen
class RegistrationForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])                
    password = PasswordField('Passwort', validators=[DataRequired()])
    password2 = PasswordField(
            'Passwort neu eingeben', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrieren')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Benutzername ist schon in Gebrauch.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('E-Mail ist schon in Gebrauch.')

#Eigenentwicklung
class CarsForm(FlaskForm):
    id = StringField('ID')
    model = StringField('Auto Marke/Modell', validators=[DataRequired()])
    date = StringField('Reservierungsdatum', validators=[DataRequired()])
    price = StringField('Preis', validators=[DataRequired()])
    status = SelectField('Status', choices=[('bezahlt'), ('nicht bezahlt')])
    customer = StringField('Name', validators=[DataRequired()])
    notes = StringField('Bemerkungen')
    submit = SubmitField('Bestätigen')
    

