#!usr/bin/python 
from producto import Producto

class Lacteo_Liquido(Producto):
    def __init__(self):
      Producto.__init__(self)
   
     
    def ingresarDatos(self):
      Producto.ingresarDatos(self)
      litros=float(raw_input("Litros:"))
      self.cant_existencia=litros
   
    def imprimirDatos(self):
       Producto.imprimirDatos(self)
       self.datos+=" Litros: %s" % (self.cant_existencia)
       print(self.datos)
