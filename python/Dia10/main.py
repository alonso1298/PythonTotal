import pygame

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

# Varibles del Jugador
img_jugador = pygame.image.load('C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia10\\nave-espacial.png')
jugador_x = 368
jugador_y = 536
jugadorx_cambio = 0
jugadory_cambio = 0


#Funcion Jugador 
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

'''
Tenemos un loop que se ejecute siempre que sea True y va a revisar cada uno de los eventos que existen dentro de la 
nomenclatura de pygame y si ese evento de tipo QUIT que es cuando se hace click en la x de la ventana
la variable pasara a ser falsa y se terminara el programa
'''
while se_ejecuta:
    
    #RGB pantalla
    pantalla.fill((205, 144, 228))
    
    #Iterar eventos
    for evento in pygame.event.get():
        
        # Evento Cerrar programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
        #Evento presionar flechas    
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugadorx_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugadorx_cambio = 0.3
        
        #Evento Soltar flechas        
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugadorx_cambio = 0
    
    #Modificar ubicacion
    jugador_x += jugadorx_cambio
    
    #Mantener dentro de bordes 
    if jugador_x <= 0:
        jugador_x = 0
        
    elif jugador_x >= 736:
        jugador_x = 736
        
        
    jugador(jugador_x, jugador_y)
    
    #Actualizar
    pygame.display.update()


