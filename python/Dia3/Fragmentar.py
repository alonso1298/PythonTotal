texto = 'ABCDFGHIJKLM'
fragmento = texto[2]
print(fragmento)

print('------------------------')

texto = 'ABCDEFGHIJKLM'
#Al agregar : y agregamos un segundo factor, estamos indicando que desde esos indices se iniciara la extraccion
fragmento = texto[2 : 5]
#Esto nos mostraria el resultado de la extraccion desde el indice 2 al 5 (CDE)
print(fragmento)

texto = 'ABCDEFGHIJKLM'
fragmento = texto[2 : ]
#Si se omite el factor esto se interpretara que sera desde el indice 2 hasta el final de la cadena
#Tambien si omitimos el primer factor, lo tomara desde el inicio hasta el indice indicado.
print(fragmento)

print('------------------------')

texto = 'ABCDEFGHIJKLM'
#Si agrego un tercer factor, este va a decir cada cuantos caracteres se va a extraer o saltar
fragmento = texto[2 : 10 : 2]
print(fragmento)

texto = 'ABCDEFGHIJKLM'
#Si ingresamos un numero negativo vamos a tener toda la cadena al revez
#Toma el ultimo numero y de uno en uno va extrayendo los datos 
fragmento = texto[ :  : -1]
print(fragmento)