from random import choice

#Creamos una lista de palabras
lista_palabras = ["esperanza", "eventura", "libertad", "amistad", "sabiduria", "armonia", "creatividad", "inspiracion", "S=serenidad", "felicidad"]
# Creamos una variable donde almacenemos las letras correctas que ah dado el usuario.
letras_correctas = []
# Creamos una variable donde almacenemos las letras incorrectas que ah dado el usuario.
letras_incorrectas = []
#Creamos la variable intentos que esta llevara la cuenta de cuantos intentos hemos tenido
intentos = 6
#Creamos la variable aciertos la cual llevara la cuenta de cuantos aciertos hemos tenido
aciertos = 0
#Esta variable se asigna False porque al comienzo del juego no esta terminado
juego_terminado = False

#Definimos la funcion para que al pasarle una lista esta nos de un elemento
def elegir_palabra(lista):
    palabra = choice(lista)
    #Esta variable va a contener cuantas letras distintas tiene la palabra sin importar las repeticiones
    letras_unicas = len(set(palabra))
    return palabra, letras_unicas


def pedir_letra():
    #Inicializamos una variable con un str vacio 
    letra = ''
    #Esta variable evalua si la letra es valida
    es_valida = False
    #En esta variable almacenaremos el abecedario completo
    abecedario = 'abcdefghijklmnopqrstvwxyz'
    #Creamos un loop para que se repita tantas veces mientras que la letra no sea valida
    while not es_valida:
        #Almacenamos el imput en la variable y lo convertimos en minuscula
        letra = input('Ingresa una letra porfavor: ').lower()
        #Si la letra esta en el abecedario y aparte solo es una letra
        if letra in abecedario and len(letra) == 1:
            #La variable la convertimos en True
            es_valida = True
        else:
            print('Por favor ingresa una letra valida.')
    return letra
            


def ocultar_palabra(palabra):
    #Creamos una lista vacia 
    palabra_oculta = []
    
    #Con el For se va a fijar si pone la letra o un guion
    for i in palabra:
        #Si esa letra se encuentra entre las letras correctas
        if i in letras_correctas:
            #Se le agregara la letra
            palabra_oculta.append(i)
        else:
            #Si la letra no esta se le agregara un guion
            palabra_oculta.append('-')

    #Aqui mostramos la palabra separada con espacios con el metodo join ya que este permite unir todos los elementos de lista oculta separados por un espacio
    print(' '.join(palabra_oculta))

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    #Esta variable quiere decir que el juego aun no a terminado
    fin = False

    #Nos fijamos si la letra legida se encuentra dentro de la palabra oculta
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        #Si esto ocurre la lista de palabras correctas va a recibir la letra elegida
        letras_correctas.append(letra_elegida)
        #Ademas si se acierta la letra se aumenta las coincidencias 
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print('Ya has encontrado esa letra. Intenta con otra diferente')
    else: 
        #Si el usuario no acerto entonces la lista de letras incorrectas va a recibir la letra elegida
        letras_incorrectas.append(letra_elegida)
        #Se le resta una vida 
        vidas -= 1
    
    #Si el usuario se queda sin vidas 
    if vidas == 0:
        #Se va a invocar la funcion perder
        fin = perder()
    #Si el las coincidencias son iguales a la cantidad de letras 
    elif coincidencias == letras_unicas:
        # Se llamara la funcion ganar
        fin = ganar(palabra_oculta) 

    #Retorna como han quedado lasvidas,el estado del juego y las coincidencias
    return vidas, fin, coincidencias

def perder():
    print("Te has quedado sin vidas ")
    print(f"La palabra ocultaera {palabra}")

    return True

def ganar(palabra_descubierta):
    ocultar_palabra(palabra_descubierta)
    print("Felicitaciones has encontrado la palabra")
    return True



palabra, letras_unicas  = elegir_palabra(lista_palabras)

while not juego_terminado:
    print("\n" + "*" * 20 + "\n")
    ocultar_palabra(palabra)
    print("\n")
    print("Letras incorrectas: " + "-".join(letras_incorrectas))
    print(f"vidas {intentos}")
    print("\n" + "*" * 20 + "\n")
    letra = pedir_letra()

    intentos, terminado, aciertos = chequear_letra(letra,palabra,intentos,aciertos)

    juego_terminado = terminado
