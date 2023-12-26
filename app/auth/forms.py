from flask_wtf import  FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username =StringField(label='Nombre de usuario',
                        validators=[InputRequired(
                        message="Nombre de usuario requerido"
                        )])
    password =PasswordField(label='Contraseña',
                            validators=[InputRequired(
                                message="Contraseña requerida"
                                )]
                            )
    
    style={'class': 'btn-light', 'style': 'background-color: white; margin-top: 5ren;'}
    
    submit =SubmitField(label='Iniciar Sesion',
                        validators=[InputRequired(
                        message="Contraseña requerida"
                        )],
                        render_kw=style
                        )