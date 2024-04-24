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
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50)
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
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    
    #Crear Checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, 
                         text=comida.title(), 
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador])
    comida.grid(row=contador,
                column=0,
                sticky=W)
    
    # Crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    
    contador += 1
    
# Generar items bebidas
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    
    #Crear Checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_bebida[contador])
    bebida.grid(row=contador, column=0, sticky=W)
    
    # Crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    
    contador += 1
    
# Generar items postres
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    
    #Crear Checkbutton
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_postre[contador])
    postre.grid(row=contador, column=0, sticky=W)
    
    # Crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)
    
    contador += 1

#Variables 
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiuetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12,'bold'),
                              bg= 'azure4',
                              fg='white')

etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)

texto_costo_comida.grid(row=0, column=1, padx=41)


# Etiuetas de costo y campos de entrada
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis', 12,'bold'),
                              bg= 'azure4',
                              fg='white')

etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)

texto_costo_bebida.grid(row=1, column=1, padx=41)


# Etiuetas de costo y campos de entrada
etiqueta_costo_postre = Label(panel_costos,
                              text='Costo Postre',
                              font=('Dosis', 12,'bold'),
                              bg= 'azure4',
                              fg='white')

etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)

texto_costo_postre.grid(row=2, column=1, padx=41)


# Etiuetas de costo y campos de entrada
etiqueta_subtotal = Label(panel_costos,
                              text='Sub total',
                              font=('Dosis', 12,'bold'),
                              bg= 'azure4',
                              fg='white')

etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)

texto_subtotal.grid(row=0, column=3, padx=41)


# Etiuetas de costo y campos de entrada
etiqueta_impuestos = Label(panel_costos,
                              text='Impuestos',
                              font=('Dosis', 12,'bold'),
                              bg= 'azure4',
                              fg='white')

etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuesto)

texto_impuestos.grid(row=1, column=3, padx=41)

# Etiuetas de costo y campos de entrada
etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis', 12,'bold'),
                              bg= 'azure4',
                              fg='white')

etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)

texto_total.grid(row=2, column=3, padx=41)


# Evitar que la pantalla se cierre
aplicacion.mainloop()

