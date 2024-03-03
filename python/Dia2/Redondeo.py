resultado = round(90/7)
print(resultado)

print("--------------------------")

#Tabien se puede aplicar directamente
print(round(90 / 7))

print("--------------------------")

#Si solo queremos ver 2 decimales nos muestra 67 ya que redondeo hacia arriba el segundo 6 
valor = round(95.6666666666666666, 2)
print(valor)

print("--------------------------")
#Si redondeamos en el valor el tipo de dato es int
valor = round(95.6666666666666666)
print(valor)
print(type(valor))
#Si redondeamos en la impresion el tipo de dato que sale es float
valor = 95.6666666666666666
print(round(valor))
print(type(valor))

#Esto pasa porque cuando hacemos el redondeo dentro de la variable estamos modificando el valor del numero
#Cuando lo hacemos fuera de la variable no se esta modificando solo se esta modificando en la forma en que se ve, pero no se cambia el tipo de dato
