from Cliente import Cliente

class Natural(Cliente):
    def __init__(self, nombre, cedula, correo, direccion, telefono, disponible):
        super().__init__(nombre, cedula, correo, direccion, telefono, disponible)
        