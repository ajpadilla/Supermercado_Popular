#usr/bin/python

from producto import Producto

class Articulo(Producto):
    def __init__(self):
        Producto.__init__(self)
        self.__marcar=str('')
        self.__datos=str('')	

    def ingresarDatos(self):
	Producto.ingresarDatos(self)
	cant=raw_input("Cantidad en existencia:")
	self.__cant_existencia=int(cant)
        marca=raw_input("Marca del articulo:")
	self.__marcar=str(marca)

    def imprimirDatos(self):
	Producto.imprimirDatos(self)
	self.__datos+='\t | Cantidad existente: %s | Marca del articulo: %s ' % (self.__cant_existencia,self.__marcar)
	print(self.__datos)
    
    
