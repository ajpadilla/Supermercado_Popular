#!usr/bin/python
class Producto:
    def __init__(self):
	self.__codigo=str(' ')
        self.__descripcion=str('')
        self.__cant_existencia=float(0.00)
        self.__costo_compra=float(0.00)
        self.__precio_venta=float(0.00)
        self.__datos=str('')  
	self.__iva=float(0.00)      
   
    def ingresarCodigo(self):
        codigo=raw_input("Codigo del producto:")
	self.__codigo=str(codigo)
    
    
    def ingresarDatos(self):
        descripcion=raw_input("Descripcion:")
        self.__descripcion=str(descripcion)
        costo_compra=raw_input("Costo de compra:")
        self.__costo_compra=float(costo_compra)
        precio_venta=raw_input("Precio de venta:")
        self.__precio_venta=float(precio_venta)    
    
   
    def imprimirDatos(self):
	self.__datos+='\tCodigo: %s | Descripcion: %s | Costo de compra: %.2f | Precio de venta: %.2f' % (self.__codigo,self.__descripcion,
  												          self.__costo_compra,self.__precio_venta)
        print(self.__datos)
         
    def set_codigo(self,cod):
        self.__codigo=str(cod)
    
    def set_descripcion(self,des):
	self.__descripcion=str(des)

    def set_cant_existencia(self,cant):
        self.__cant_existencia=float(cant)
    
    def set_costo_compra(self,costo):
	self.__costo_compra=costo

    def set_precio_venta(self,precio):
	self.__precio_venta=precio

    def get_codigo(self):
	return self.__codigo

    def get_descripcion(self):
	return self.__descripcion

    def get_cant_existencia(self):
	return self.__cant_existencia

    def get_costo_compra(self):
        return self.__costo_compra

    def get_precio_venta(self):
	return self.__precio_venta

 



  
    def algo(self):
	algo=0
        print(algo)




	
