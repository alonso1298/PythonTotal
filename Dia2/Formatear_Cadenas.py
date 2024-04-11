#Esta es una forma inpractica de concatenar cadenas
x = 10
y = 5

print("Mis numeros son: " + str(x) + " y " + str(y))

print("----------------------------")

#Funcion format
print("Mis numeros son: {} y {}".format(x, y))
#Tambien se pueden realizar operaciones
print("La suma de los numeros: {} y {} es igual a {}".format(x, y, x+y))

print("----------------------------")

#Cadenas Literales

color = "gris" 
matricula = "NCZ5794"

print(f"El color del carro es: {color} y su matricula es: {matricula}")