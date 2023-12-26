from flask import render_template, redirect, flash
from flask_login import current_user
from app.usuarios import usuarios
import app
import os
from .forms import NewUserForm, EditUserForm

@usuarios.route('/create', methods=['GET', 'POST'])
def creat():
    p = app.models.Usuarios()
    form = NewUserForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        if current_user.is_authenticated:
            flash("Usuario registrado correctamente")
            return redirect('/usuarios/listar')
        else:
            flash("Usuario registrado correctamente")
            return redirect('/')
    return render_template('new_usuarios.html', 
                            form = form)

@usuarios.route('/listar')
def listar():
    usuarios = app.models.Usuarios.query.all()
    return render_template("list_usuarios.html",
                            usuarios = usuarios)

@usuarios.route('/update/<usuario_id>', methods=['GET', 'POST'])
def edit(usuario_id):
    p = app.models.Usuarios.query.get(usuario_id)
    form = EditUserForm(obj=p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash("Usuario actualizado")
        return redirect('/usuarios/listar')
    return render_template('new_usuarios.html', form=form)

@usuarios.route('/delete/<usuario_id>')
def delete(usuario_id):
    p=app.models.Usuarios.query.get(usuario_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash("Usuario eliminado")
    return redirect('/usuarios/listar')