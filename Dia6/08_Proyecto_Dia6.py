import os 
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "Recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador

#Mostrar Menu inicio
def inicio():
    system('cls')
    print('*' * 50)
    print('*' * 5 + ' Bienvenido al administrador de recetas ' + '*' * 5)
    print('*' * 50)
    print('\n')
    print(f'Las recetas se encuentran en {mi_ruta}')
    print(f'Total recetas: {contar_recetas(mi_ruta)}')

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('Elige una opcion: ')
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa''')
        eleccion_menu = input()

    return int(eleccion_menu)

def mostrar_categorias(ruta):

    print('Categorias: ')
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    # iterdir() se utiliza para iterar sobre los elementos (archivos y directorios) dentro de un directorio dado.
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f'[{contador}] - {carpeta_str}')
        lista_categorias.append(carpeta)
        contador += 1
    
    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input('\nElije una categoria: ')
    
    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print('Recetas: ')
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f'[{contador}] - {receta_str}')
        lista_recetas.append(receta)
        contador += 1 

    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = 'x'

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input('\nElige una receta: ')
    
    return lista[int(eleccion_receta) - 1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crer_receta(ruta):
    existe = False

    while not existe:
        print('Escribe el nombre de tu receta: ')
        nombre_receta = input() + '.txt'
        print('Escribe tu nueva receta: ')
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Tu receta {nombre_receta} ah sido creada')
            existe = True
        else:
            print('Lo siento esa receta ya existe')

def crear_categoria(ruta):
    existe = False

    while not existe:
        print('Escribe el nombre de tu la nueva categoria: ')
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)
        

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Tu nueva categoria {nombre_categoria} ah sido creada')
            existe = True
        else:
            print('Lo siento esa categoria ya existe')

def eliminar_receta(receta):
    #Con este metodo se elimina un archivo 
    Path(receta).unlink()
    print(f"La receta {receta.name} ah sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f'La categoria {categoria.name} ah sido eliminada')

def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input('\nPresione "v" para volver al menu: ')

finalizar_programa = False

while not finalizar_programa:

    menu = inicio()

    if menu == 1:
        # Mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # Elegir una categoria 
        mi_categoria = elegir_categoria(mis_categorias)
        # Mostrar recetas
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print('No hay recetas en esta categoria.')
        else:
            # Elegir recetas 
            mi_receta = elegir_recetas(mis_recetas)
            # Leer receta
            leer_receta(mi_receta)
            # Volver inicio 
            volver_inicio()
        
    elif menu == 2:
        # Mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # Elegir una categoria 
        mi_categoria = elegir_categoria(mis_categorias)
        # Crear receta nueva
        crer_receta(mi_categoria)
        # Volver inicio 
        
    elif menu == 3:
        # Crear nueva categoria
        crear_categoria(mi_ruta)
        #Volver al inicio
        volver_inicio()
        
    elif menu == 4:
        # Mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # Elegir una categoria 
        mi_categoria = elegir_categoria(mis_categorias)
        # Mostrar recetas
        mis_recetas = mostrar_recetas(mi_categoria)
        # Elegir recetas 
        mi_receta = elegir_recetas(mis_recetas)
        # eliminar receta
        eliminar_receta(mi_receta)
        # Volver inicio 
        volver_inicio()
        
    elif menu == 5:
        # Mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # Elegir una categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # Eliminar categoria 
        eliminar_categoria(mi_categoria)
        # Volver al inicio 
        volver_inicio()
        
    elif menu == 6:
        #Finalizar programa 
        finalizar_programa = True
        