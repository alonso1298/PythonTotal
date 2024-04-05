from pathlib import Path

base = Path.home()
ubicacion_recetario = Path(base, 'Recetas')
lista_recetas = []

def listar_carpetas(ruta):
    # Convertir la ruta en un objeto Path
    ruta = Path(ruta)
    
    # Verificar si la ruta es un directorio
    if ruta.is_dir():
        # Obtener los nombres de las carpetas en la ruta
        carpetas = [carpeta.name for carpeta in ruta.iterdir() if carpeta.is_dir()]
        #Con un loop for mostramos solo los nombres que contiene la lista
        for categorias in carpetas:
            print(categorias) 
    else:
        print("La ruta no es un directorio válido.")
    

def mostrar_recetas(categoria):
    base = Path.home()
    carpeta = Path(base, 'Recetas', categoria)
    #Se crea una lista que por cada nobre de archivo en la carpeta si se encuentra un archivo .txt
    lista_recetas = [carpeta.stem for carpeta in carpeta.glob('*.txt')]
    #Con un loop for mostramos solo los nombres que contiene la lista
    for nombres in lista_recetas:
        indice = lista_recetas.index(nombres) + 1
        print(f"Receta numero: {indice} {nombres}")

def leer_receta(categoria):
    categoria = ''
    input('Ingesa una categoria')
    lista_recetas = mostrar_recetas()
    match categoria:
        case 'Carnes':
            print(f'Esta categoria tiene las siguientes recetas ')
            print('Que receta quieres leer?')


for i in Path(ubicacion_recetario).glob('**/*.txt'):
    lista_recetas.append(i)

print('Bienvenido al recetrario! \nAqui encontraras diversas categorias de delicionas recetas')
print(f'Las recetas las encontraras en la siguiente ruta: {ubicacion_recetario}')
print(f'Actualmente contamos con {len(lista_recetas)} recetas')
print('\n[1] - Leer receta \n[2] - Crear receta \n[3] - Crear categoria \n[4] - Eliminar receta \n[5] - Eliminar Categoria \n[6] - Finalizar programa')
opcion = ""
opcion = input('\nFavor de ingresar una opcion: ')
match opcion:
    case '1':
        print(f'Tenemos las siguientes categorias: \n')
        listar_carpetas(ubicacion_recetario)
        categoria = input('\nQue categoria eliges?: \n')
        print('Estas con las recetas que tenemos: \n')
        mostrar_recetas(categoria)
        print('\nQue receta deseas leer?: ')




