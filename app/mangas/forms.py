from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField, IntegerField, DateField, SelectField
from wtforms.validators import InputRequired, NumberRange, DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MangaForm():
    title = StringField(
        "Ingrese título del manga",
        validators=[
            InputRequired(message='Título requerido')
        ]
    )
    description = StringField(
        "Ingrese la descripción del manga",
        validators=[
            InputRequired(message="Descripción requerido")
        ]
    )
    image_path = FileField (label="Ingrese la imagen promocional",
                            validators=[
                                FileRequired(message="Se requiere la imagen promocional"),
                                FileAllowed(
                                    ["jpg","png","jpeg"],
                                    message="Solo se aceptan imagenes"
                                    )
                                ]
                            )
    status = SelectField(
        "Estado del manga",
        choices = [
            "Disponible"
        ],
        validators=[
            InputRequired(message='Estado requerido')
        ]                     
    )
    price = IntegerField(
        "Ingrese el precio del manga" ,
        validators=[
            InputRequired(message='Precio requerido')
        ]
    )
    author = StringField(
        "Ingrese el autor del manga" ,
        validators=[
            InputRequired(message='Autor requerido')
        ]
    )
    quantity = IntegerField(
        "Ingrese la cantidad" ,
        validators=[
            InputRequired(message='Cantidad requerida')
        ]
    )
    category = SelectField(
        "Ingrese la categoría del manga" ,
        validators=[
            InputRequired(message='Categoría requerida')
        ]
    )

class NewMangaForm(FlaskForm, MangaForm):
    submit = SubmitField("Guardar")
    
class EditMangaForm(FlaskForm, MangaForm):
    submit =SubmitField("Actualizar")