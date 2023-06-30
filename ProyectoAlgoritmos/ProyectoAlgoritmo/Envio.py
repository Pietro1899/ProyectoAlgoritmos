class Envio:
    def __init__(self, idCompra, servicio, motorizado, costo, fecha, cliente):
        self.idCompra = idCompra 
        self.servicio = servicio
        self.motorizado = motorizado
        self.costo = costo
        self.pendiente = False
        self.fecha = fecha
        self.cliente = cliente
        
    #Funcion que regresa los atributos de la clase en string
    def mostrar(self):
        return f"""
        Num de Venta: {self.idCompra}
        Cliente: {self.cliente.nombre}
        Servicio: {self.servicio}
        Motorizado: {self.motorizado}
        Costo: {self.costo}
        fecha: {self.fecha.mostrar()}
        """