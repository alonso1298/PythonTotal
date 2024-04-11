class Persona:
    #Dos atributos nombre y apellido
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        

class Cliente(Persona):
    #Atributos: Num de cuenta, balance
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    #Metodos: 
    # 1 - Imprimir cliente __str__ imprime todos los datos incluyendo el balance de su cuenta
    def __str__(self):
        return f'Nombre: {self.nombre} {self.apellido} \nBalance de cuenta: {self.numero_cuenta}: ${self.balance}'
    
    # 2 - depositar() permite decidir cuanto dinero agregar a su cuenta
    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print(f'Deposito aceptado')

    # 3 - Retirar() cuanto dinero desea sacar de la cuenta 
    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print('Retiro realizado')
        else:
            print('Fondos insuficientes')
            
def crear_cliente():
    nombre_cl = input('Favor de ingresar tu nombre: ')
    apellido_cl = input('Favor de ingresar un apellido: ')
    numero_cuenta = input('Favor de ingresar el numero de cuenta: ')
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0
    
    while opcion != 'S':
        print('Elige Depositar [D] - Retirar [R] - Salir del programa [S]')
        opcion = input()
        
        if opcion == 'D':
            monto_dep = int(input('Monto a depositar: '))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input('Monto a retirar: '))
            mi_cliente.retirar(monto_ret)
            
        print(mi_cliente)
        
    print('Gracias por operar en banco Python')
    
inicio()
    
                