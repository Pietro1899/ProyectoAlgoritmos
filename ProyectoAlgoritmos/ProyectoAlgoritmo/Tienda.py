from Cliente import Cliente
from Natural import Natural
from Juridico import Juridico
from Envio import Envio
from Producto import Producto
from Pago import Pago
from Venta import Venta
from Fecha import Fecha
from Validacion import Validacion
from urllib.request import urlopen
import copy
import requests
import pickle
import matplotlib.pyplot as plt
import numpy as np

class Tienda: 
    def __init__(self):
        self.productos = []
        self.ventas = []
        self.clientes = []
        self.pagos = []
        self.envios = []

# Crea los productos con la informacion de la api, al inicio del programa
    def agregarProductos(self, infoLista):
        for json in infoLista:
            self.productos.append(Producto(json))   # Se crean los productos
            

# Se gurada la informacion en un txt, cuando el programa se cierra
    def guardar_info(self):
        with open('Productos.txt', 'wb') as file:
            pickle.dump(self.productos, file)

        with open('Ventas.txt', 'wb') as file:
            pickle.dump(self.ventas, file)
            
        with open('Clientes.txt', 'wb') as file:
            pickle.dump(self.clientes, file)
        
        with open('Pagos.txt', 'wb') as file:
            pickle.dump(self.pagos, file)
        
        with open('Envios.txt', 'wb') as file:
            pickle.dump(self.envios, file)

#Lee la informacion del txt para poder tener la informacion anterior
    def extraerInfo(self):
        #Agregar Productos
        try:
            with open('Productos.txt', 'rb') as file:
                new_file = pickle.load(file)
                for i, p in enumerate(new_file):
                    self.productos[i] = p
        except:
            return


        #Agregar Ventas
        try:
            with open('Ventas.txt', 'rb') as file:
                new_file = pickle.load(file)
                for v in new_file:
                    self.ventas.append(v)
        except:
            return 


        #Agregar Clientes
        try:
            with open('Clientes.txt', 'rb') as file:
                new_file = pickle.load(file)
                for c in new_file:
                    self.clientes.append(c)
        except:
            return 
            
        

        try:
            #Agregar Pagos
            with open('Pagos.txt', 'rb') as file:
                new_file = pickle.load(file)
                for p in new_file:
                    self.pagos.append(p)
        except:
            return 


        try:
            #Agregar Envios
            with open('Envios.txt', 'rb') as file:
                new_file = pickle.load(file)
                for e in new_file:
                    self.envios.append(e)
        except:
            return 

#Le pregunta a el usuario el tipo de filtro que desea aplicarle a los productos
    def buscarProductos(self):
        print('\nTipos de Filtro:')
        opcion = Validacion.opcion(" 1. Categoría \n 2. Descripción \n 3. Precio \n 4. Nombre\n 5. Disponibilidad de Inventrio\n Seleccione un filtro (1-5): ", 5)
        productosFiltrados = list(filter(lambda x: x.disponible , self.productos))
        
        
        if opcion == 1:
            print('\nCATEGORIAS:')
            categorias = list(set([producto.categoria for producto in productosFiltrados]))
            self.filtrarInfo(categorias, productosFiltrados, 'categoriaProducto', 'Seleccione una de las caregorias')
            
        elif opcion == 2:
            print('\nDESCRPCIONES:')
            descripciones = list(set([producto.descripcion for producto in productosFiltrados]))
            self.filtrarInfo(descripciones, productosFiltrados, 'descripcionProducto', 'Seleccione una de las descripciones')
            
        elif opcion == 3:
            print('\nPRECIOS:')
            precios = list(set([producto.precio for producto in productosFiltrados]))
            self.filtrarInfo(precios, productosFiltrados, 'precioProducto', 'Seleccione uno de los precios' )
            
        elif opcion == 4:
            print('\nNOMBRES:') 
            nombres = list(set([producto.nombre for producto in productosFiltrados]))
            self.filtrarInfo(nombres, productosFiltrados, 'nombreProducto', 'Seleccione un de los nombres' )
            
        else:
            print('\nDISPONIBILIDAD DE LOS PRODUCTOS (INVENTARIO):')
            inventario = list(set([producto.inventario for producto in productosFiltrados]))
            self.filtrarInfo(inventario, productosFiltrados, 'inventarioProducto', 'Seleccione una de las disponibilidades' )
            

