#Necesitaremos en algun punto que la consola se limpie sin salir del programa 
from os import system

nombre = input('Dime tu nombre: ')
edad = input('Dime tu edad: ')

#Anadimos el comando para limpiar la terminal que en caso de Windows es 'cls' en otros sistemas es 'clear'
system('cls')

print(f'Tu nombre es {nombre} y tienes {edad} a~os')