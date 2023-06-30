from Cliente import Cliente
class Juridico(Cliente):
    def __init__(self, nombre, cedula, correo, direccion, telefono, disponible):
        super().__init__(nombre, cedula, correo, direccion, telefono, disponible)
        self.pendiente = False
    