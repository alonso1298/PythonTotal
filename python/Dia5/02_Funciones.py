#Las funciones se crean con la palabra clave def seguido del nombre de la funcion
def saludar_persona(nombre):#Podemos pasar parametros al crear variables internas
    #Esta funcion sirve para saludar a las personas
    print('Hola ' + nombre)

#Para que la funcion se ejecute tenemos que mandar a llamar la funcion 
saludar_persona('Luis') #Le pasamos el parametro a la variable 
saludar_persona('Alonso')

print('\n---------------------\n')

def saludar():
    print('¡Hola mundo!')
    
saludar()