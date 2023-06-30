class Fecha():
    def __init__(self, dia, mes, año):
        self.año = año
        self.dia  = dia
        self.mes = mes
        self.completa = f"{self.dia}/{self.mes}/{self.año}"
    
    #Funcion que regresa los atributos de la clase en string    
    def mostrar(self):
        return f"{self.dia}/{self.mes}/{self.año}"