from os import system
import numeros

def preguntar():
    system('cls')
    print('*' * 50)
    print('*' * 5 + ' Bienvenido al administrador de turnos ' + '*' * 5)
    print('*' * 50)
    print('\n')

    while True: 
        print('Para que area desea tomar su turno?: ')
        print('''
        [P] - Area de Perfumes
        [F] - Area de Farmacia 
        [C] - Area de Cosmetica''')
        try:
            eleccion_menu = input('\nElija su rubro: ').upper()
            ['P', 'F', 'C'].index(eleccion_menu)
        except ValueError:
            print('Esa no es una opcion valida')
        else:
            break
        
    numeros.decorador_turno(eleccion_menu)    
    
        
        
def inicio(): 
           
    while True:
        preguntar()
        try:
            otro_turno = input('Deseas tomar otro turno? [S] [N]?: ').upper()
            ['S', 'N'].index(otro_turno)
        except ValueError:
            print('Esa no es una opciones valida')
        else:
            if otro_turno == "N":
                print('Gracias por su visita')
                break
            
inicio()