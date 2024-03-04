#Verificaremos si 10 > 9 
if 10 > 9:
    print('Es correcto')

#Tambien se pueden ingresar variables
x = True 

if x:
    print('Es correcto')

#Si la condicion no se cumple no se va a ejecutar nada 
if 2 == 5:
    print('Es correcto')

print('--------------------------')

#Si queremos hacer que algo suceda cuando no se cumpla la condicion agregamos un else
if 2 == 5:
    print('Es correcto')
else:
    print('No es correcto')

print('--------------------------')

#Para hacer varias preguntas es con elif
mascota = 'perro'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
else:
    print('No se que animal tienes')

print('--------------------------')

#Se pueden anidar las condiciones if
edad = 16
calificacion =  9

if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else: 
        print('No aprobado')
else:
    print('Eres mayor de edad')

print('--------------------------')

habla_ingles = True
sabe_python = False

if sabe_python == True and habla_ingles == True:
    print("Cumples con los requisitos para postularte")
    if sabe_python == False and habla_ingles == False:
        print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif habla_ingles == False:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif sabe_python == False:
    print("Para postularte, necesitas saber programar en Python")
