from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email

"""
    class Usuarios(db.Model):
    __tablename__= "usuarios"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(50), unique = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    """


class UserForm():
    username = StringField("Ingrese su usuario",
                            validators=[InputRequired(
                                message="username"
                            )])
    first_name= StringField("Ingrese su nombre",
                            validators=[InputRequired(
                                message="first_name"
                            )])
    last_name= StringField("Ingrese su apellido",
                            validators=[InputRequired(
                                message="last_name"
                        ),
                            ])
    email = StringField("Ingrese su correo",
                            validators=[InputRequired(
                                message="email"
                            )])
    phone = StringField("Ingrese su celular",
                            validators=[InputRequired(
                                message="phone"
                        ),
                                        ])
    
class NewUserForm(FlaskForm, UserForm):
    submit = SubmitField("Guardar")

class EditUserForm(FlaskForm, UserForm):
    submit = SubmitField("Actualizar")