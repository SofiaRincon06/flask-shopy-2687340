#Dependencia de flask
from flask import Flask, render_template
#Dependencia de los modelos
from flask_sqlalchemy import SQLAlchemy
#Dependencia de la migracion
from flask_migrate import Migrate
#Dependencia para fechar y hora
from datetime import datetime
#Dependencias de wtforms
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField 

#crear el objeto flask
app = Flask(__name__)

#La 'cadena de conexion'(connectionstring)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:@localhost:3307/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']= False
app.config['SECRET_KEY']='Mochuelo'

#Crear el objeto de modelos
db = SQLAlchemy(app)
#Crear el objeto de la migracion
migrate = Migrate(app,db)

#Crear Formulario de registro de prodcutos 

class ProductosFrom(FlaskForm):
    nombre= StringField('Ingrese el nombre del producto')
    precio= StringField('Ingrese el precio del producto')
    submit = SubmitField('Registrar Producto')
    

#crear los modelos cliente
class Cliente(db.Model):
    #definir los atributos
    __tablename__="clientes"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120),
                         nullable=True)
    pasword = db.Column(db.String(128),
                        nullable=True)
    email= db.Column(db.String(100),
                        nullable=True)
    
    #Relaciones en Sql alchemy
    ventas= db.relationship('Venta', backref='Cliente',lazy='dynamic')
   
#crear los modelos producto
class Producto(db.Model):
    #definir los atributos
    __tablename__="productos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120))
    precio = db.Column(db.Numeric(precision = 10, scale =2))
    imagen = db.Column(db.String(200))

class Venta(db.Model):
    __tablename__="ventas"
    id=db.Column(db.Integer, primary_key=True)
    fecha=db.Column(db.DateTime, 
                    default= datetime.utcnow )
#clave FORANEA:
    cliente_id= db.Column(db.Integer,
                            db.ForeignKey('clientes.id'))


class Detalles(db.Model):
    __name__="detalles"
    id=db.Column(db.Integer,primary_key=True)
    producto_id=db.Column(db.Integer,
                            db.ForeignKey('productos.id'))
    venta_id=db.Column(db.Integer,
                            db.ForeignKey('ventas.id'))
    cantidad=db.Column(db.Numeric(precision = 10, scale =2))
    
    
    #Rutas:
    @app.route('/productos', methods= ['GET', 'POST'])
    def nuevo_producto():
        form = ProductosFrom()
        if form.validate_on_submit():
            p= Producto(nombre = form.nombre.data, precio= form.precio.data)
            db.session.add(p)
            db.session.commit()
            return "Producto Registrado"
        return render_template('nuevo_producto.html', form = form)