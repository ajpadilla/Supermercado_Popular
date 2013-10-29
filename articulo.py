#usr/bin/python

from producto import Producto

class Articulo(Producto):
    def __init__(self):
        Producto.__init__(self)
        self.marcar=str('')	

    def ingresarDatos(self):
	Producto.ingresarDatos(self)
	cant=raw_input("Cantidad en existencia:")
	self.cant_existencia=int(cant)
        marca=raw_input("Marca del articulo:")
	self.marcar=str(marca)

    def imprimirDatos(self):
	Producto.imprimirDatos(self)
	self.datos+='| Cantidad existente: %s | Marca del articulo: %s ' % (self.cant_existencia,self.marcar)
	print(self.datos)
    
    
