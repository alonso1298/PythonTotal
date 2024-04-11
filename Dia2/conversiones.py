#Conversion implicita
num1  = 20 #Type int
num2 = 30.5 #Type float

num1 = num1 + num2 #Aqui se hace una conversion de dato implitica, que el entero ahora se convierte en float

print(type(num1))
print(type(num2))

print("-------------------------------")
#Conversion explicita
num1 = 5.8 
print(num1)
print(type(num1))

num2 = int(num1)
print(num2)
print(type(num2))


print("-------------------------------")

edad = input("Dime tu edad: ")
edad = int(edad)
nueva_edad = 1 + edad
print(f"Vas a cumplir:  {nueva_edad}")