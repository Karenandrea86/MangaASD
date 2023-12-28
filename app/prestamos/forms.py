from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DateField, SelectField
from wtforms.validators import InputRequired, DataRequired

class LoanForm():
    
    user_id = SelectField("Usuario")
    manga_id = SelectField("Manga",
                            validators=[InputRequired(
                                message="ID Requerido"
                            )])
    
class NewLoanForm(FlaskForm, LoanForm):
    submit = SubmitField("Alquilar")

class EditLoanForm(FlaskForm, LoanForm):
    submit = SubmitField("Actualizar")