#Tiene toda la logica del los filtros que se solicitan
    def filtrarInfo(self, lista, listaFiltrada, tipo, mensaje):
        listafinal = []
        self.mostrarOpciones(lista)
        seleccion = Validacion.opcion(f'{mensaje} (1-{len(lista)}): ', len(lista))
        if tipo == 'nombreProducto':
            listaFinal = list(filter(lambda producto: producto.nombre == lista[seleccion - 1], listaFiltrada))
        elif tipo == 'descripcionProducto':
            listaFinal = list(filter(lambda producto: producto.descripcion == lista[seleccion - 1], listaFiltrada))
        elif tipo == 'precioProducto':
            listaFinal = list(filter(lambda producto: producto.precio == lista[seleccion - 1], listaFiltrada))
        elif tipo == 'inventarioProducto':
            listaFinal = list(filter(lambda producto: producto.inventario == lista[seleccion - 1], listaFiltrada))
        elif tipo == 'categoriaProducto':
            listaFinal = list(filter(lambda producto: producto.categoria == lista[seleccion - 1], listaFiltrada))
        elif tipo == 'cedulaCliente':
            listaFinal = list(filter(lambda cliente: cliente.cedula == lista[seleccion - 1], listaFiltrada))
        elif tipo == 'correoCliente':
            listaFinal = list(filter(lambda cliente: cliente.correo == lista[seleccion - 1], listaFiltrada))
        elif tipo == 'clientePago':
            listaFinal = list(filter(lambda pago: pago.cliente.nombre == lista[seleccion - 1], listaFiltrada))
        elif tipo == 'tiposPago':
            listaFinal = list(filter(lambda pago: pago.tipo == lista[seleccion - 1], listaFiltrada))
        elif tipo == 'monedaPago':
            listaFinal = list(filter(lambda pago: pago.moneda == lista[seleccion - 1], listaFiltrada))
        elif tipo == 'clienteVenta':
            listaFinal = list(filter(lambda venta: venta.cliente.nombre == lista[seleccion - 1], listaFiltrada))
        elif tipo == 'clienteEnvio':
            listaFinal = list(filter(lambda envio: envio.cliente.nombre == lista[seleccion - 1], listaFiltrada))
        elif tipo == 'fechaEnvio':
            listaFinal = list(filter(lambda envio: envio.fecha.completa == lista[seleccion - 1], listaFiltrada))
        elif tipo == 'pagoFecha':
            listaFinal = list(filter(lambda pago: pago.fecha.completa == lista[seleccion - 1], listaFiltrada))
        elif tipo == 'ventaFecha':
            listaFinal = list(filter(lambda venta: venta.fecha.completa == lista[seleccion - 1], listaFiltrada))    
        elif tipo == 'montoVenta':
            listaFinal = list(filter(lambda venta: venta.total == lista[seleccion - 1], listaFiltrada))    
        else:
            pass
        print('\n------------- RESULTADOS -------------')
        self.mostrarInfoObjeto(listaFinal)
        
        
#Le pregunta a el usuario el tipo de filtro que desea aplicarle a los clientes        
    def buscarClientes(self):
        
        if self.clientes != []:
            print('\nTipos de Filtro:')
            opcion = Validacion.opcion(" 1. Cédula o RIF \n 2. Correo electrónico \n Seleccione un filtro (1-2): ", 2)
            clientesFiltrados = list(filter(lambda x: x.disponible , self.clientes))

            if opcion == 1:
                print('\nCEDULAS Y RIF:')
                cedulas = list(set([cliente.cedula for cliente in clientesFiltrados]))
                self.filtrarInfo(cedulas, clientesFiltrados, 'cedulaCliente', 'Seleccione una de las cedulas')
                
            else:
                print('\nCORREOS ELECTRONICOS:')
                correos = list(set([cliente.correo for cliente in clientesFiltrados]))
                self.filtrarInfo(correos, clientesFiltrados, 'correoCliente', 'Seleccione uno de los correos')
        else: 
            print('\nNo hay clientes registrados')
            input('Dale enter para continuar... ')


#Le pregunta a el usuario el tipo de filtro que desea aplicarle a los pagos        
    def buscarPago(self):
        if self.pagos != []:
            print('\nTipos de Filtro:')
            opcion = Validacion.opcion(" 1. Cliente \n 2. Fecha \n 3. Tipo de Pago \n 4. Moneda de Pago\n Seleccione un filtro (1-4): ", 4)
            if opcion == 1:
                print('\nCLIENTES:')
                clientes = list(set([pago.cliente.nombre for pago in self.pagos]))
                self.filtrarInfo(clientes, self.pagos, 'clientePago', 'Seleccione uno de los clientes')
                
            elif opcion == 2:
                print('\nFRECHAS:')
                fechas = list(set([pago.fecha.completa for pago in self.pagos]))
                self.filtrarInfo(fechas, self.pagos, 'pagoFecha', 'Seleccione una de las fechas de los pagos')
            elif opcion == 3:
                print('\nTIPO DE PAGOS:')
                tiposPago = list(set([pago.tipo for pago in self.pagos]))
                self.filtrarInfo(tiposPago, self.pagos, 'tiposPago', 'Seleccione uno de los tipos de pago' )
                
            else:
                print('\nMONEDAS DE PAGO:') 
                monedasPago = list(set([pago.moneda for pago in self.pagos]))
                self.filtrarInfo(monedasPago, self.pagos, 'monedaPago', 'Seleccione una de las monedas de pago' )
        else:
            print('\nNo se ha registrado ningun pago')
            input('Dale enter para continuar... ')

        
#Le pregunta a el usuario el tipo de filtro que desea aplicarle a las ventas        
    def buscarVentas(self):
        if self.ventas != []:
            print('\nTipos de Filtro:')
            opcion = Validacion.opcion(" 1. Cliente \n 2. Fecha \n 3. Monto Total \n Seleccione un filtro (1-3): ", 3)
            if opcion == 1:
                print('\nCLIENTES:')
                clientes = list(set([venta.cliente.nombre for venta in self.ventas]))
                self.filtrarInfo(clientes, self.ventas, 'clienteVenta', 'Seleccione uno de los clientes')
                
            elif opcion == 2:
                print('\nFRECHAS:')
                fechas = list(set([venta.fecha.completa for venta in self.ventas]))
                
                self.filtrarInfo(fechas, self.ventas, 'ventaFecha', 'Seleccione una de las fechas de los pagos')

            else:
                print('\nMONTOS TOTALES DE LAS VENTAS:')
                montos = list(set([venta.total for venta in self.ventas]))
                self.filtrarInfo(montos, self.ventas, 'montoVenta', 'Seleccione uno de los montos' )
        else:
            print('\nNo se ha realizado ninguna venta')
            input('Dale enter para continuar ... ')

