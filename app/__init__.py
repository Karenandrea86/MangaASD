from flask import Flask, render_template, flash, redirect
from flask_login import LoginManager, current_user
from .config  import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .mi_blueprint import  mi_blueprint
from app.mangas import mangas
from app.prestamos import prestamos
from app.usuarios import usuarios
from app.auth import auth
from flask_bootstrap import Bootstrap
from app.prestamos.forms import NewLoanForm, EditLoanForm

app = Flask(__name__)
app.config .from_object(Config)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = "/auth/login"

db = SQLAlchemy(app)
migrate = Migrate(app , db )

app.register_blueprint(mi_blueprint)
app.register_blueprint(mangas)
app.register_blueprint(prestamos)
app.register_blueprint(usuarios)
app.register_blueprint(auth)



from .models import Usuarios, Mangas, Prestamos

@app.route('/')
def prueba ():
    if current_user.is_authenticated:
        form = NewLoanForm()
        mangas = models.Mangas.query.filter_by(status="Disponible")
        print(mangas)
        form.manga_id.choices = [(manga.id, str(manga.title)) for manga in mangas]
        usuario = current_user
        usuarios = models.Usuarios.query.filter_by(username=usuario.username).all()
        form.user_id.choices = [(usuario.id, usuario.username) for usuario in usuarios]
        return render_template("index.html", mangas = mangas, form = form)
    else:
        form = NewLoanForm()
        mangas = models.Mangas.query.filter_by(status="Disponible")
        print(mangas)
        return render_template("index.html", mangas = mangas, form = form)

@app.route("/crear", methods=['GET', 'POST'])
def crear():
    p = models.Prestamos()
    form = NewLoanForm()
    mangas = models.Mangas.query.filter_by(status="Disponible")
    print(mangas)
    form.manga_id.choices = [(manga.id, str(manga.title)) for manga in mangas]
    usuario = current_user
    usuarios = models.Usuarios.query.filter_by(username=usuario.username).all()
    form.user_id.choices = [(usuario.id, usuario.username) for usuario in usuarios]
    if form.validate_on_submit():
        form.populate_obj(p)
        db.session.add(p)
        db.session.commit()
        flash("Préstamo por 15 días registrado correctamente")
        mangas = models.Mangas.query.all()
        return redirect('/')