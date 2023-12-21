from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email

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