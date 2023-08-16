#Dependencia de flask
from flask import Flask
#dependencia de configuracion 
from .config import Config
#Dependencia de los modelos
from flask_sqlalchemy import SQLAlchemy
#Dependencia de la migracion
from flask_migrate import Migrate
from .mi_blueprint import mi_blueprint
from app.products import products

#crear el objeto flask
app = Flask(__name__)
##configuracion del objeto flaks
app.config.from_object(Config)

#vincular blueprints del proyecto
app.register_blueprint(mi_blueprint)
app.register_blueprint(products)

#Crear el objeto de modelos
db = SQLAlchemy(app)
#Crear el objeto de la migracion
migrate = Migrate(app,db)

#importar los modelos de .models
from .models import Cliente, Producto, Venta, Detalles

