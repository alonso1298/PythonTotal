nombre = input("Cuale es tu nombre?: ")
total_vendido = float(input("Cuanto has vendido?: "))

print(f'Hola {nombre}, este mes has ganado en comisiones un total de: ${round(total_vendido * 0.13, 2)}')