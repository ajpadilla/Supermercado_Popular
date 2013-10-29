#usr/bin/python

from producto import Producto

class Enlatado(Producto):
    def __init__(self):
        Producto.__init__(self)
        self.marca=str('')

    def ingresarDatos(self):
	Producto.ingresarDatos(self)
	cant=raw_input("Cantidad en existencia:")
        self.cant_existencia=int(cant)
        marca=raw_input("Marca del enlatado:")
	self.marca=str(marca)

    def imprimirDatos(self):
        Producto.imprimirDatos(self) 
        self.datos+='| Cantidad existente: %s | Marca: %s ' % (self.cant_existencia,self.marca)
       	print(self.datos)
    
    

