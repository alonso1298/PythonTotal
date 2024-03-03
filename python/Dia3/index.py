mi_texto = "Esta es una prueba"
#Imprime lo que hay en el indice que requerimos
resultado = mi_texto[9]
print(resultado)

mi_texto = "Esta es una prueba"
#Tambien se puede con numeros negativos 
resultado = mi_texto[-4]
print(resultado)

print('------------------')

mi_texto = "Esta es una prueba"
#Index tiene 3 parametros posibles. 1- Caracter, 2-(opcional) de donde y hasta donde buscar 
resultado = mi_texto.index("n")
#Nos muestra en que indice esta la letra
print(resultado)

mi_texto = "Esta es una prueba"
#Tambien podemos buscar palabras enteras
#Nota* Es sensible a Mayusculas y minusculas
resultado = mi_texto.index("prueba")
#Nos muestra en que indice comienza la palabra
print(resultado)

print('------------------')

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a", 5)
#Cuando busquemos un indice que se repita siempre va a buscar el primero y nos dara el resultado
#Al poner coma y un indice, este va a buscar a partir del indice que le pongamos
print(resultado)

print('------------------')

mi_texto = "Esta es una prueba"
#El metodo rindex busca desde el ultimo caracter hasta el primero o de derecha a izquierda
resultado = mi_texto.rindex("a", 5)
#Devuelve el resultado con el indice que va de izquierda a derecha
print(resultado)