from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed 
#formulario de registro 
#de nuevo producto
class NewProductForm(FlaskForm):
    nombre = StringField(validators=[InputRequired(message="Falta Nombre :(")],
                    label="Ingrese nombre: ")
    precio = IntegerField(label= "Ingrese precio: ",
                          validators =[InputRequired(message="Falta precio mochuelo"),
                                       NumberRange(message="Precio fuera de rango",
                                                   min=1000,
                                                   max=10000)])
    imagen= FileField("carge imagen del producto",
                      validators=[
                          FileRequired(message="Suba una imagen porfa <3"),
                      FileAllowed(
                                ["jpg", "png"],
                                  message="Tipo de archivo incorrecto")])
    submit = SubmitField("Registrar")