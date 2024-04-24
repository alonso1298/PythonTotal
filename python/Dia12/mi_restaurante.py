from tkinter import *

#Iniciar tkinter
aplicacion = Tk()


# Tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

# Evitar maximizar 
aplicacion.resizable(0, 0)

#Titulo de ventana
aplicacion.title('Mi restaurante - Sistema de Facturacion')

#Color de fondo de la ventana
aplicacion.config(bg = 'PaleGoldenrod')

#Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

#Titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4',
                        font=('Dosis', 58), bg='PaleGoldenrod', width=20)
etiqueta_titulo.grid(row=0, column=0)

# Panel Izquierdo
panel_izquierdo = Frame(aplicacion, border=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#Panel Costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

#Panel Comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                          bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

#Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                          bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

#Panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                          bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

#Panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

#Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, background='PaleGoldenrod')
panel_calculadora.pack()

#Panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, background='PaleGoldenrod')
panel_recibo.pack()

#Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, background='PaleGoldenrod')
panel_botones.pack()

# Lista de productos 
lista_comidas = ['pollo', 'cordero', 'pescado', 'salmon', 'tacos', 'pizza', 'suadero', 'pastor']
lista_bebidas = ['agua', 'refresco', 'te', 'cafe', 'jugo', 'vino', 'cerveza', 'tequila']
lista_postres = ['flan', 'fruta', 'helado', 'mouse', 'pastel', 'pay', 'gelatina', 'chocolate']

# Generar items comida
variables_comida = []
contador = 0
for comida in lista_comidas:
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_comida[contador])
    comida.grid(row=contador, column=0, sticky=W)
    contador += 1
    
# Generar items bebidas
variables_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_bebida[contador])
    bebida.grid(row=contador, column=0, sticky=W)
    contador += 1
    
# Generar items postres
variables_postre = []
contador = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_postre[contador])
    postre.grid(row=contador, column=0, sticky=W)
    contador += 1


# Evitar que la pantalla se cierre
aplicacion.mainloop()