#Le pregunta a el usuario el tipo de filtro que desea aplicarle a los envios        
    def buscarEnvios(self):
        if self.envios != []:
            print('\nTipos de Filtro:')
            opcion = Validacion.opcion(" 1. Cliente \n 2. Fecha \n Seleccione un filtro (1-2): ", 2)
            if opcion == 1:
                print('\nCLIENTES:')
                nombres = list(set([envio.cliente.nombre for envio in self.envios]))
                self.filtrarInfo(nombres, self.envios, 'clienteEnvio', 'Seleccione uno de los clientes: ')
                
            else:
                print('\nFECHA:')
                fechas = list(set([envio.fecha.completa for envio in self.envios]))
                self.filtrarInfo(fechas, self.envios, 'fechaEnvio', 'Seleccione una de las fechas: ')
        else:
            print('\nNo se ha realizado ningun envio')
            input('Dale enter para continuar ... ')

#Funcion que te permite modificar a los productos           
    def modificarProducto(self):
        atributos = ['Nombre', 'Descripicion', 'Precio', 'Categoria', 'Inventario']
        respuesta = 's'
        productosDisponibles = list(filter(lambda x: x.disponible , self.productos))
        nombres = [producto.nombre for producto in productosDisponibles]
        self.mostrarOpciones(nombres)
        opcion = Validacion.opcion(f"Seleccione el nombre del producto al cual le desea modificar la informacion 1-{len(nombres)}: ", len(nombres))
        producto = productosDisponibles[opcion - 1]
        while respuesta == 's':
            self.mostrarOpciones(atributos)
            opcion = Validacion.opcion(f"Selecciona el atributo que deseas modificarle al producto 1-{len(atributos)}: ", len(atributos))
            if opcion == 1:
                nombre = Validacion.string('\nIngrese el nuevo nombre: ')
                producto.nombre = nombre
            elif opcion == 2:
                descripcion = Validacion.string('\nIngrese la nueva descripcion: ')
                producto.descripcion = descripcion
            elif opcion == 3:
                precio = Validacion.numero('\nIngrese el nuevo precio: ')
                cliente.precio = precio
            elif opcion == 4:
                categoria = Validacion.string('\nIngrese la nueva categoria: ')
                producto.categoria = categoria
            elif opcion == 5:
                inventario = Validacion.numero('\nIngrese el nuevo inventario: ')
                producto.inventario = inventario
            
            respuesta = Validacion.escogencia('\nDesea modificar algun otro atributo (s/n): ').lower()
        
        print('\nLa modificacion se realizo con exito\nNueva informacion:')
        print(producto.mostrar())
        input('Dale enter para continuar ... ')

#Funcion que te permite modificar a los clientes           
    def modificarCliente(self):
        if self.clientes != []:
            atributos = ['Nombre', 'Cedula', 'Correo', 'Direccion', 'Telefono'] 
            respuesta = 's'
            clientesDisponibles = list(filter(lambda x: x.disponible , self.clientes))
            
            nombres = [cliente.nombre for cliente in clientesDisponibles]
            self.mostrarOpciones(nombres)
            opcion = Validacion.opcion(f"Seleccione el nombre del cliente al cual le dese modificar la informacion 1-{len(nombres)}: ", len(nombres))
            cliente = clientesDisponibles[opcion - 1]
            while respuesta == 's':
                self.mostrarOpciones(atributos)
                opcion = Validacion.opcion(f"Selecciona el atributo que deseas modificarle al cliente 1-{len(atributos)}: ", len(atributos))
                if opcion == 1:
                    nombre = Validacion.string('\nIngrese el nuevo nombre: ')
                    cliente.nombre = nombre
                elif opcion == 2:
                    cedula = Validacion.numero('\nIngrese la nueva cedula: ')
                    cliente.cedula = cedula
                elif opcion == 3:
                    correo = Validacion.correo('\nIngrese el nuevo correo: ')
                    cliente.correo = correo
                elif opcion == 4:
                    direccion = Validacion.string('\nIngrese la nueva direccion: ')
                    cliente.direccion = direccion
                elif opcion == 5:
                    telefono = Validacion.telefono('\nIngrese el nuevo telefono ej(0424348943): ')
                    cliente.telefono = telefono
                respuesta = Validacion.escogencia('\nDesea modificar algun otro atributo (s/n): ')
            
            print('\nLa modificacion se realizo con exito\nNueva informacion:')
            print(cliente.mostrar())
            input('Dale enter para continuar ... ')
        else:
            print('No hay clientes registrados')  
            input('Dale enter para continuar ... ')  
        
#Permite que el usuario escoja el producto a eliminar    
    def eliminarProducto(self):
        productosFiltrados = list(filter(lambda x: x.disponible , self.productos))
        self.mostrarInfoObjeto(productosFiltrados)
        seleccion = Validacion.opcion(f'Selecciona el producto que desea eliminar (1-{len(productosFiltrados)}): ', len(productosFiltrados))
        productosFiltrados[seleccion -1 ].disponible = False

