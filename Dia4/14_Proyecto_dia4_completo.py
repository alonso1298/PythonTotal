from random import randint

intentos = 0
numero_secreto = randint(1,100)

nombre = input('Dime tu nombre: ')

print(f'Bueno {nombre} eh pensado un numero entre 1 y 100 \n Tienes 8 intentos para adivinar.')

while intentos < 8:
    estimado = int(input('Cual es el numero?: '))
    intentos += 1
    
    if estimado not in range(1,101):
        print('Tu numero no se encuentra en el rango de 1 al 100')
    if estimado < numero_secreto:
        print('Mi numero es mas alto')
    elif estimado > numero_secreto:
        print('Mi numero es mas bajo')
    else: 
        print(f'Felicitaciones {nombre}! Has adivinado en {intentos} intentos.')
        break

if estimado != numero_secreto:
    print(f'Lo siento se han agotado los intentos. El numero secreto era {numero_secreto}')