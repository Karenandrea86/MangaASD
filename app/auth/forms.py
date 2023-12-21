from flask_wtf import  FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email

class LoginForm(FlaskForm):
    username =StringField(label='Nombre de usuario',
                        validators=[InputRequired(
                        message="Nombre de usuario requerido"
                        )])
    password =PasswordField(label='Contraseña')
    
    style={'class': 'btn-light', 'style': 'background-color: white; margin-top: 5ren;'}
    
    submit =SubmitField(label='Iniciar Sesion',
                        validators=[InputRequired(
                        message="Contraseña requerida"
                        )],
                        render_kw=style
                        )

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
    password = PasswordField("Ingrese su contraseña",
                            validators=[InputRequired(
                                message="password"
                        ),
                                        ])


class NewUserForm(FlaskForm, UserForm):
    submit = SubmitField("Guardar")

class EditUserForm(FlaskForm, UserForm):
    submit = SubmitField("Actualizar")