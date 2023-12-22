from app.auth import auth
import app
from flask import render_template, redirect, flash
from flask_login import login_user, logout_user
import wtforms
from .forms import *


@auth.route('/login',
            methods=["GET",'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #selecciona al Usuarios por username
        c =app.models.Usuarios.query.filter_by(username=form.username.data).first()
        if c is None or not c.check_password(form.password.data):
            print('usuario no existe')
            redirect('/auth/login')
            #mensaje flask de usuario no existente
        else:
            flash('Bienvenido al sistema')
            login_user(c, remember=True)
            return redirect('/usuarios/listar')
    return render_template('login.html', form = form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/auth/login')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    p = app.models.Usuarios()
    form = NewUserForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        flash("Usuario registrado correctamente")
        return redirect('/')
    return render_template('register.html', form=form, wtf=wtforms)