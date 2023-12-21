from flask import Flask, render_template
from flask_login import LoginManager
from .config  import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .mi_blueprint import  mi_blueprint
from app.mangas import mangas
from app.usuarios import usuarios
from app.auth import auth
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config .from_object(Config)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = "/auth/login"

db = SQLAlchemy(app)
migrate = Migrate(app , db )

app.register_blueprint(mi_blueprint)
app.register_blueprint(mangas)
app.register_blueprint(usuarios)
app.register_blueprint(auth)



from .models import Usuarios, Mangas, Prestamos

@app.route('/')
def prueba ():
    return render_template("index.html")