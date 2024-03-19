# A python le falataba una herramieta que existe en otros lenguajes que es una variedad del if que permite elegir una opcion en una serie de opciones
# Esta se conoce como como Switch o Switch case en Python a partir de la version 3.10 esta opcion esta disponible y se llama match

serie = "N-02" #Anteriormente lo hariamos de esta forma

if serie == "N-01":
    print('Samsung')
elif serie == "N-02":
    print('Nokia')
elif serie == 'N-3':
    print('Motorola')
else:
    print('No existe ese producto')

print('\n---------------------\n')

#Ahora lo haremos con la palabra clave 'match' 
match serie:
    case "N-01":
        print('Samsung')
    case "N-02":
        print('Nokia')
    case "N-03":
        print('Motorola')
    case _:
        print('No existe')

print('\n---------------------\n')

cliente = {'nombre': 'Federico', 
          'edad': 45, 
          'ocupacion': 'instructor'}

pelicula = {'titulo': 'Matrix', 
            'ficha_tecnica':{'protagonista': 'Keanu reeves',
                                'director': 'Lana y Lilly Wachowski'}}

elementos = [cliente, pelicula, 'libro']

for i in elementos:
    match i:
        case {'nombre':nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print('Es un cliente')
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista': protagonista,
                                'director': director}}:
            print('Es una pelicula')
            print(titulo, protagonista, director)
        case _:
            print('No se que es esto')