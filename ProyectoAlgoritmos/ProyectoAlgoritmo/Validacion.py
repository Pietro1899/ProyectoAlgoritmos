import re
class Validacion:

#Para elegir opcion en un menu
    def opcion(mensaje, rango):  
        #Para que la persona elija alguna opcion y verficar que no salga algun error
        while True:
            try:
                option = int(input(mensaje))
                if option not in range(1, rango + 1):
                    raise Exception
            except ValueError:
                print("Error!. Verifique que ingreso un numero")
                
            except:  
                print("Error!. Ingrese un numero que se encuentre dentro de las opciones")
            else:
                return option

#Funcion que te permite validar si el correro esta bien escrito 
    def correo(mensaje):
        while True:
            patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            try:
                correo = input(mensaje)
                if not re.match(patron, correo):
                    raise ValueError('Error! Correo electrónico inválido.')
            except ValueError as e:
                print(e)
            else:
                return correo
        
    #Verificar la cedula  
    def cedula(message): 
        while True:
            try:
                dni = input(message)
                if not dni.isnumeric():
                    raise Exception
                
                if len(dni) <= 0 or dni == 0:
                    raise Exception
            except:
                print('Error!. Verifique los datos')
            else:
                return int(dni)

#Funcion qu epermite verificr si lgun datos solo tiene caracteres y no numeros           
    def string(message):  
        while True:
            try:
                string = input(message).lower()
                check_string = string.replace(' ', '')  #quitarle el espacio por si lo hay, para ver los caracteres 
                
                if not check_string.isalpha():
                    raise Exception
            except: 
                print('Error!. Verifique los datos')
            else:
                return string.capitalize()
            
            
#Permite validar un numero cualquiera
    def numero(message):
        while True:
            try:
                info = int(input(message))
                if info == 0:
                    raise Exception
            except ValueError:
                print('Error!. Verifique que escribio un numero')
            except:
                print('Error!. Ingrese un numero distinto de 0')
            else:
                return info
            
#Validacion que asegura que el usuario escogio Si o No
    def escogencia(message):
        while True:
                try:
                    selection = input(message).lower()
                    
                    if not selection.isalpha() or not selection in 'sn':
                        raise Exception
                except:
                    print('Error en los datos! escriba una S (Si) o una N(No)')
                
                else:
                    return selection
    
#funcion para verificar el año
    def año(message):
        while True:
            try:
                info = int(input(message))
                if info == 0 or info < 2023:
                    raise Exception
            except ValueError:
                print('Error!. Verifique los datos')
            except:
                print('Error!. Ingrese el ano a partir de 2023')
            else:
                return info      

#funcion que verifica el mes
    def mes(message):
        while True:
            try:
                info = int(input(message))
                if info == 0 or info > 12 or info<1:
                    raise Exception
            except ValueError:
                print('Error!. Verifique los datos')
            except:
                print('Error!. Ingrese un numero del mes')
            else:
                return info     
            
#funcion que verifica el dia
    def dia(message):
        while True:
            try:
                info = int(input(message))
                if info == 0 or info > 31 or info  < 1:
                    raise Exception
            except ValueError:
                print('Error!. Verifique los datos')
            except:
                print('Error!. Ingrese un numero del dia')
            else:
                return info     
            
            
#Funcion que valida el telefono
    def telefono(message):
        while True:
            try:
                info = input(message)
                if not info.isnumeric() or len(info) != 11:
                    raise Exception
            except:
                print('Error!. Ingrese el telefono con 11 caracteres y que todos sean numeros')
            else:
                return info     