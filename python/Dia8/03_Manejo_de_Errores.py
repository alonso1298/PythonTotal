'''
Existen estrategias para capturar y gestionar los errores que
pueden presentarse al ejecutar un programa, a fines de evitar
una falla mayor y controlar la información que es mostrada al
usuario.
'''
#Si el usuario pone alguna letra esta funcion nos arrojara un error
def suma():
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    print(n1 + n2)
    print('Gracias por sumar' + n1)
   
# Para programas donde depende el usuario haga lo correcto manejar de alguna forma la posibilidad de que suceda un error  
# suma()


# #Usaremos la estructura de try, except, finally
# try: 
#     # Codigo que queremos probar
#     suma()
# except:
#     # Codigo a ejecutar si hay un error
#     print('Algo no a salido bien')
# else:
#     # Codigo a ejecutar si no hay error 
#     print('Hiciste todo bien')
# finally:
#     # Codigo que se va a ejecutar de todos modos cometa el error o no 
#     print('Eso fue todo')
    
    
# Tambien se pueden manejar distintas tipos de excepciones ya sea ValueError, TypeError, etc.
try: 
    suma()
#Le pasamos el tipo de error con el cual hara la accion
except TypeError:
    print('Estas intentando concatenar tipos distintos')
#Los errores se agregan con otro except
except ValueError:
    print('Ese no es un nuemero')
else:
    print('Hiciste todo bien')
finally:
    print('Eso fue todo')

print('\n---------------------\n')

#Nos podemos preparar para que un usuario ingrese un numero como se lo pedimos
def pedir_numero():
    
    while True:
        # Va a intentar ver si numero es igual al integer de un input que ingrese el ususario 
        try: 
            numero = int(input('Dame un numero: '))
        # Si el dato que ingreso el usuario no es un numero imprimira que no es un numero
        except:
            print('Ese no es un numero')
        #En el caso de que ingresara un numero este se muestra y termina el ciclo
        else:
            print(f'Ingresaste el numero {numero}')
            break
         
    print('gracias')

pedir_numero()