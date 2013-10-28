#!usr/bin/python
# -*- coding:utf8 -*-

from producto import Producto
from enlatado import Enlatado

class Almacen:
   def __init__(self):
       self.__cant_productos=int(0)
       self.__productos=[]      

   def menuPrincipal(self):
      opcion=0
      print("Menu Principal")
      print("1.Añadir producto al almacen")
      print("2.Modificar existencia de un producto")
      print("3.Facturar venta")
      print("4.Ingresos brutos")
      print("5.Egresos de la empresa")
      print("6.Reporte de productos exentos de IVA con mayores ventas")
      print("7.Reporte de productos con existencia baja")
      print("8.Salir")
      opcion=int(raw_input("Opcion:"))
      return opcion
  
   def menuProductos(self):
       opcion=0
       print("Menu Productos ")
       print("1. Enlatado")
       print("2. Lacteo Liquido")
       print("3. Lacteo Solido")
       print("4. Carne")
       print("5. Articulo")
       print("6.Salir")
       opcion=int(raw_input("Opcion:"))
       return opcion
    
   def verificarCodigoProducto(self,codigo):
       #print("codigo:"+codigo)
       for producto in self.__productos:
	   if producto.get_codigo() == codigo:
              return True
       return False 
   
   def buscarProducto(self,codigo):
      pos=-1
      print("cant_pro:"+str(len(self.__productos)))
      for i in range(len(self.__productos)):
          if self.__productos[i].get_codigo()==codigo:
             print("Hola")
             return i
      return -1
              
        

 
   def agregarProducto(self):
     seleccion=0
     while seleccion>=0 and seleccion<=6:
           seleccion=self.menuProductos()
       
 	   if seleccion == 1 :
              producto=Enlatado() 

           if seleccion<=0 or seleccion>=6:
              print("Opcion Invalida")
              break  

           producto.ingresarCodigo()
           if(self.verificarCodigoProducto(producto.get_codigo())):
               print("El codigo ya existe")
           else:
               producto.ingresarDatos()
               self.__productos.append(producto)
	       print("Producto agregado al sistema"+str(len(self.__productos)))
        
   def buscarProductoAlmacen(self):
       codigo=str(raw_input("Ingrese codigo a buscar:"))
       pos=self.buscarProducto(codigo)
       if pos>-1:
          self.__productos[pos].imprimirDatos()
       else:
          print("No se encontro el producto") 

   def main(self):
        res='s'
        opcion=0
        while opcion>=0 and  opcion<8:
          opcion=self.menuPrincipal() 
          if opcion==1:
              self.agregarProducto()
          if opcion==2:
              self.buscarProductoAlmacen()          

          if opcion<=0 or opcion>8:
             print("Opcion Invalida")
             break
      
             
  
