#Para compara mas de dos valores se hace de la siguiente manera
mi_bool = 4 < 5 < 6
#Esto es una comparacion directa.s
print(mi_bool)

print('------------AND-------------')

#Aqui verificamos si 4 es menor a 5 y tambien se fija si 5 es mayor a 6
mi_bool2 = (4 < 5) and (5 > 6)
#Al no cumplisre las 2 condiciones el valor del bool es falso 
#Para que de verdadero se tienen que cuplir las 2 condiciones
print(mi_bool2)

mi_bool3 = (55 == 55) and ('perro' == 'perro')
#Tambien se pueden hacer comparaciones de diferente tipos de datos 
print(mi_bool3)

print('-------------OR------------')

mi_bool4 = 8 == 10 or 3 == 3
#Si una de las dos comparaciones es verdadera, esta siempre arrojara verdadero
print(mi_bool4)

#Tambien podemos buscar 2 palabras en un texto 
texto = 'Esta frase es breve'
mi_bool5 = ('frase' in texto) or ('python' in texto)

print('-------------NOT------------')

mi_bool6 = 'a' == 'a'
print(mi_bool6)