from flask import render_template
from . import products
from . forms import NewProductForm
import app 
import os 

@products.route('/create', methods=["GET", "POST"])
def crear_producto():
    p= app.models.Producto()
    form= NewProductForm()
    
    if form.validate_on_submit():
        ##llenar atributo del objeto producto con eñ formulario
        form.populate_obj(p)
        #registrar en bases de datos
        app.db.session.add(p)
        p.imagen = form.imagen.data.filename
        app.db.session.commit()
        #trasladar la imagen cargada a la carpeta app/prodcts/imagenes 
        archivo= form.imagen.data
        archivo.save(os.path.abspath(os.getcwd()+'/app/products/imagenes/'+p.imagen))
        return os.getcwd()
    return render_template('new.html',
                           form=form)