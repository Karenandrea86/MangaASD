from flask import render_template, redirect, flash
from flask_login import current_user
from app.prestamos import prestamos
import app
from .forms import NewLoanForm, EditLoanForm

@prestamos.route('/create', methods=['GET', 'POST'])
def crear():
    p = app.models.Prestamos()
    form = NewLoanForm()
    prestamos = app.models.Prestamos.query.all()
    mangas = app.models.Mangas.query.filter_by(status="Disponible")
    form.manga_id.choices = [(manga.id, str(manga.title)) for manga in mangas]
    usuario = current_user
    usuarios = app.models.Usuarios.query.filter_by(username=usuario.username).all()
    form.user_id.choices = [(usuario.id, usuario.username) for usuario in usuarios]
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        flash("Préstamo por 15 días registrado correctamente")
        return redirect('/prestamos/listar')
    return render_template('new_prestamos.html', 
                            form = form, prestamos = prestamos)

@prestamos.route('/listar')
def listar():
    if current_user.is_authenticated and current_user.rol == 2:
        prestamos = app.models.Prestamos.query.all()
    else:
        prestamos = app.models.Prestamos.query.filter_by(user_id=current_user.id).all()
    return render_template("list_prestamos.html",
                            prestamos = prestamos)

@prestamos.route('/update/<prestamo_id>', methods=['GET', 'POST'])
def edit(prestamo_id):
    p = app.models.Prestamos.query.get(prestamo_id)
    form = EditLoanForm(obj=p)
    mangas = app.models.Mangas.query.filter_by(status="Disponible")
    print(mangas)
    form.manga_id.choices = [(manga.id, str(manga.title)) for manga in mangas]
    """usuarios = app.models.Usuarios.query.all()
    print(usuarios)
    form.user_id.choices = [(usuario.id, str(usuario.username)) for usuario in usuarios]"""
    usuario = current_user
    usuarios = app.models.Usuarios.query.filter_by(username=usuario.username).all()
    form.user_id.choices = [(usuario.id, usuario.username) for usuario in usuarios]
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash("Préstamo actualizado")
        return redirect('/prestamos/listar')
    return render_template('new_prestamos.html', form=form)

@prestamos.route('/delete/<prestamo_id>')
def delete(prestamo_id):
    p=app.models.Prestamos.query.get(prestamo_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash("Préstamo eliminado")
    return redirect('/prestamos/listar')