#Permite que el usuario escoja el cliente a eliminar 
    def eliminarCliente(self):
        if self.clientes != []:
            clientesFiltrdos = list(filter(lambda x: x.disponible , self.clientes))
            self.mostrarInfoObjeto(clientesFiltrdos)
            seleccion = Validacion.opcion(f'Selecciona al cliente que desea eliminar (1-{len(clientesFiltrdos)}): ', len(clientesFiltrdos))
            clientesFiltrdos[seleccion -1 ].disponible = False
            print('El cliente fue eliminado exitosamente')
        else:
            print('No hay clientes registrados')

#Metodo para imprimir las opciones que el usuario tiene
    def mostrarOpciones(self, lista):
        for i , elemento in enumerate(lista):
            print(f'{i + 1}. {elemento}') 
    
#Metodo para imprimir el deltallado de un objeto
    def mostrarInfoObjeto(self, lista):
        for i , elemento in enumerate(lista):
            print(f'{i + 1}. {elemento.mostrar()}') 


#funcion para el grafico que te permite calcular la cantidad de compras que hizo un cliente 
    def calcular_cantidad_compras(self, nombre):
        cantidadCompras = 0
       
        for venta in self.ventas:
            if venta.cliente.nombre == nombre:
                cantidadCompras += 1
        
        return cantidadCompras
    


