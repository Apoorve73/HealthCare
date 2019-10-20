from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationFormP, RegistrationFormD, RegistrationFormI, LoginForm, PatientId

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'Hashir'

db = SQLAlchemy(app)


class medical_history(db.Model):
    patient_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    occupation = db.Column(db.String(120), nullable=True, default='Unoccupied')
    gender = db.Column(db.String(10), nullable=True, default='Not specified')
    address = db.Column(db.String(120), nullable=True, default='Not mentioned')
    date_last_seen = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        return f"medical_history('{self.full_name}', '{self.email}', '{self.image}')"


class Doctor_register(db.Model):
    doctor_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hospital_name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"Doctor_register('{self.doctor_id}', '{self.full_name}')"


class Insurance_register(db.Model):
    insurance_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    company_name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"Insurance_register('{self.email}', '{self.insurance_id}')"


class Patient_register(db.Model):
    patient_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"Patient_register('{self.patient_id}', '{self.full_name}')"


@app.route("/")
@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/registerd", methods=['GET', 'POST'])
def registerd():
    form = RegistrationFormD()
    if form.validate_on_submit():
        flash(f'Account created for Doctor {form.username.data}!', 'success')
        return redirect(url_for('about'))
    return render_template('registerdoctor.html', title='Register-Doctor', form=form)


@app.route("/registerp", methods=['GET', 'POST'])
def registerp():
    form = RegistrationFormP()
    if form.validate_on_submit():
        flash(f'Account created for Patient {form.username.data}!', 'success')
        return redirect(url_for('patientID.html'))
    return render_template('registerpatient.html', title='Register-Patient', form=form)


@app.route("/registeri", methods=['GET', 'POST'])
def registeri():
    form = RegistrationFormI()
    if form.validate_on_submit():
        flash(f'Account created for Insurance Officer {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('registerinsurance.html', title='Register-Insurance', form=form)



@app.route("/accessd", methods=['GET', 'POST'])
def accessd():
    form1 = PatientId()
    if request.method == "GET":

        return render_template('accessd.html', title='Access', form=form1)
    else:
        iop = medical_history.query.filter_by(patient_id = request.form.get('patient_id'))
        return render_template('df.html', iop=iop)


@app.route("/accessi", methods=['GET', 'POST'])
def accessi():
    form1 = PatientId()
    if request.method == "GET":

        return render_template('accessi.html', title='Access', form=form1)
    else:
        iop = medical_history.query.filter_by(patient_id = request.form.get('patient_id'))
        return render_template('inf.html', iop=iop)


@app.route("/accessp", methods=['GET', 'POST'])
def accessp():
    form1 = PatientId()
    if request.method == "GET":

        return render_template('accessp.html', title='Access', form=form1)
    else:
        iop = medical_history.query.filter_by(patient_id = request.form.get('patient_id'))
        return render_template('pf.html', iop=iop)


@app.route("/logina", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'hameedhashirniazi@gmail.com' and form.password.data == "18723654":
            flash('You have been logged in successfully', 'success')
            return redirect(url_for('about'))
        else:
            flash('Incorrect username or password', 'danger')
    return render_template('logina.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)