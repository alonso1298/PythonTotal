from random import *

print('Bienvenido a adivina el numero!!')

nombre = input('Cual es tu nombre?: ')
print(f'Bienvenido {nombre} comenzaremos el juego.')

num_intentos = 8
print(f'Recuerda que solo tienes {num_intentos} intentos')

numero = 0
num_aleatorio = randint(1,100)

while numero != num_aleatorio:
    numero = int(input(f'Piensa un numero entre el 1 y el 100: '))
    num_intentos -= 1
    print(f'Solo te quedan {num_intentos} intentos')
    if numero > num_aleatorio:
        print('El numero es mas pequeño')
    elif numero < num_aleatorio:
        print('El numero es mas grande')
    elif numero == num_aleatorio:
        break
    elif num_intentos < 0:
        print(f'Has alcanzado en numero de intentos, fallaste el numero era {num_aleatorio}')
        break
else:
    ('Ingresa un numero valido')

print(f'Muchas felicidades adivinaste el numero en {8 - num_intentos} intentos')