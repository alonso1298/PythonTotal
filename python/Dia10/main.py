import pygame
import random

#inicializamos a Pygame
pygame.init()

#Creamos el tamano de la pantalla 
pantalla  = pygame.display.set_mode((800, 600))

#Creamos un loop para que se muestre la pantalla
se_ejecuta = True

#Titulo e icono 
pygame.display.set_caption('Invasion Espacial')
icono = pygame.image.load('C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia10\\nasa.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia10\\Fondo.jpg')

# Varibles del Jugador
img_jugador = pygame.image.load('C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia10\\nave-espacial.png')
jugador_x = 368
jugador_y = 500
jugadorx_cambio = 0

# Variables enemigo
img_enemigo = pygame.image.load('C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia10\\ovni.png')
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 0.3
enemigo_y_cambio = 50

# Variables de la bala
img_bala = pygame.image.load('C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia10\\hotdog.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

#Funcion Jugador 
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

#Funcion Enemigo    
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))

#Funcion disparar bala    
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

'''
Tenemos un loop que se ejecute siempre que sea True y va a revisar cada uno de los eventos que existen dentro de la 
nomenclatura de pygame y si ese evento de tipo QUIT que es cuando se hace click en la x de la ventana
la variable pasara a ser falsa y se terminara el programa
'''
while se_ejecuta:
    
    #imagen de fondo
    pantalla.blit(fondo, (0,0))
    
    #Iterar eventos
    for evento in pygame.event.get():
        
        # Evento Cerrar programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
        #Evento presionar teclas    
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugadorx_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugadorx_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                disparar_bala(jugador_x, bala_y)
        
        #Evento Soltar flechas        
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugadorx_cambio = 0
    
    #Modificar ubicacion del jugador
    jugador_x += jugadorx_cambio
    
    #Mantener dentro de bordes al jugador 
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
        
    #Modificar ubicacion del enemigo
    enemigo_x += enemigo_x_cambio
    
    #Mantener dentro de bordes al enemigo 
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.3
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -0.3
        enemigo_y += enemigo_y_cambio
        
    # Movimiento bala
    if bala_visible:
        disparar_bala(jugador_x, bala_y)
        bala_y -= bala_y_cambio
        
        
        
    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)
    
    #Actualizar
    pygame.display.update()


