from flask import render_template, redirect, flash
from app.prestamos import prestamos
import app
import os
from .forms import NewLoanForm, EditLoanForm

@prestamos.route('/create', methods=['GET', 'POST'])
def creat():
    p = app.models.Prestamos()
    form = NewLoanForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        flash("Préstamo registrado correctamente")
        return redirect('/prestamos/listar')
    return render_template('new_prestamos.html', 
                            form = form)

@prestamos.route('/listar')
def listar():
    prestamos = app.models.Prestamos.query.all()
    return render_template("list_prestamos.html",
                            prestamos = prestamos)

@prestamos.route('/update/<prestamo_id>', methods=['GET', 'POST'])
def edit(prestamo_id):
    p = app.models.Prestamos.query.get(prestamo_id)
    form = EditLoanForm(obj=p)
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