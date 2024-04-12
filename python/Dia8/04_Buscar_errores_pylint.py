'''
Pylint es un verificador de código, errores y calidad para
Python, siguiendo el estilo recomendado por PEP 8, la guía de
estilo de Python. Es de gran utilidad en el trabajo en equipo.
'''

# Hacemos un error intencionalmente 
def una_funcion():
    numero1 = 500
    print(numero1)
    
    
una_funcion()

'''
Si queremos checar desde pylint como esta el archivo en termino de errores y estilo 
tenemos que buscar la ruta del archivo a analizar, depues ingresamos "pylint >Nombre_archivo.py< -r (reporte) y (yes para confirmar)"
#PS C:\Users\yo_al\Documentos\PythonTotal\python\Dia8> pylint 04_Buscar_errores_pylint.py -r y
'''