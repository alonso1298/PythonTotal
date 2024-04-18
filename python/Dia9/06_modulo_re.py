'''
Una expresión regular es una secuencia de caracteres que
forman un patrón de búsqueda determinado. Pueden ser
utilizadas para verificar strings en búsqueda de un contenido
(patrón) específico. Utilizamos el módulo re en Python.
'''

import re

texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'

#Para buscar una palabra lo haciamos de esta manera
palabra = 'ayuda' in texto
print(palabra)

print('\n---------------------\n')

patron = 'ayuda'
busqueda = re.search(patron, texto)
print(busqueda)
#Este nos muestra solo la ubicacion
print(busqueda.span())
#Nos muestra desde donde inicia la palabra 
print(busqueda.start())
#Nos muestra desde donde termina la palabra 
print(busqueda.end())

print('\n---------------------\n')

#Como tenemos 2 palabras 'ayuda' si quiero encontrar mas de una es con find all 
busqueda2 = re.findall(patron, texto)
#Nos arroja una lista con todas las palabra que encontro
print(busqueda2)

print('\n---------------------\n')

#Si queremos saber las ubicaciones de los 2 elementos tenemos que iterar con finiter
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())


print('\n-----------------------------------\n')


enunciado = 'llama al 564-525-6588 ya mismo'

#Ahora el patron sera una seri de caracteres separados por un guion
patron2 = r'\d{3}-\d{3}-\d{4}'

#A la busqueda le pasamos el patron, seguido del texto donde se va a buscar
resultado = re.search(patron2, enunciado)
print(resultado)
#Si le pasamos el metodo group este nos dara solo el numero encontrado
print(resultado.group())

#Tambien podemos compilarlos 
patron3 = (r'(\d{3})-(\d{3})-(\d{4})')

resultado2 = re.search(patron3, enunciado)
#Nos muestra el segundo elemento del grupo
#NOTA* los indices de busqueda inician desde el uno 
print(resultado2.group(2))

print('\n---------------------\n')

'''
Esto tiene varios usos practicos por ejemplo si un usuario quiere generar una clave 
y queremos controlar que cumpla con algunas condiciones.
Que enpiece con una letra y que en total tenga 8 caracteres
'''

clave = input('Clave: ')

patron4 = r"\D{1}\w{7}"

chequear = re.search(patron4, clave)

print(chequear)

print('\n---------------------\n')

#Tambien tenemos operadores especiales 

info = 'No atendemos los lunes por la tarde'

#Con el caracter | podemos buscar si esta una palabra u otra diferente dentro del texto
#Esto se puede usar para buscar plurales y singulares
buscar = re.search(r'lunes|martes', info)
print(buscar)
#Tambien tenemos comodines como el punto (.) si las ponemos antes o despues este nos traera el texto
buscar2 = re.search(r'....demos.....', info)
print(buscar2)

#Este comodin ^ nos permite verificar el primer caracter, en este caso le estamos preguntando si el primer caracter no es un digito
buscar3 = re.search(r'^\D', info)
print(buscar3)

#Este comodin $ nos permite verificar el ultimo caracter, en este caso le estamos preguntando si el ultimo caracter no es un digito
buscar4 = re.search(r'\D$', info)
print(buscar4)

print('\n---------------------\n')

#Con la serie de caracteres [^] va a encontrar todos los que excluyan un espacio vacio 
buscar5 = re.findall(r'[^\s]', info)
print(buscar5)

#Si le agregamos el signo + lo va a buscar todas las veces que existan y los va a construir en una lista de palabras
buscar5 = re.findall(r'[^\s]+', info)
print(buscar5)


print('\n---------------------\n')

'''
Crea una función llamada verificar_email para comprobar si una dirección de email es correcta, 
que verifique si el email dado como argumento contiene "@" 
(entre el nombre de usuario y el dominio) y finaliza en ".com" 
(aunque aceptando también casos que cuentan con un dominio adicional, 
tal como ".com.br" para el caso de un usuario de Brasil).

Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok", 
pero si detecta que la frase no contiene los elementos indicados, 
debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el mensaje.
'''

def verificar_email(email):
    patron6 = r'^[a-z A-Z 0-9 ]+@[a-z A-Z 0-9 .-]+\.[a-zA-Z]{2,}$'
    
    if re.match(patron6, email):
        print('ok')
    else:
        print('La dirección de email es incorrecta')
        
verificar_email("usuario@host.com")

print('\n---------------------\n')

'''
Crea una función llamada verificar_saludo para verificar si una frase entregada como argumento inicia con la palabra "Hola". 
Si se encuentra el patrón, la función debe finalizar mostrando el mensaje "Ok", 
pero si detecta que la frase no contiene "Hola", 
debe informarle al usuario "No has saludado" imprimiendo el mensaje en pantalla.
'''

def verificar_saludo(frase):
    patron7 = r'^Hola\s\w+'
    
    if re.match(patron7, frase):
        print('ok')
    else:
        print('No has saludado')

verificar_saludo('Hola como estas')


print('\n---------------------\n')

'''
El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y cuatro numéricos 
a continuación (ejemplo: XX1234). Crea una función, 
llamada verificar_cp para comprobar si el código postal pasado como argumento sigue este patrón. 
Si el patrón es correcto, mostrar al usuario el mensaje "Ok", 
de lo contrario: "El código postal ingresado no es correcto".
'''

def verificar_cp(cp):
    
    patron = r'\w{2}\d{4}'
    
    if re.match(patron, cp):
        print("Ok")
        
    else:
        print("El código postal ingresado no es correcto")