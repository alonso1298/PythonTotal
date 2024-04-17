'''
El módulo datetime (incorporado en Python) puede importarse en
proyectos para trabajar con fechas y horas, así como intervalos y
duraciones.

'''
import datetime

#En una varible guardamos la hora pasandole el parametro de hora y minutos, esto en formato de 24hrs.
mi_hora = datetime.time(17, 35)
print(mi_hora)
#Podemos ir aislando los valores para poderlos ir manipulando si queremos
print(mi_hora.minute)

print('\n---------------------\n')

#Tambien podemos trabajar con fechas
mi_dia = datetime.date(2024, 10, 17)
print(mi_dia)
#Tmbien permite aislar la informacion
print(mi_dia.year)

#Esto muestra la fecha actual
print(mi_dia.today())

print('\n---------------------\n')

from datetime import datetime, date

#Si queremos mostrar la fecha y el dia 
mi_fecha = datetime(2024, 5, 22, 10, 15, 18, 1500)
print(mi_fecha)

#Podemos reeplazar los datos
mi_fecha = mi_fecha.replace(month = 12)
print(mi_fecha)

#Tambien podemos calcular tiempos que transcurren de un tiempo a otro ya sea fechas u horas
nacimiento = date(1967, 11, 21)
defuncion = date(2020, 12, 31)

vida = defuncion - nacimiento

print(vida)


print('\n---------------------\n')

#Podemos calcular cuanto tiepo estuvo una perosona despierta desde que se levanto hasta que se durmio
despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)

vigilia = duerme - despierta
print(vigilia)

#Si le aplicacmos la propiedad seconds nos dara el total en segundos 
print(vigilia.seconds)