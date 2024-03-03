texto = 'Este es el texto de Alonso'
resultado = texto
print(resultado)

print('-----------------')

texto = 'Este es el texto de Alonso'
#Transforma todas las letras en mayusculas
resultado = texto.upper()
print(resultado)

texto = 'Este es el texto de Alonso'
#Tambien lo podemos hacer con indices en particular
resultado = texto[2].upper()
#Le estamos diciendo que el resultado sera igual al indice 2 
print(resultado)
#Solo imprime la T 

print('-----------------')

texto = 'Este es el texto de Alonso'
#Transforma todas las letras en minusculas
resultado = texto.lower()
print(resultado)

print('-----------------')

texto = 'Este es el texto de Alonso'
#Separa los elementos y los guarda dentro de una lista
#Separa los elementos conforme a los espacios de la cadena
resultado = texto.split()
print(resultado)

texto = 'Este es el texto de Alonso'
#Si le pasamos el parametro "t" este separara conforme a t
resultado = texto.split('t')
#Separara todos los elementos tomando a 't' como separador
print(resultado)

print('-----------------')

a = 'Aprender'
b = 'Python'
c = 'es'
d = 'genial'
#Al aplicarle el metodo join va a tomar todos lo elementos que incluyamos dentro del parentesis y lo separara con un espacio 
e = " ".join([a, b, c, d])
#Creamos un lista con los elementos  
print(e)

print('-----------------')

texto = 'Este es el texto de Alonso'
#Este busca un determinado caracter dentro del String
resultado = texto.find('s')
#Nos muestra el indice donde se encuentra ese caracter
print(resultado)
#La diferencia con index es que si se busca un caracter que no existe arroja el valor -1 

print('-----------------')

texto = 'Este es el texto de Alonso'
#Este metodo remplaza un fragmento del texto y lo reemplaza por otro
resultado = texto.replace('Alonso', "Todos")
#El el primer parametro ingresamos el texto que queremos eliminar y en el segundo el texto a remplazar 
print(resultado)

#Para reemplazar 2 o mas palabras

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

print(frase.replace('difícil', 'fácil').replace('mala', 'buena'))