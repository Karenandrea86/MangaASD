from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MangaForm():
    nombre = StringField(
                        "Ingrese nombre del producto" ,
                        validators=[
                            InputRequired(message='nombre requerido')
                                    ]
                        
                        
                        )
    precio =IntegerField("Ingrese el precio del producto",
                         validators=[
                             InputRequired(
                                 message="Precio requerido"
                                 ),
                             NumberRange(
                                 message="Precio fuera de rango",
                                 min =10000,
                                 max =100000
                                        )
                                     ]
                        )

class NewMangaForm(FlaskForm, MangaForm):
    imagen = FileField (label="Imagen del pproducto ",
                        validators=[FileRequired(message="Se requiere la imagen"),
                                    FileAllowed(
                                        ["jpg","png"],
                                        message="solo se aceptan imagenes"

                                    )
                                    ]
                       )
    submit =SubmitField("Guardar")
    
class EditMangaForm(FlaskForm, MangaForm):
    submit =SubmitField("Actualizar")