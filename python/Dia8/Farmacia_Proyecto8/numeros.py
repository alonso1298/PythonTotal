#generadores
def perfumeria():
    for n in range(1, 10000):
        yield f'P-{n}'
       
def farmacia():
    for n in range(1, 10000):
        yield f'F-{n}'
             
def cosmeticos():
    for n in range(1, 10000):
        yield f'C-{n}'


p = perfumeria()
f = farmacia()
c = cosmeticos()


#decorador
def decorador_turno(rubro):
    
    print('\n' + '*' * 25)
    print('Su numero es: ')
    if rubro == 'P':
        print(next(p))
    elif rubro == 'F':
        print(next(f))
    else: 
        print(next(c))
    print('Favor de ser paciente')
    print('\n' + '*' * 25)
