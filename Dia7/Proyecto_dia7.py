from os import system

class Persona:
    #Dos atributos nombre y apellido
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        

class Cliente(Persona):
    #Atributos: Num de cuenta, balance
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    #Metodos: 
    # 1 - Imprimir cliente __str__ imprime todos los datos incluyendo el balance de su cuenta
    def __str__(self):
        return f'Nombre: {self.nombre} {self.apellido} \nNumero de cuenta: {self.numero_cuenta} \nTu dinero: {self.balance}'
    
    # 2 - depositar() permite decidir cuanto dinero agregar a su cuenta
    def depositar(self):
        dinero = 0
        dinero = float(input('Cuanto dinero deseas depositar?: '))
        self.balance = dinero + self.balance
        print(f'Ahora tienes {self.balance} pesos')

    # 3 - Retirar() cuanto dinero desea sacar de la cuenta 
    def retirar(self):
        while True:
            dinero_retirar = float(input('Cuanto dinero deseas retirar?: '))
            if dinero_retirar > self.balance:
                print(f"No tienes suficiente dinero. Tu saldo actual es: {self.balance} pesos")
                print('Por favor, introduce una cantidad válida.')
            else:
                self.balance -= dinero_retirar
                print(f'Has retirado {dinero_retirar} pesos. Tu saldo restante es: {self.balance} pesos')
                break
        
#Recomendacion: Crear 2 funciones

#Una que se encargue de crear al cliente pidiendole al usuario toda la informacion necesaria y devolviendo un objeto cliente 
def crear_usuario():
    nombre = input('Favor de ingresar tu nombre: ')
    apellido = input('Favor de ingresar un apellido: ')
    numero_cuenta = int(input('Favor de ingresar el numero de cuenta: '))
    balance = float(input('Favor de ingresar el dinero actual: '))
    return Cliente(nombre, apellido, numero_cuenta, balance)

#Inicio() es la funcion que se encarga de la ejecucion de todo el codigo 
def inicio():

    system('cls')
    print('Bienvenido al banco del Bienestar\n')
    print('*' * 10)
    nuevo_cliente = crear_usuario()
    print('\nBienvenido, tu cuenta se a creado exitosamente !!!\n')
    print(nuevo_cliente)
    return nuevo_cliente

def mostrar_opciones():
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,4):
        print('Elige una opcion: ')
        print('''
        [1] - Depositar
        [2] - Retirar
        [3] - Salir del programa''')
        eleccion_menu = input()

    return int(eleccion_menu)

def volver_opciones():
    print('Deseas hacer otro movimiento? \nPresiona "s"')
    opcion = input()
    if opcion == 's':
        return mostrar_opciones()
    else: 
        return inicio()

#Codigo para desarrollar el programa
finalizar_programa = False

nuevo_cliente = inicio()

#Nota* El usuario puede hacer tantas operaciones como quiera hasta que decida salir 
while not finalizar_programa:

    menu = mostrar_opciones()

    #Elegir si quiere hacer deposito o returar o salir 
    if menu == 1:
        nuevo_cliente.depositar()
        menu = volver_opciones()

    elif menu == 2:
        nuevo_cliente.retirar()
        menu = volver_opciones()

    elif menu == 3:
        #Finalizar programa 
        finalizar_programa = True

#El codigo tiene que llevar la cuenta de cuanto dinero hay en el balance y no puede retirar mas dinero del que posee 