#Funcion que te permite mostrarle al usuario las estadisticas de la tienda
    def estdisticas(self):
        if self.ventas != []:
            seleccion = Validacion.opcion('1. Informe de ventas \n2. Informe de Pagos\n3. Informe de Envios\nSeleccione una de las opciones: ', 3)
            clientesDisponibles = list(filter(lambda x: x.disponible , self.clientes))
            print("\nOpciones:")
            if seleccion == 1:
                opcion = Validacion.opcion('1. Ventas totales\n2. Productos Mas vendidos\n3. Cliente mas frecuente\nSeleccione una de las opciones: ', 3)
        
                if opcion == 1:
                    # periodo = Validacion.opcion('Ventas por: \n 1. Dia \n 2. Semana\n 3. Mes\n 4. Año\n Seleccione una de las opciones: ', 4)
                    conteo = self.ventasPorPeriodo()
                    print()
                    for ano, meses in conteo.items():
                        print(f"Año: {ano}:")
                        ventas_totales_ano = 0
                        for mes, dias in meses.items():
                            ventas_totales_mes = 0
                            print(f" Mes: {mes}:")
                            for dia, total in dias.items():
                                ventas_totales_mes += total
                                print(f"   Dia {dia}: {total}$")
                            ventas_totales_ano += ventas_totales_mes
                            print(f" Ventas totales por el mes {mes}: {ventas_totales_mes}$")
                        print(f" Ventas totales en el año {ano}: {ventas_totales_ano}$")
                        
                        print()

                    ventas_por_anio = []
                    for year, meses in conteo.items():
                        sales_per_month = []
                        for month, dias in meses.items():
                            sales_per_day = list(dias.values())
                            sales_per_month.append(sales_per_day)
                        ventas_por_anio.append(sales_per_month)

                    # Crear gráfico de barras
                    fig, ax = plt.subplots()
                    ventas_sin_enero = ventas_por_anio[0][0][1:]  # eliminar el primer elemento (correspondiente a enero)
                    ax.bar(range(len(ventas_sin_enero)), ventas_sin_enero, label="")
                    accumulated_sales = list(ventas_por_anio[0][0])
                    for i in range(1, len(ventas_por_anio[0])):
                        accumulated_sales = [x + y for x, y in zip(accumulated_sales, ventas_por_anio[0][i-1])]
                        ax.bar(range(len(ventas_por_anio[0][i])), ventas_por_anio[0][i], bottom=accumulated_sales, label=f"Mes {i+1}")
                    ax.legend()
                    ax.set_xlabel("Días")
                    ax.set_ylabel("Ventas")
                    ax.set_title("Ventas por mes y día en 2023")
                    plt.show()
                        
                    input('\nDale enter para continuar ... ')

                
                elif opcion == 2:
                    #Codigo para productos mas vendidos
                    productos_ordenados = sorted(self.productos, key=lambda p: p.inventario)[:3]
                    print('\nProductos mas vendidos: \n')
                    for i, producto  in enumerate(productos_ordenados):
                        print(f' {i + 1}. {producto.nombre} - {50 - producto.inventario}')
                    
                    
                    cantidades_vendidas = [50 - producto.inventario for producto in productos_ordenados]

                    # Crear una secuencia de valores numéricos para las coordenadas en el eje x
                    coordenadas_x = np.arange(len(productos_ordenados))

                    # Crear el gráfico de barras
                    plt.bar(coordenadas_x, cantidades_vendidas, width=0.8)

                    # Modificar las etiquetas del eje x para mostrar los nombres de los productos
                    nombres_productos = [producto.nombre for producto in productos_ordenados]
                    plt.xticks(coordenadas_x, nombres_productos)

                    # Agregar etiquetas al eje y y el título del gráfico
                    plt.ylabel('Cantidad vendida')
                    plt.title('Productos más vendidos')

                    # Mostrar el gráfico
                    plt.show()
                    input('\nDale enter para continuar ... ')
                else:
                    listaClientes= self.clienteMasVendido()
                    print('\Clientes mas Frecuentes: \n')   
                    for i, cliente  in enumerate(listaClientes):
                        print(f'{i +1}. {cliente}')
                    
                    # Crear una lista de coordenadas en el eje x
                    coordenadas_x = range(len(listaClientes))

                    # Crear una lista de cantidades vendidas para cada cliente
                    cantidades_vendidas = [self.calcular_cantidad_compras(cliente) for cliente in listaClientes]

                    # Crear el gráfico de barras
                    plt.bar(coordenadas_x, cantidades_vendidas, width=0.8)

                    # Modificar las etiquetas del eje x para mostrar los nombres de los clientes
                    plt.xticks(coordenadas_x, listaClientes)

                    # Agregar etiquetas al eje y y el título del gráfico
                    plt.ylabel('Cantidad de compras')
                    plt.title('Clientes más frecuentes')

                    # Mostrar el gráfico
                    plt.show()
                    
                    input('\nDale enter para continuar ... ')
                    
            elif seleccion == 2:
                opcion = Validacion.opcion('1. Pagos totales\n2. Clientes con pagos pendientes\n Seleccione una de las opciones: ', 2)
                if opcion == 1:
                    conteo = self.pagosPorPeriodo()
                    print()
                    for ano, meses in conteo.items():
                        print(f"Año: {ano}:")
                        ventas_totales_ano = 0
                        for mes, dias in meses.items():
                            ventas_totales_mes = 0
                            print(f" Mes: {mes}:")
                            for dia, total in dias.items():
                                ventas_totales_mes += total
                                print(f"   Dia {dia}: {total}$")
                            ventas_totales_ano += ventas_totales_mes
                            print(f" Pagos totales por el mes {mes}: {ventas_totales_mes}$")
                        print(f" Pagos totales en el año {ano}: {ventas_totales_ano}$")
                        
                        print()
                    
                    
                    ventas_por_anio = []
                    for year, meses in conteo.items():
                        sales_per_month = []
                        for month, dias in meses.items():
                            sales_per_day = list(dias.values())
                            sales_per_month.append(sales_per_day)
                        ventas_por_anio.append(sales_per_month)

                    # Crear gráfico de barras
                    fig, ax = plt.subplots()
                    ventas_sin_enero = ventas_por_anio[0][0][1:]  # eliminar el primer elemento (correspondiente a enero)
                    ax.bar(range(len(ventas_sin_enero)), ventas_sin_enero, label="")
                    accumulated_sales = list(ventas_por_anio[0][0])
                    for i in range(1, len(ventas_por_anio[0])):
                        accumulated_sales = [x + y for x, y in zip(accumulated_sales, ventas_por_anio[0][i-1])]
                        ax.bar(range(len(ventas_por_anio[0][i])), ventas_por_anio[0][i], bottom=accumulated_sales, label=f"Mes {i+1}")
                    ax.legend()
                    ax.set_xlabel("Días")
                    ax.set_ylabel("Pagos")
                    ax.set_title("Pagos por mes y día en 2023")
                    plt.show()
                       

                else:
                    clientesPedientes = self.clientePendiente()
                    print("\nClientes con pagos pendientes: ")
                    for i, cliente  in enumerate(list(set(clientesPedientes))):
                        print(f'{i +1}. {cliente.nombre}')
                    
                    nombresClientes = [cliente.nombre for cliente in clientesPedientes]
                    # Crear una lista de valores iguales (1) para cada cliente en la lista de nombresClientes
                    valores = [1] * len(nombresClientes)

                    # Configurar la figura del gráfico
                    fig, ax = plt.subplots(figsize=(10, 10))
                    ax.set_title("Clientes con pagos pendientes", fontsize=20)

                    # Crear el gráfico de torta
                    ax.pie(valores, labels=nombresClientes, autopct='%1.1f%%', startangle=90)

                    # Mostrar el gráfico
                    plt.show()
                    
                    input('\nDale enter para continuar ... ')
                    
                        
            else:
                opcion = Validacion.opcion('1. Envios totales\n2. Productos mas enviados\n3. Clientes con envios pendientes\n Seleccione una de las opciones: ', 3)\
                
                if opcion == 1:
                    conteo = self.enviosPorPeriodo()
                    print()
                    for ano, meses in conteo.items():
                        print(f"Año: {ano}:")
                        ventas_totales_ano = 0
                        for mes, dias in meses.items():
                            ventas_totales_mes = 0
                            print(f" Mes: {mes}:")
                            for dia, total in dias.items():
                                ventas_totales_mes += total
                                print(f"   Dia {dia}: {total}$")
                            ventas_totales_ano += ventas_totales_mes
                            print(f"Envios totales por el mes {mes}: {ventas_totales_mes}$")
                        print(f" Pagos totales en el año {ano}: {ventas_totales_ano}$")
                        
                        print()
                        
                        
                    ventas_por_anio = []
                    for year, meses in conteo.items():
                        sales_per_month = []
                        for month, dias in meses.items():
                            sales_per_day = list(dias.values())
                            sales_per_month.append(sales_per_day)
                        ventas_por_anio.append(sales_per_month)

                    # Crear gráfico de barras
                    fig, ax = plt.subplots()
                    ventas_sin_enero = ventas_por_anio[0][0][1:]  # eliminar el primer elemento (correspondiente a enero)
                    ax.bar(range(len(ventas_sin_enero)), ventas_sin_enero, label="")
                    accumulated_sales = list(ventas_por_anio[0][0])
                    for i in range(1, len(ventas_por_anio[0])):
                        accumulated_sales = [x + y for x, y in zip(accumulated_sales, ventas_por_anio[0][i-1])]
                        ax.bar(range(len(ventas_por_anio[0][i])), ventas_por_anio[0][i], bottom=accumulated_sales, label=f"Mes {i+1}")
                    ax.legend()
                    ax.set_xlabel("Días")
                    ax.set_ylabel("Envios")
                    ax.set_title("Envios por mes y día en 2023")
                    plt.show()
                       

                elif opcion == 2:
                    envios = list(filter(lambda x: x.pendiente == False, self.envios))
                    productos_vendidos = {}
                    for envio in envios:
                        for  producto in self.ventas[envio.idCompra - 1].carrito:
                            if producto not in productos_vendidos:
                                productos_vendidos[producto] = 1
                            else:
                                productos_vendidos[producto] += 1
                    productos_mas_repetidos = sorted(productos_vendidos.items(), key=lambda x: x[1], reverse=True)[:3]
                    productos =  [producto[0].nombre for producto in productos_mas_repetidos]
                    print('\nProductos mas enviados: ')
                    for i, producto in enumerate(productos):
                        print(f'{i + 1}. {producto}')
                    
                    cantidad_envios = [producto[1] for producto in productos_mas_repetidos]

                    # Crear un gráfico de barras para mostrar la cantidad de envíos de cada producto
                    plt.bar(productos, cantidad_envios)

                    # Agregar etiquetas y título al gráfico
                    plt.xlabel('Productos')
                    plt.ylabel('Cantidad de envíos')
                    plt.title('Productos más enviados')

                    # Mostrar el gráfico
                    plt.show()
                        
                    input('\nDale enter para continuar ... ')
                    
                else:
                    #Se calculan los clientes con pagos pendientes
                    clientesPendientes = []
                    for envio in self.envios:
                        if envio.pendiente:
                            clientesPendientes.append(envio.cliente)
                    
                    print('\nClientes con envios pendientes: ')
                    nombres = list(set([cliente.nombre for cliente in clientesPendientes]))
                    self.mostrarOpciones(nombres)
                    
                    conteos = {}
                    for nombre in nombres:
                        if nombre in conteos:
                            conteos[nombre] += 1
                        else:
                            conteos[nombre] = 1

                    # Crear un diagrama de barras para mostrar los conteos
                    plt.bar(conteos.keys(), conteos.values())

                    # Agregar etiquetas y título al gráfico
                    plt.xlabel('Nombres de clientes con envíos pendientes')
                    plt.ylabel('Cantidad de clientes')
                    plt.title('Clientes con envíos pendientes')

                    # Mostrar el gráfico
                    plt.show()
                    input('Dale enter para continuar ... \n')
        else:
            print('No hay ninguna venta realizada\n')
            input('Dale enter para continuar... ')

