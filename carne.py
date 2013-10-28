#!usr/bin/python 
from producto import Producto

class Carne(Producto):
    def __init__(self):
      Producto.__init__(self)
      self.__kilos=float(0.00)
      self.__datos=str('')
     
    def ingresarDatos(self):
      Producto.ingresarDatos(self)
      kilos=float(raw_input("Kilos:"))
      self.__kilos=kilos
   
    def imprimirDatos(self):
       Producto.imprimirDatos(self)
       self.__datos+="\t Kilos: %s" % (self.__kilos)
       print(self.__datos)
