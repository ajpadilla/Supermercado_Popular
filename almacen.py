#!usr/bin/opcionpython
# -*- coding:utf8 -*-

from producto import Producto
from enlatado import Enlatado
from lacteo_liquido import Lacteo_Liquido
from lacteo_solido import Lacteo_Solido
from carne import Carne
from articulo import Articulo

class Almacen:
   def __init__(self):
       self.__cant_productos=int(0)
       self.__productos=[]      

   def menuPrincipal(self):
      opcion=0
      print("\t\t      Menu Principal    ")
      print("\t\t 1.Añadir producto al almacen")
      print("\t\t 2.Mostrar productos")
      print("\t\t 3.Modificar existencia de un producto")
      print("\t\t 4.Facturar venta")
      print("\t\t 5.Ingresos brutos")
      print("\t\t 6.Egresos de la empresa")
      print("\t\t 7.Reporte de productos con existencia baja")
      print("\t\t 8.Salir")
      opcion=int(raw_input("\t\t Opcion:"))
      return opcion
  
   def menuProductos(self):
       opcion=0
       print("\t\t      Menu Productos    ")
       print("\t\t 1. Enlatado")
       print("\t\t 2. Lacteo Liquido")
       print("\t\t 3. Lacteo Solido")
       print("\t\t 4. Carne")
       print("\t\t 5. Articulo")
       print("\t\t 6.Salir")
       opcion=int(raw_input("\t\t Opcion:"))
       return opcion
    
   def verificarCodigoProducto(self,codigo):
       #print("codigo:"+codigo)
       for producto in self.__productos:
	   if producto.codigo == codigo :
              return True
       return False 
   
   def buscarProducto(self,codigo):
      pos=-1
      print("Productos en almacen:"+str(len(self.__productos)))
      for i in range(len(self.__productos)):
          if self.__productos[i].codigo == codigo :
             return i
      return -1
              

   def agregarProducto(self):
     bandera=False
     while True:
           seleccion=self.menuProductos()
 	   if seleccion == 1:
              producto=Enlatado()
              bandera=True
           elif seleccion == 2:
              producto=Lacteo_Liquido()
              bandera=True
           elif seleccion == 3:
              producto=Lacteo_Solido()
              bandera=True
           elif seleccion == 4:
              producto=Carne()
              bandera=True
           elif seleccion == 5:
              producto=Articulo()
              bandera=True
           elif  seleccion<1 or seleccion>6 :
              print("Opcion Invalida")   
           elif seleccion==6:
              break
   
           if bandera : 	  
             producto.ingresarCodigo()
             if self.verificarCodigoProducto(producto.codigo):
                print("El codigo ya existe")
             else:
               producto.ingresarDatos()
               self.__productos.append(producto)
	       print("Producto agregado al sistema:"+str(len(self.__productos)))
    
   def mostrarProductos(self):
      if len(self.__productos)>0:
        for producto in self.__productos:
          producto.imprimirDatos()
      else:
          print("No hay productos registrados")
           

   def modificarExistenciaProductoAlmacen(self):
       codigo=str('')
       cantidad=0

       codigo=str(raw_input("Ingrese codigo a modificar:"))
       pos=self.buscarProducto(codigo)
       if pos>-1:
          print("Producto localizado")
          cantidad=float(raw_input("Cantidad:"))
          if cantidad>0:
	     producto=self.__productos[pos]
             producto.cant_existencia=cantidad
             self.__productos.insert(pos,producto)
             self.__productos[pos].imprimirDatos()
          else:
              print("Cantidad incorrecta")
       else:
          print("No se encontro el producto") 
       
        
    

   def main(self):
        print("\t\t------ Supermercado Popular------")
        res='s'
        opcion=0
        while True:
          opcion=self.menuPrincipal() 
          if opcion==1:
              self.agregarProducto()
          elif opcion==2:
              self.mostrarProductos() 
          elif opcion==3:
              self.modificarExistenciaProductoAlmacen()          
          if opcion<1 or opcion>8:
             print("Opcion Invalida")
          elif opcion == 8 :
             break
      
             