#Funcion que te permite calcular las ventas totales por día, semana, mes y año   
    def ventasPorPeriodo(self):
        conteo = {}
        for venta in self.ventas:
            año = venta.fecha.año
            mes = venta.fecha.mes
            dia = venta.fecha.dia

            if año not in conteo:
                conteo[año] = {}
            if mes not in conteo[año]:
                conteo[año][mes] = {}
            if dia not in conteo[año][mes]:
                conteo[año][mes][dia] = 0

            conteo[año][mes][dia] += venta.total

        return conteo        

#Funcion que te permite calcular los pagos totales por día, semana, mes y año   
    def pagosPorPeriodo(self):
        conteo = {}
        for pago in self.pagos:
            año = pago.fecha.año
            mes = pago.fecha.mes
            dia = pago.fecha.dia

            if año not in conteo:
                conteo[año] = {}
            if mes not in conteo[año]:
                conteo[año][mes] = {}
            if dia not in conteo[año][mes]:
                conteo[año][mes][dia] = 0

            conteo[año][mes][dia] += pago.monto

        return conteo    

#codigo que te permite ver los envios por periodo     
    def enviosPorPeriodo(self):
        conteo = {}
        for envio in self.envios:
            año = envio.fecha.año
            mes = envio.fecha.mes
            dia = envio.fecha.dia

            if año not in conteo:
                conteo[año] = {}
            if mes not in conteo[año]:
                conteo[año][mes] = {}
            if dia not in conteo[año][mes]:
                conteo[año][mes][dia] = 0

            conteo[año][mes][dia] += envio.costo

        return conteo    

        
        
        
#codigo para ver clientes mas vendio para la parte de estadisticas 
    def clienteMasVendido(self):
        conteo = {}
        for venta in self.ventas:
            cliente = venta.cliente.nombre
            if cliente in conteo:
                conteo[cliente] += 1
            else:
                conteo[cliente] = 1
        top_clientes = sorted(conteo, key=conteo.get, reverse=True)[:3]
        return top_clientes

#codigo para ver si el cliente esta pendiete para la parte de estadisticas 
    def clientePendiente(self):
        clientesPendientes = []
        for venta in self.ventas:
            cliente = venta.cliente
            if isinstance(cliente, Juridico):
                if cliente.pendiente:
                    clientesPendientes.append(cliente)
        return clientesPendientes

#Funcion que le pregunta los datos al cliete 
    def registrarCliente(self):
        print('\nAGREGAR CLIENTE')
        nombre = Validacion.string('Ingrese su nombre: ')
        cedula = Validacion.cedula('Ingrese su cedula: ')
        correo = Validacion.correo('Ingrese su correo: ')
        direccion = Validacion.string('Ingrese su direccion: ')
        telefono = Validacion.telefono('Ingrese su telefono: ')
        print('\n1. Cliente Natural\n2. Cliente Juridico')
        seleccion = Validacion.opcion('Seleccion el tipo de cliente (1-2): ', 2)
        if seleccion == 1:
            cliente = Natural(nombre, cedula, correo, direccion, telefono, True)
        else:
            cliente = Juridico(nombre, cedula, correo, direccion, telefono, True)
        
        return cliente
   
