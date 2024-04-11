from pathlib import Path

base = Path.home()
ubicacion_recetario = Path(base, 'Recetas')
opcion = ""
extension = '.txt'
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
    #Se guarda en la variable carpeta la ruta con la categoria elegida
    carpeta = Path(base, 'Recetas', categoria)
    #Se crea una lista que contiene la extension del archivo
    lista_con_extension = [carpeta.name for carpeta in carpeta.glob('*.txt')]
    #Se crea una lista que por cada nobre de archivo en la carpeta si se encuentra un archivo .txt
    lista_recetas = [carpeta.stem for carpeta in carpeta.glob('*.txt')]
    #Con un loop for mostramos solo los nombres que contiene la lista
    for nombres in lista_recetas:
        #Para agregar el indice creamos una nueva variable y con index agregamos el indice sumandole uno en cada ciclo
        indice = lista_recetas.index(nombres) + 1
        #Se muestran los indices y los nombres 
        print(f"Receta numero: {indice} {nombres}")
    return lista_con_extension, carpeta


def leer_receta(ubicacion, lista_con_extension ,numero_receta):
    #Si el numero ingresado es menor que el largo de la lista
    if 1<= numero_receta <= len(lista_con_extension):
        #El texto en ese indice se guardara en la variable receta
        receta = lista_con_extension[numero_receta -1]
        #Se muestra el nombre de la receta que se eligio 
        print(f'Has elegido "{receta}"') 
        #Se guarda en una nueva variavle la ubicacion de la receta que se eligio 
        ubicacion_receta_leer = Path(ubicacion, Path(receta))
        #En otra variable se abre la receta
        mi_receta = ubicacion_receta_leer.open()
        #Se imprime la receta
        print(mi_receta.read())
    else:
        (f'Opcion no valida favor de ingresar un numero entre uno y {len(lista_con_extension)}')
    return ubicacion_receta_leer
    

def crear_receta(ubicacion, extension):
    #Se le pide al usuario que ingrese un nombre
    nombre = input('\nPor favor ingresa el nombre de la receta: ')
    #Este se concatena con la extension 
    archivo_nuevo = nombre + extension
    #Se le pide que agregue el contenido que va a tener el archivo
    contenido_archivo = input('\nPor favor ingresa la receta: ')
    #Se añade el archivo a la categoria que eligio el usuario y se agrega el archivo 
    ruta_archivo = Path(ubicacion, archivo_nuevo)
    #Se escribe el contenido al archivo creado
    ruta_archivo.write_text(contenido_archivo)
    #Si el archivo no se encuentra en la carpeta este imprimira que el archivo no se genero 
    if not ruta_archivo.exists():
        print('\nEste archivo no se genero')
    else: 
        #Si se encuentra este imprimira que se genero correctamente
        print('\nEl archivo se genero correctamente!')


def crear_categoria(ubicacion):
    nombre_carpeta = input('Porfavor ingresa el numero de la categoria: ')
    ruta_nueva = Path(ubicacion, nombre_carpeta)
    ruta_nueva.mkdir()
    if not ruta_nueva.exists():
        print('Este archivo no existe')
    else: 
        print('\nLa categoria se creo correctamente!')

def eliminar_receta(ubicacion_receta):
    ubicacion_receta.unlink()
    if ubicacion_receta.exists():
        print(f"\nEl archivo {ubicacion_receta} no se ah eliminado.")
    else:
       print(f"\nEl archivo {ubicacion_receta} se ah eliminado exitosamente! .")

def eliminar_categoria(ubicacion_categoria):
    ubicacion_categoria.rmdir()
    if ubicacion_categoria.exists():
        print(f"La carpeta {ubicacion_categoria} no ha sido eliminada.")
    else:
        print(f"La carpeta {ubicacion_categoria} se elimino correctamente!.")


for i in Path(ubicacion_recetario).glob('**/*.txt'):
    lista_recetas.append(i)

while opcion not in ['1', '2', '3', '4', '5', '6']:
    print('Bienvenido al recetario! \nAqui encontraras diversas categorias de deliciosas recetas')
    print(f'Las recetas las encontraras en la siguiente ruta: {ubicacion_recetario}')
    print(f'Actualmente contamos con {len(lista_recetas)} recetas')
    print('\n[1] - Leer receta \n[2] - Crear receta \n[3] - Crear categoria \n[4] - Eliminar receta \n[5] - Eliminar Categoria \n[6] - Finalizar programa')
    opcion = input('\nFavor de ingresar una opcion: ')

    if opcion == '1':
        print(f'Tenemos las siguientes categorias: \n')
        listar_carpetas(ubicacion_recetario)
        categoria = input('\nQue categoria eliges?: \n')
        print('Estas con las recetas que tenemos: \n')
        #Se almacena en una variable la lista de recetas que retorna la funcion
        lista_recetas, carpeta = mostrar_recetas(categoria)
        receta = int(input('\nQue receta deseas leer? Ingresar el numero de la receta: '))
        leer_receta(carpeta, lista_recetas, receta)

    elif opcion == '2':
        print(f'Tenemos las siguientes categorias: \n')
        listar_carpetas(ubicacion_recetario)
        categoria = input('\nQue categoria eliges?: \n')
        lista_recetas, carpeta = mostrar_recetas(categoria)
        crear_receta(carpeta, extension)

    elif opcion == '3':
        crear_categoria(ubicacion_recetario)
    elif opcion == '4':
        print(f'Tenemos las siguientes categorias: \n')
        listar_carpetas(ubicacion_recetario)
        categoria = input('\nQue categoria eliges?: \n')
        print('Estas con las recetas que tenemos: \n')
        #Se almacena en una variable la lista de recetas que retorna la funcion
        lista_recetas, carpeta = mostrar_recetas(categoria)
        receta = int(input('\nQue receta deseas eliminar? Ingresar el numero de la receta: '))
        ubicacion = leer_receta(carpeta, lista_recetas, receta)
        eliminar_receta(ubicacion)

    elif opcion == '5':
        print(f'Tenemos las siguientes categorias: \n')
        listar_carpetas(ubicacion_recetario)
        categoria = input('\nQue categoria eliges?: \n')
        lista_recetas, carpeta = mostrar_recetas(categoria)
        eliminar_categoria(carpeta)

    elif opcion == '6':
        print("Finalizando programa...")
        break
    else:
        print('Ingresa un numero valido entre el 1 al 6')
