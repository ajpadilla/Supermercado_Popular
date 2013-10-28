#!usr/bin/python 
from producto import Producto

class Lacteo_Liquido(Producto):
    def __init__(self):
      Producto.__init__(self)
      self.__litros=float(0.00)
      self.__datos=str('')
     
    def ingresarDatos(self):
      Producto.ingresarDatos(self)
      litros=float(raw_input("Litros:"))
      self.__litros=litros
   
    def imprimirDatos(self):
       Producto.imprimirDatos(self)
       self.__datos+="\t Litros: %s" % (self.__litros)
       print(self.__datos)
