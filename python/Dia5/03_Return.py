def multiplicar(num1,num2):#Creamos una funcion que pida 2 parametros
    return num1 * num2 #Con return esto retronara la multiplicacion sin necesidad de un print

print(multiplicar(5,10))#La funcion return noimprime nada, para verlo necesitamos poner la funcion print

resultado = multiplicar(5,10)
print(resultado)#Lo mejor es agregarlo a una variable y despues imprimier esta variable

print('\n---------------------\n')

#Tambien en las funciones en vez de solo tener el return, puede tener toda la operacion en variables internas 
def suma(num1,num2):
    total = num1 + num2
    return total

sum = suma(3,9)
print(sum)

print('\n---------------------\n')

def invertir_palabra(palabra):
    return (palabra[::-1]).upper()
    
resultado = invertir_palabra('Python')
print(resultado)