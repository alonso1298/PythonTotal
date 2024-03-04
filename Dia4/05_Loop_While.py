#Tenamos que tener ya que podemos ejecutar un loop while infinitamente y eso provocara grandes erroes
#monedas = 5
#Este codigo es un loop Infinito 
#while monedas > 0:
#    print(f"Tengo {monedas} monedas")

monedas = 5
#Para salir del loop infinito tendremos una linea que modifique la cantidad de monedas
while monedas > 0:
    print(f"Tengo {monedas} monedas")
#E cada loop perdemos una moneda
    #monedas = monedas - 1 
#Otra forma de escribir esta ultima linea es poninedo -= esto significa que es igual a la cantidad que tengo - 1
    monedas -= 1
#Tambien se pueden colocar bloque else
else: 
    print('No tengo mas dinero')

print('-------------------------')

respuesta = 's'
#En este loop no podemos tener un control de este ya que el usuario puede continuar o no 
while respuesta == 's':
    respuesta = input('Quieres seguir? s/n: ')
else:
    print('Gracias')

print('------------pass-------------')

respuesta2 = 's'
#La palabra pass significa pasar o sea que no hace nada
"""while respuesta2 == 's':
    pass    #pass se encarga de guardar el lugar para poder ejecutar el codigo

print('Hola')"""

print('------------brake-------------')

#Brake lo que hace es interrumpir el loop en el que estamos y salir de este
nombre = input('Tu nombre: ')

for letra in nombre:
    if letra == 'r':
        break
    print(letra)
#Si yo quiero que el programa se interrumpa cuendo se encuentre con alguna letra utilizamos brake
    
print('------------continue-------------')

#Continue este interrumpe la iteracion con la condicion dada y despues continua con las demas iteraciones
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)

print('-------------------------')

"""Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:

- Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)

- Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente)."""

numero = 50

print(numero)#Primero se imprime el numero 50 ya que al entrar al loop este no se va a imprimir
while numero >= 0:
    numero -= 1 #Aqui hacemos la resta de los numero de uno en uno
    if numero % 5 == 0: #Verificamos si el numero es divisible por 5
        print(numero) #Si lo es entonces se imprime el numero
    else:
        continue #Si no el ciclo contunua exeptuando lo numeros que no son divisibles entre 5 

print('-------------------------')

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for i in lista_numeros:
    if i < 0:
        break
    print(i)