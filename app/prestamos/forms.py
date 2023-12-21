from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DateField
from wtforms.validators import InputRequired, DataRequired

class LoanForm():
    user_id = StringField("Ingrese id de usuario",
                            validators=[InputRequired(
                                message="ID Requerido"
                            )])
    manga_id = StringField("Ingrese id de manga",
                            validators=[InputRequired(
                                message="ID Requerido"
                            )])
    return_date = DateField("Ingrese fecha de Regreso",
                            validators=[DataRequired(
                                message="Fecha Requerida"
                        ),
                            ])
    
class NewLoanForm(FlaskForm, LoanForm):
    submit = SubmitField("Guardar")

class EditLoanForm(FlaskForm, LoanForm):
    submit = SubmitField("Actualizar")