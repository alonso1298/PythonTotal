dic = {'calve1':100,'Clave2':500}

#Si queremos aplicar algun metodo al diccionario es invocando a esa instancia del objeto seguido de un punto
a = dic.popitem()
print(a)
print(dic)

print('\n---------------------\n')

#El método lstrip() en Python se utiliza para eliminar los caracteres de espacio en blanco (como espacios en blanco, tabulaciones, saltos de línea, etc.)
cadena = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

cadena_nueva = cadena.lstrip(',:_#,,,,,,:::____##')

print(cadena_nueva)

print('\n---------------------\n')

#El método insert() en Python se utiliza para insertar un elemento en una lista en una posición específica. Toma dos argumentos: el índice donde se insertará el elemento y el elemento mismo que se insertará.
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 

frutas.insert(4,'naranja')

print(frutas)

print('\n---------------------\n')

#El método isdisjoint() en Python se utiliza para verificar si dos conjuntos (sets) no tienen elementos en común. Devuelve True si los conjuntos no tienen elementos comunes y False si tienen al menos un elemento en común.
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)