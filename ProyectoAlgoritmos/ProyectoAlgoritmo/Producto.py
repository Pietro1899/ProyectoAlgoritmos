class Producto: 
    def __init__ (self, json):
        self.nombre = json['name']
        self.descripcion = json['description']
        self.precio = json['price']
        self.categoria = json['category']
        self.inventario = 50
        self.disponible = True
        self.cantidad = 0
    
    #Funcion que regresa los atributos de la clase en string  
    def mostrar(self):
        return f"""
        Nombre: {self.nombre}
        Descripcion: {self.descripcion}
        Precio: {self.precio}
        Categoria: {self.categoria}
        Inventario: {self.inventario}
        """