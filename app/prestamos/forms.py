from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DateField, SelectField
from wtforms.validators import InputRequired, DataRequired

class LoanForm():
    
    user_id = SelectField("Ingrese usuario",
                          choices= [],
                            validators=[InputRequired(
                                message="ID Requerido"
                            )])
    manga_id = SelectField("Ingrese manga",
                           choices= [],
                            validators=[InputRequired(
                                message="ID Requerido"
                            )])
    return_date = DateField("Ingrese fecha de regreso",
                            validators=[DataRequired(
                                message="Fecha Requerida"
                        ),
                            ])
    
class NewLoanForm(FlaskForm, LoanForm):
    submit = SubmitField("Guardar")

class EditLoanForm(FlaskForm, LoanForm):
    submit = SubmitField("Actualizar")