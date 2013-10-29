#!usr/bin/python
class Producto:
    def __init__(self):
	self.codigo=str(' ')
        self.descripcion=str('')
        self.cant_existencia=float(0.00)
        self.costo_compra=float(0.00)
        self.precio_venta=float(0.00)
        self.datos=str('') 
        self.cant_vendida=0 
	self.iva=float(0.00)      
   
    def ingresarCodigo(self):
        codigo=raw_input("Codigo del producto:")
	self.codigo=str(codigo)
    
    
    def ingresarDatos(self):
        descripcion=raw_input("Descripcion:")
        self.descripcion=str(descripcion)

        costo_compra=raw_input("Costo de compra:")
        self.costo_compra=float(costo_compra)

        precio_venta=raw_input("Precio de venta:")
        self.precio_venta=float(precio_venta)
    
    def imprimirDatosVenta(self):
        self.texto=str("")
        self.texto+="\t Codigo: %s | Descripcion: %s | Precio: %.2f Cantidad vendida: %d" % (self.codigo,self.descripcion,self.precio_venta,
                                                                                              self.cant_vendida)
        print(self.texto)
              
    def imprimirDatos(self):
	self.datos+='\t Codigo: %s | Descripcion: %s | Costo de compra: %.2f | Precio de venta: %.2f' % (self.codigo,self.descripcion,
  												          self.costo_compra,self.precio_venta)
  
 
class Factura:
    def __init__(self):
       self.cedula_cliente=str('')
       self.productos=[] 

    def agregarProducto(self,producto):
        self.productos.append(producto)
    
    def imprimir(self):
       for producto in self.productos:
           producto.imprimirDatosVenta()


    
