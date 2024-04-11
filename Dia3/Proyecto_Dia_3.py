text = input('Por favor ingresa un texto: ').lower()
letras = input('Favor de ingresar 3 letras de tu eleccion: ').lower()

#Con este metodo separamos cada una de las palabras y se alojan en una lista llamada num_palabras
num_palabras = text.split()

#Se utiliza el metodo split para separar los valores en una lista
resultado = letras.split()

#Aqui preguntamos si la palabra 'Python' se encuentra en el texto
palabra = 'python' in text

#Aqui se almacenan los valores que ingreso el usurario
letra1, letra2, letra3 = resultado

print(f'La letra: {letra1} aparece {text.count(letra1)} veces. \nLa letra: {letra2} aparece {text.count(letra2)} veces. \nLa letra: {letra3} aparece {text.count(letra3)} veces.')
print(f'El numero de palabras de tu texto es: {len(num_palabras)}')
print(f'La primera letra del texto es {text[0]} y la ultima letra es {text[::-1][0]}')
print(f'Tu texto al revez quedaria de la siguiente manera {text[::-1]}')
print(f'La palabra "Python" esta en el texto?: {palabra}')