#funcion que revisa que envio esta pendiete para la parte de estadisticas 
    def envioPendiente(self):
        EnvioPendientes = []
        for envio in self.envios:
            cliente = envio.cliente
            if isinstance(cliente, Juridico):
                if cliente.pendiente:
                    clientesPendientes.append(cliente)
        return clientesPendientes
   
   
   
# Funcion que te permite registrar el Pago 
    def registrarPago(self, cliente, monto,fecha):
        print('\nMONEDA DE PAGO:\n 1. Dolares \n 2. Bolivares')
        seleccion = Validacion.opcion('Seleccione la moneda con la que desaa pagar: ', 2)
        if seleccion == 1:
            moneda = 'Dolares'
        else:
            moneda = 'Bolivares'
        print('\nTIPO DE PAGO:\n 1. Zelle \n 2. Efectivo\n 3. PM')
        seleccion = Validacion.opcion('Seleccione la el tipo de pago: ',3)
        if seleccion == 1:
            tipo = 'Zelle'
        elif seleccion == 2:
            tipo = 'Efectivo'
        else: 
            tipo = 'PM'
            
        return Pago(cliente, monto, moneda, tipo, fecha)
        
#funcion que te permite registrar el envio
    def registrarEnvio(self, fecha, idCompra, cliente):
        orden = idCompra
        motorizado = '-----'
        seleccion = Validacion.opcion('\nServicio de Envio:\n1. MRW \n2. Zoom \n3. Delivery\nSeleccione el servicio de envio: ',3)
        if seleccion == 1:
            servicio = 'MRW'
        elif seleccion == 2:
            servicio = 'Zoom'
        else: 
            servicio = 'Delivery'
            motorizado = Validacion.string('\nIngrese el nombre de motorizado: ')
        
        costo = Validacion.numero('\nIngrese el costo del servicio: ')
        envio = Envio(orden, servicio, motorizado, costo, fecha, cliente)
        seleccion = Validacion.escogencia('\nEl envio fue realizado (s/n): ')
        if seleccion == "n":
            envio.pendiente = True
        
        return envio
             
#Funcion para reducir el inventario
    def controlInvetario(self, venta):
        productosFiltrados = list(filter(lambda x: x.disponible, self.productos))

        #  Se hizo una copia para ahora, poder restarle a a original lo que se compro
        #Actualizar el stock
        for p in venta.carrito:
            for producto in productosFiltrados:
                if p.nombre == producto.nombre:
                    producto.inventario -= p.cantidad
                    break
    
#Funcion para agregar fecha 
    def agregarFecha(self):
        print('AGREGAR FECHA: ')
        dia = Validacion.dia('Ingrese el dia: ')
        mes = Validacion.mes('Ingrese el mes: ')
        año = Validacion.año('Ingrese el año: ')
        fecha = Fecha(dia, mes, año) 
        return fecha
       
#Funcion para realizar la venta
    def realizarVenta(self):
        fecha = self. agregarFecha()
        print('\n')
        cliente_registrado = False
        cedula = Validacion.cedula('Ingrese su numero de cedula: ')
        for c in self.clientes:
            if c.cedula == cedula:
                cliente_registrado = True
                cliente = c
                break
        
        if not cliente_registrado:
            print("\nCliente no registrado")
            cliente = self.registrarCliente()
            
        respuesta = 's'
        carrito = []  #El carrito donde se podran poner los producos que se desean llevar
        
        #Lista para tener en cuenta los productos que estan disponibles
        productosFiltrados = list(filter(lambda x: x.disponible, self.productos))  
        productos_copia = copy.deepcopy(productosFiltrados) #Mientras el elige poder ir restando la cantidad que adquiere el cliente
            
        while respuesta == 's':
            print('------------ PRODUCTOS ------------')
            
            self.mostrarInfoObjeto(productos_copia)

            respuesta = Validacion.opcion('Seleccione un producto: ', len(productos_copia))

            producto = productos_copia[respuesta - 1] #copia de copia
                
            if producto.inventario != 0:
                    
                aux = copy.deepcopy(producto) #Se hace una copia, para poder modificar los valores (datos), y que los datos inciales no sean modificados
                    
                
                aux.cantidad = Validacion.numero(f'Ingrese la cantidad que desea comprar (max.{producto.inventario}): ') #Verificar la cantidad
                while aux.cantidad > producto.inventario:
                    aux.cantidad = Validacion.numero(f'Error! no hay disponible esa cantidad\n Ingrese de nuevo la cantidad que desea comprar (max.{producto.inventario}): ') 
                
                productos_copia[respuesta - 1].inventario -= aux.cantidad  #restarle al producto de la lista copia la cantidad adquirida po el cliente

                carrito.append(aux)
                
            else:
                print()
                print('Producto Agotado')
                print('----------------')
                
            
            respuesta = Validacion.escogencia('Desea seleccionar otro producto (s/n): ')
        
    
        
        venta = Venta(cliente, carrito, fecha)
        venta.obtenerPrecio()
        pagar = False
        realizar = ''
        venta_realizada = False
        if venta.total != 0: #Esto es por si no seleccionaron nada de los productos
            print()
            print(venta.previo())
            if isinstance(cliente, Juridico):           
                seleccion = Validacion.escogencia('Desea realizar el pago a credito (s/n): ')
                if seleccion == 's':
                    venta.cliente.pendiente = True 
                    envio = self.registrarEnvio(fecha, len(self.ventas), cliente)
                    venta.metodoEnvio = envio.servicio
                    venta.obtenerPrecio()
                    print(venta.mostrar())
                    self.ventas.append(venta)   #se guardan los recivos en la lista 
                    self.controlInvetario(venta)
                    self.clientes.append(venta.cliente)
                    self.envios.append(envio)
                    print()
                    print('La venta ha sido registrada exitosamente!')
                    print('------------------------')
                    venta_realizada = True
                else:
                    eleccion = Validacion.escogencia('Desea realizar el pago (s/n): ')
                    if eleccion == 's':
                       pagar = True; 
            else:
                realizar = Validacion.escogencia('Desea realizar la compra (s/n): ')
                

            if realizar == 's' or pagar:
                pago = self.registrarPago(cliente, venta.total, fecha)                 
                envio = self.registrarEnvio(pago.fecha, len(self.ventas) + 1, cliente)
                venta.metodoPago = pago.moneda
                venta.metodoEnvio = envio.servicio
                venta.obtenerPrecio()
                print(venta.mostrar())
                self.ventas.append(venta)   #se guardan los recivos en la lista 
                self.controlInvetario(venta)
                self.pagos.append(pago)
                self.envios.append(envio)
                self.clientes.append(cliente)
                print()
                print('La venta ha sido registrada exitosamente!')
                print('------------------------')
            else:
                if not venta_realizada:
                    print()
                    print('No se realizo la venta')
                    print('------------------------')
                                
            print()
        else:
            print()
            print('No llevo ningun producto')
            print('------------------------')

            
