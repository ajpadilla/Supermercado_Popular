#!usr/bin/python 
from producto import Producto

class Lacteo_Solido(Producto):
    def __init__(self):
      Producto.__init__(self)
     
    def ingresarDatos(self):
      Producto.ingresarDatos(self)
      kilos=float(raw_input("Kilos:"))
      self.cant_existencia=kilos
   
    def imprimirDatos(self):
       Producto.imprimirDatos(self)
       self.datos+="kilos: %s" % (self.cant_existencia)
       print(self.datos)
