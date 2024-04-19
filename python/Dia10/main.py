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

#Jugador
img_jugador = pygame.image.load('C:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia10\\nave-espacial.png')
img_jugador_x = 368
img_jugador_y = 536

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
    
    img_jugador_x += 0.1
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
    
    jugador(img_jugador_x, img_jugador_y)
    
    pygame.display.update()