# Funcion de donde se hace toda la logica
    def comienzo(self):
        res = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/e20c412e7e1dcc3b089b0594b5a42f30ac15e49b/products.json')
        info = res.json() #Se toma el diccionario (json) de la Api
        self.agregarProductos(info)
        self.extraerInfo()
        print("--------------------------------------------------")
        print("  BIENVENIDO A LA TIENDA DE PRODUCTOS NATURALES  ")
        print("--------------------------------------------------")

        while True: 
            print("                      MENU                        ")
            print("--------------------------------------------------")

            menu = Validacion.opcion(" 1. Gestión de productos\n 2. Gestión de ventas\n 3. Gestión de clientes\n 4. Gestión de pagos\n 5. Gestión de envíos\n 6. Indicadores de gestión (estadísticas)\n 7. Salir\n Seleccione una de las opciones: ", 7)  

            if menu == 1:
                print("--------------------------------------")
                print("         Gestión de productos         ")
                print("--------------------------------------")
                
                seleccion = Validacion.opcion(" 1. Buscar Producto \n 2. Modificar Productos \n 3. Eliminar Productos\n 4. Salir\n\n Seleccione una de las opciones: ", 4)
                if seleccion == 1:
                    self.buscarProductos()
                elif seleccion == 2: 
                    self.modificarProducto()

                elif seleccion == 3:
                    self.eliminarProducto()
                else:
                    print('\n')
                
            elif menu == 2:
                print("-----------------------------------")
                print("         Gestión de Ventas         ")
                print("-----------------------------------")

                seleccion = Validacion.opcion(" 1. Realizar Venta\n 2. Buscar Ventas \n 3. Salir \n Seleccione una de las opciones: ", 3)
                
                if seleccion == 1:
                   self.realizarVenta()
                elif seleccion == 2: 
                    self.buscarVentas()
                else: 
                    print('\n')


            elif menu == 3:
                print("-------------------------------------")
                print("         Gestión de Clientes         ")
                print("-------------------------------------")

                seleccion = Validacion.opcion(" 1. Modificar Información Cliente\n 2. Eliminar Cliente \n 3. Buscar Cliente\n 4. Salir\n Seleccione una de las opciones: ", 4)
                
                if seleccion == 1:
                    self.modificarCliente()
                elif seleccion == 2: 
                    self.eliminarCliente()
                elif seleccion == 3: 
                    self.buscarClientes()
                else: 
                    print('\n')
                    
            elif menu == 4:
                print("----------------------------------")
                print("         Gestión de Pagos         ")
                print("----------------------------------")

                seleccion = Validacion.opcion(" 1. Buscar Pago\n 2. Salir\n\n Seleccione una de las opciones: ", 2)
                
                if seleccion == 1:
                    self.buscarPago()
                else: 
                    print('\n')

            elif menu == 5: 
                print("-----------------------------------")
                print("         Gestión de Envíos         ")
                print("-----------------------------------")

                seleccion = Validacion.opcion(" 1. Buscar Envío\n 2. Salir\n\n Seleccione una de las opciones: ", 2)
                
                if seleccion == 1:
                    self.buscarEnvios()
                else: 
                    print('\n')

            elif menu == 6:
                print("---------------------------------------")
                print("        Indicadores de gestión         ")
                print("---------------------------------------")
                self.estdisticas()
                
            else:
                print("------------------------------------------")
                print("Gracias por visitarnos .¡Hasta la próxima!")
                print("------------------------------------------")
                self.guardar_info()
                break