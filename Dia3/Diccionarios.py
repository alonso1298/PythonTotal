diccionario = {'c1':'valor1', 'c2':'valor2'}
#En los diccionarios no se puede repetir la clave
print(diccionario)

#Las busquedas se hacen con el valor de la clave
resultado = diccionario['c1']
print(resultado)

print('---------------------')

#Los diccionarios pueden contener diferentes tipos de datos y diccionarios dentro del diccionario
cliente = {'nombre':'Alonso', 'apellido':'Sagrero', 'peso':80, 'talla':1.70}
consulta = cliente['apellido']
print(consulta)

print('---------------------')

dic = {'c1':55, 'c2':[10, 20, 30], 'c3':{'s1':100, 's2':200}}
#Para consultar valores de un lista dentro de un diccionario consultamos primero la clave y porteriormente el indice del otro diccionario
print(dic['c2'][1])
#Si agregamos solo la clave del diccionario, este nos muesta el diccionario completo
print(dic['c3']['s2'])
#Si queremos consultar el valor de un diccionario que esta dentro de otro, podemos ingresar la clave del diccionario, posterior a la clave dentro del diccionario

print('---------------------')

dic2 = {'c1':['a', 'b', 'c'], 'c2':['d', 'e', 'f']}
print(dic2['c2'][1].upper())
#Se pueden agregar los metodos prpios de los str en los diccionarios que lo contienen

print('---------------------')

dic3 = {1:'a', 2:'b'}
print(dic3)
#Para agregar elementos a un diccionario que ya a sido creado se llama al diccionario luego se agrega la clave y el valor se agregara despues del = 
dic3[3] = 'c'
print(dic3)

print('---------------------')

#Para sobreescribir un valor de un diccionario es llamando la clave donde queremos sobreescribir y le asignamos el nuevo valor 
dic3[2] = 'B'
print(dic3)

print('---------------------')

print(dic3.keys())
#Con keys conocemos todas las claves del diccionario
print(dic3.values())
#Con values solo conocemos los valores del diccionario
print(dic3.items)
#Con items conocemos todos los valores del diccionario