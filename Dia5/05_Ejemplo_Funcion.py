precios_cafe = [('Cappucino', 1.5),('Expresso',1.2),('Moca',1.9)]

for elemento in precios_cafe:
    print(elemento)

print('\n---------------------\n')

#Si queremos que nos de las 2 por separado agregamos 2 variables
for cafe,precio in precios_cafe:
    print(cafe)

print('\n---------------------\n')

#Si yo quiero conocer cual es el cafe mas caro crearemos un sistema que pase por cada uno de los elementos y retenga el que tiene el precio mayor 

def cafe_mas_caro(lista_precios):

    precio_mayor = 0 #Inicializamos el precio mayor en 0 
    cafe_mas_caro = '' #eEste se va a inicializar con un string vacio 

    for cafe,precio in lista_precios: #Este for va a pasar por cafe y precio en la lista dada
        if precio > precio_mayor: #Se va a fijar si el precio es mayor a lo que sea que este en precio mayor, si es asi 
            precio_mayor = precio #Se sobre escribe el precio mayor con el contenido de precio
            cafe_mas_caro = cafe #Luego tambien va a sobre escribir el de cafe mas caro con el valor que hay en cafe
        else:
            pass 

    return(cafe_mas_caro,precio_mayor)#Queremos que nos devuelva el nombre y el precio del cafe mas caro

print(cafe_mas_caro(precios_cafe)) #Esto nos devuelve la tupla con el cafe mas caro

#Si queremos guardar en dos variables el resultado, creamos dos variables y las igualamos al resultado de la funcion 
cafe, precio = cafe_mas_caro(precios_cafe)
print(f'El cafe mas caro es {cafe}, cuyo precio es {precio}')



