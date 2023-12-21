from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField, IntegerField, DateField
from wtforms.validators import InputRequired, NumberRange, DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MangaForm():
    title = StringField(
                        "Ingrese título del manga" ,
                        validators=[
                            InputRequired(message='Título requerido')
                                    ]
                        
                        
                        )
    description = StringField("Ingrese la descripción del manga",
                         validators=[
                             InputRequired(
                                 message="Descripción requerido"
                                 )
                                     ]
                        )

class NewMangaForm(FlaskForm, MangaForm):
    image_path = FileField (label="Ingrese la imagen promocional",
                        validators=[FileRequired(message="Se requiere la imagen promocional"),
                                    FileAllowed(
                                        ["jpg","png"],
                                        message="Solo se aceptan imagenes"

                                    )
                                    ]
                       )
    return_date = DateField(
                        "Ingrese la fecha de devolución" ,
                        validators=[
                            DataRequired(message='Fecha requerida')
                                    ]
                        
                        
                        )
    status = StringField(
                        "Ingrese el estado del manga" ,
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
    submit = SubmitField("Guardar")
    
class EditMangaForm(FlaskForm, MangaForm):
    submit =SubmitField("Actualizar")