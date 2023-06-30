class Cliente:
    def __init__(self, nombre, cedula, correo, direccion, telefono, disponible):
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        self.disponible = disponible
    
    #Funcion que regresa los atributos de la clase en string
    def mostrar(self):
        return f"""
        Nombre: {self.nombre}
        Cedula: {self.cedula}
        Correo: {self.correo}
        Direccion: {self.direccion}
        Telefono: {self.telefono}  
        """
    
