# Con el metodo min podemos el minimo valor de una lista, o cualquier otro iterable
menor = min(58,96,72,64,35) #Podemos almacenar en una variable el valor menor
mayor = max(58,96,72,64,35)

print(menor)
print(mayor)

print('\n-------------------------\n')

#Tambien podemos trabajar con listas
lista = [58,96,72,64,35]

print(max(lista))
print(min(lista))
print(f'El menor es {min(lista)} y el mayor es {max(lista)}')

print('\n-------------------------\n')

#Tambien podemos trabajar con Stings 
nombres = ['Juan', 'Pablo', 'Alicia', 'Carlos']

print(min(nombres)) #Esto nos imprime el primer lugar en orden alfabetico 

print('\n-------------------------\n')

nombre = 'Carlos'

#Esto va a imprimir 'C' ya que primero busca en las letras mayuscular y luego en las minusculas
print(min(nombre)) 

#Para imprimir sin errores podemos usar el metodo Lower
print(min(nombre.lower()))

print('\n-------------------------\n')

#Tambien podemos trabajar con Diccionarios 
dic = {'C1':45, 'C2':11}

#Esto nos va a imprimir la clave que tenga el valor inferior 'C1'
print(min(dic))

#Si yo quiero el valor y no la clave puedo usar el metodo .values
print(min(dic.values()))