#Zip combina dos o mas listas entrelazando sus elementos en tuples

nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,42]
ciudades = ['Lima', 'Madrid', 'Mexico']

combinados = list(zip(nombres, edades, ciudades))
#Para poder ver el zip necesitamos castearlo dentro de una lista, ya que si no lo hacemos solo nos dara la direccionde memoria
print(combinados)
#NOTA* Si edades tiene un elemento mas este no se va a imprimir ya que solo toma el largo de lista mas corta

#Poedemos crear un loop donde se impriman frases donde contengan todos los elemtos de las listas

for nombres, edades, ciudades in combinados:
    print(f'{nombres} tiene {edades} anios y vive en {ciudades}')

print('\n---------------------\n')

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinados = list(zip(paises, capitales))

for paises, capitales in combinados:
    print(f'La capital de {paises} es {capitales}')

print('\n---------------------\n')
