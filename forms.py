from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationFormP(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    patient_id = StringField('Patient Id', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class RegistrationFormD(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    doctor_id = StringField('Doctor Id', validators=[DataRequired(), Length(min=2, max=20)])
    hospital_name = StringField('Hospital Name', validators=[DataRequired(), Length(min=2, max=120)])
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class RegistrationFormI(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    insurance_id = StringField('Insurance Id', validators=[DataRequired(), Length(min=2, max=20)])
    company_name = StringField('Company Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')
    option = StringField('Select Your Option', validators=[DataRequired(), Length(min=2, max=20)])


class PatientId(FlaskForm):
    patient_id = IntegerField('Patient ID', validators=[DataRequired()])
    submit = SubmitField('Enter')