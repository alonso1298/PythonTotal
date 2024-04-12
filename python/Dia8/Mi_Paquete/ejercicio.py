#Importamos desde el paquete el archivo que contiene las funciones 
from Paquete_Alonso import suma_y_resta
#Para importar un sub paquete ponemos el nombre del paquete inicial y enseguida el nombre del sub paquete, despues la funcion 
from Paquete_Alonso.Sub_Paquete import saludo

#Para usar sus funciones primero tengo que llamar el modulo y con un punto las funciones 
suma_y_resta.suma(15,2)
suma_y_resta.resta(80,60)

#Ya podemos importar saludo del sub paquete 
saludo()