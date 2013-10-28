#usr/bin/python

from producto import Producto

class Enlatado(Producto):
    def __init__(self):
        Producto.__init__(self)
        self.__marcar=str('')
	
    def ingresarDatos(self):
	Producto.ingresarDatos(self)
	cant=raw_input("Cantidad en existencia:")
	self.__cant_existencia=int(cant)
        marca=raw_input("Marca del enlatado:")
	self.__marcar=str(marca)

    def imprimirDatos(self):
	Producto.imprimirDatos(self)
	#self.__datos+='| Cantidad existente: %s | Marca: %s ' % (self.__cant_existencia,self.__marcar)
	#print(self.__datos)
    
    

