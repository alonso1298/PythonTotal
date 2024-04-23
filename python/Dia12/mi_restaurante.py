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


# Evitar que la pantalla se cierre
aplicacion.mainloop()

