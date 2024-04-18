import os
import re
import time
import datetime
import math

ruta = 'C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia9\\Proyecto+Dia+9'

patron = r'N\D{3}-\d{5}'

dia_actual = datetime.date.today()

series = []

inicio = time.time()

#Walk recorre todos los directorios, carpetas, subcarpetas y archivos que encuentre en su camino dada una ruta
print('-' * 80)
print(f'Fecha de busqueda: [{dia_actual}]\n')
print('ARCHIVO\t\tNRO. SERIE')
print('-------\t\t----------')

for carpetas, subcarpetas, archivos in os.walk(ruta):
    for archivo in archivos:
        ruta_archivo = os.path.join(carpetas, archivo)
        with open(ruta_archivo, 'r') as archivo_abierto:

            contenido = archivo_abierto.readlines()
            for linea in contenido:
                coincidencia = re.search(patron, linea)
                if coincidencia:
                    print(f'{archivo}\t{coincidencia.group()}')
                    if coincidencia:
                        series.append(coincidencia.group())

final = time.time()
    
tiempo_ejecucion = (final - inicio)   
                 
print(f'\nNúmeros encontrados: {len(series)}')
print(f'\nDuración de la búsqueda: {math.ceil(tiempo_ejecucion)} segundos')
print('-' * 80)