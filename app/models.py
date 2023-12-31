from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

# Tabla de Usuarios

class Usuarios(db.Model, UserMixin):
    __tablename__= "usuarios"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(50), unique = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(15))
    password = db.Column(db.String(120))
    rol = db.Column(db.Integer, db.ForeignKey('rol.id'))
    
    def setPassword(self,password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

@login.user_loader
def load_user(id):
    return Usuarios.query.get(id)

# Tabla de Mangas

class Mangas(db.Model):
    __tablename__= "mangas"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    image_path = db.Column(db.String(100))
    rental_date = db.Column(db.DateTime, default = datetime.utcnow)
    status = db.Column(db.String(20), default= 'Disponible')
    price = db.Column(db.Numeric(precision = 10, scale = 2))
    author = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    category = db.Column(db.Integer, db.ForeignKey('categorias.id'))
    
# Tabla de Préstamos
class Prestamos(db.Model):
    __tablename__= "prestamos"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    manga_id = db.Column(db.Integer, db.ForeignKey('mangas.id'))
    loan_date = db.Column(db.DateTime, default = datetime.utcnow)
    return_date = db.Column(db.DateTime, default = datetime.utcnow() + timedelta(days=15))
    
# Tabla de Rol
class Rol(db.Model):
    __tablename__= "rol"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50))
    
#Tabla de Categorías
class Categorías(db.Model):
    __tablename__= "categorias"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50))