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
       self.iva=float(0.00)
       self.datos=str('')

    def agregarProducto(self,producto):
        self.productos.append(producto)
    
    def imprimir(self):
       for producto in self.productos:
           producto.imprimirDatosVenta()
   
    def calcularPago(self):
        self.monto=0
        self.sub_total=0        
        self.total=0
        print("Cedula cliente:"+self.cedula_cliente)
        for producto in self.productos:
            self.monto=(producto.precio_venta * producto.cant_vendida)
            self.sub_total+=self.monto
            print("Cod: %s | Desc: %s | Cant: %s | Precio: %.2f | Monto: %.2f" % (producto.codigo,producto.descripcion,
                                                                                        producto.cant_vendida,producto.precio_venta,self.monto))
           # print(self.datos)
            
        self.iva=(self.sub_total * (0.12) )
        self.total=(self.sub_total +self.iva)
        print("Sub-total Bs:"+str(self.sub_total)) 
        print("IVA:"+str(self.iva)+" "+"12%")
        print("Total Bs:"+str(self.total))
