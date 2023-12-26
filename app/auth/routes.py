from flask_login import login_user, current_user, logout_user
from flask import render_template, redirect, flash, request
from flask_login import login_required
from app.auth import auth
from .forms import LoginForm
import app

@auth.route('/login',
            methods=["GET",'POST'])
def login():
    form = LoginForm()
    try:
        if form.validate_on_submit():
            #selecciona al Usuarios por username
            c =app.models.Usuarios.query.filter_by(username=form.username.data).first()
            if c is None or not c.check_password(form.password.data):
                login_user(c, remember=True)
                flash('Bienvenido al sistema')
                return redirect('/')
    except:
            flash('Usuario o contraseña incorrectos. Intentalo de nuevo.')
    
    return render_template('login.html', form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada con exito')
    return redirect('/')