'''
Unit Testing es un método o herramienta utilizado en programación
para determinar si un módulo o un conjunto de módulos de código
funciona correctamente. Dicha evaluación se realiza en un archivo
independiente. En Python, se implementa desde el módulo
incorporado unittest.
'''
#Tenemos que importar unittest
import unittest

import cambia_texto

#Heredamos de Unittest los metodos de TestCase
class ProbarCambiaTexto(unittest.TestCase):
    
    #NOTA* El nombre tiene que comensar con la palabra test si no, no va a encontrar el sistema la prueba
    def test_mayusculas(self):
        #Primero ponemor el ejemplo de una palabra que yo quiero ver como funciona
        palabra = 'Buen dia'
        #El resultado va a ser la palabra que yo tengo en cambia texto
        resultado = cambia_texto.todo_mayusculas(palabra)
        # assertEqual es un metodo que se encarga de checar 2 argumentos, el resultado y el resultado esperado
        self.assertEqual(resultado, 'BUEN DIA')
 
'''
Antes incluso de ejecutar el código, Python lee el archivo para definir algunas variables globales. Una de ellas es
__name__, que toma el nombre "__main__" en caso que Python esté corriendo en dicho módulo de manera
individual. Si por el contrario, el módulo fuera importado, la variable __name__ toma el nombre del módulo. Este bloque
de código evalúa que la prueba se esté ejecutando directamente.
'''       
if __name__ == '__main__':
    unittest.main()