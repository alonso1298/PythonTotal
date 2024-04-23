import pygame
import random
import math
from pygame import mixer

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

# Agregar musica
mixer.music.load('C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia10\\stranger-things.mp3')
mixer.music.set_volume(0.6)
mixer.music.play(-1)

# Varibles del Jugador
img_jugador = pygame.image.load('C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia10\\nave-espacial.png')
jugador_x = 368
jugador_y = 500
jugadorx_cambio = 0

# Variables enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia10\\ovni.png'))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

# Variables de la bala
img_bala = pygame.image.load('C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia10\\hotdog.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 0.8
bala_visible = False

#Mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

#Puntaje
puntaje = 0
fuente = pygame.font.Font('C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia10\\techno_hideo.ttf', 32)
texto_x = 10
texto_y = 10

# Texto final de juego 
fuente_final = pygame.font.Font('C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia10\\techno_hideo.ttf', 40)

def texto_final():
    mi_fuente_final = fuente_final.render('GAME OVER', True, (255,255,255))
    pantalla.blit(mi_fuente_final, (270, 200))

#Funcion Jugador 
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

#Funcion Enemigo    
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

#Funcion disparar bala    
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x, y - 40))

# Detectar_colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    if distancia < 27:
        return True
    else:
        return False
    
    
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
                sonido_bala = mixer.Sound('C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia10\\disparo.mp3')
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)
        
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
    for e in range(cantidad_enemigos):
        
        # Fin del juego 
        if enemigo_y[e] > 500:
            for  k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
        
        enemigo_x[e] += enemigo_x_cambio[e]
    
        #Mantener dentro de bordes al enemigo 
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]
            
        # Colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia10\\roblox-death.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
        
        enemigo(enemigo_x[e], enemigo_y[e], e)
        
    # Movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
        
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio
        
        
         
    jugador(jugador_x, jugador_y)
    
    mostrar_puntaje(texto_x, texto_y)
    
    #Actualizar
    pygame.display.update()


