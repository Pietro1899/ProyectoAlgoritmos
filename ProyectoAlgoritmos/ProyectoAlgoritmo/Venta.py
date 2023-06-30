from Juridico import Juridico
class Venta:
    def __init__(self, cliente, carrito, fecha):
        self.cliente = cliente
        self.carrito = carrito
        self.metodoPago = ''
        self.metodoEnvio = ''
        self.subtotal = 0
        self.descuento = 0
        self.iva = 0.16
        self.igtf = 0
        self.total = 0      
        self.fecha = fecha
    
    #Funcion que te permite calcular el precio    
    def calcularPrecio(self, precio):
        if self.metodoPago == "Dolares":
            self.igtf = 0.03
            self.total = round(precio * self.igtf, 2)
        else:
            self.total = round(precio, 2)
            
        if isinstance(self.cliente, Juridico):
            self.total -= (self.total * 0.05)
            self.descuento = 0.05
            

        self.subtotal = round(self.total / (1 + self.iva), 2)

    #Sacar el precio del carrito del cliente
    def obtenerPrecio(self):
        precio = 0
        for producto in self.carrito:
            precio += producto.precio * producto.cantidad

        self.calcularPrecio(precio)

    #Describir el carrito de productos
    def decribir_carrito(self):
        message = f""
        for i, producto in enumerate(self.carrito):
            message += f"""
        {i+1}.- {producto.nombre} --- Cantidad: {producto.cantidad}"""
        return message 

    #mostrar el previo de la venta
    def previo(self):
        mensaje = f"Productos:\n"
        for i, producto in enumerate(self.carrito):
            mensaje += f"{i+1}.- {producto.nombre} --- Cantidad: {producto.cantidad}\n"
        
        return f"COMPRA:\nCliente: {self.cliente.nombre}\n{mensaje}-----------------------------\nMonto total: {round(self.total, 2)}$\n"
    
    #Funcion que regresa la factura
    def mostrar(self):
        return f""" 
            FACTURA
        --------------{self.cliente.mostrar()}Productos:{self.decribir_carrito()}
        Método de pago: {self.metodoPago}
        Método de envío: {self.metodoEnvio}
        IVA: {self.iva}
        IGTF: {self.igtf}
        Subtotal: {self.subtotal}$
        Descuento: {self.descuento}$
                {self.tipoCliente()}
        ---------------------------  
        Monto Total: {self.total}$
        """
        
    def tipoCliente(self):
        if isinstance(self.cliente, Juridico):
            return f"\nPago: {'Pendiente' if self.cliente.pendiente else 'Cancelado'}"
        
        return '\n'