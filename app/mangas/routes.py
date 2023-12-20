from flask import render_template, redirect, flash
from app.mangas import mangas
import app
import os
from .forms import NewMangaForm, EditMangaForm

@mangas.route('/create',
                 methods=['GET','POST'])
def crear():
    p = app.models.Mangas()
    form = NewMangaForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        p.imagen=form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()
        archivo = form.imagen.data
        archivo.save(os.path.abspath(os.getcwd() +"/app/mangas/images/"+p.imagen))
        
        flash("Manga registrado correctamente")
        return redirect('/mangas/listar')
    return render_template('new_mangas.html',
                           form=form )

@mangas.route('/listar')
def listar():
    mangas = app.models.Mangas.query.all()
    return render_template("list_mangas.html" ,
                           mangas = mangas)
    
@mangas.route('/editar/<manga_id>' ,
                 methods = ['GET' , 'POST'])
def editar(manga_id):
    p = app.models.Mangas.query.get(manga_id)
    form = EditMangaForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Manga actualizado')
        return redirect('/mangas/listar')
    return render_template('new_mangas.html' ,
                           form = form)

@mangas.route('/eliminar/<manga_id>')
def eliminar(manga_id):
    p = app.models.Mangas.query.get(manga_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('Manga eliminado')
    return redirect('/mangas/listar')