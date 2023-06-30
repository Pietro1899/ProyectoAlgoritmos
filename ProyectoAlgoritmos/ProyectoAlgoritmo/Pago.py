
class Pago:
    def __init__(self, cliente, monto, moneda, tipo, fecha):
        self.cliente = cliente
        self.monto = monto
        self.moneda = moneda
        self.tipo = tipo
        self.fecha = fecha
    
  #Funcion que regresa los atributos de la clase en string
    def mostrar(self):
        return f"""
        Cliente: {self.cliente.nombre}
        Monto: {self.monto}
        Moneda: {self.moneda}
        Tipo de Pago: {self.tipo}
        Fecha: {self.fecha.mostrar()}
        """
