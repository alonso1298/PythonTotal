var1 = True
var2 = False
print(type(var1))
print(var1)

print('------------------------')

#Los bool tambien se pueden representar con comparaciones de numeros
numero = 5 > 2+3
print(type(numero))
print(numero)

#Tambien se puede representar mas explicito creando la funcion bool y poner la expresion
numero2 = bool( 5 < 6 )
print(type(numero2))
print(numero2)

print('------------------------')

#Tambien nos regresa un valor bool cuando consultemos si un elemento esta en una lista
lista = [1, 2, 3, 4]
control = 5 in lista
print(type(control))
print(control)