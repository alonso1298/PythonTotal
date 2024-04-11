'''
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.
'''

def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    lista_numeros = [num1, num2, num3]
    if suma > 15:
        return max(lista_numeros)
    elif suma < 10:
        return min(lista_numeros)
    elif suma >= 10 and suma <= 15:
        return lista_numeros[1]
    
resultado = devolver_distintos(4,2,3)
print(resultado)