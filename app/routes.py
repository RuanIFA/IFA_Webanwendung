#Eigenentwicklung
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app
from app import db
from app.forms import LoginForm, RegistrationForm, CarsForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Cars

#Eigenentwicklung
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    car = Cars.query.all()
    return render_template('index.html', car=car)

#Übernommen
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Benutzername oder Passwort ist falsch.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Benutzername oder Passwort ist falsch.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
            return redirect(next_page)

#Eigenentwicklung
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

#Übernommen
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Sie haben sich erfolgreich registriert.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#Eigenentwicklung
@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CarsForm()
    print(form.errors)
    if form.validate_on_submit():
        cars = Cars(model=form.model.data, date=form.date.data, price=form.price.data, status=form.status.data, customer=form.customer.data, notes=form.notes.data)
        db.session.add(cars)
        db.session.commit()
        flash('Der Eintrag wurde erstellt.')
        print(form.errors)
        return redirect(url_for('index'))
    return render_template('create.html', title='Create', form=form)

#Eigenentwicklung
@app.route('/edit/<id>', methods=['GET','POST'])
@login_required
def edit(id):
    cars = Cars.query.get(id)
    form = CarsForm()
    print(form.errors)
    if cars:
        if form.validate_on_submit():
            cars.model = form.model.data
            cars.date = form.date.data
            cars.price = form.price.data
            cars.status = form.status.data
            cars.customer = form.customer.data
            cars.notes = form.notes.data
            db.session.commit()
            flash('Die Änderungen sind gespeichert.')
            print(form.errors)
            return redirect(url_for('index'))
        return render_template('edit.html', title='Edit', form=form, id=id)
    else:
        flash('ID nicht gefunden.')
    return redirect(url_for('index'))

#Eigenentwicklung
@app.route('/delete/<id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    cars = Cars.query.get(id)
    form = CarsForm()
    if cars:
        db.session.delete(cars)
        db.session.commit()
        flash('Der Datensatz wurde entfernt.')
        return redirect(url_for('index'))
    else:
        flash('ID nicht gefunden.')
    return redirect(url_for('index'))

#Eigenentwicklung
@app.route('/us', methods=['GET'])
def us():
    return render_template('us.html', title='Us')
