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

# Evitar que la pantalla se cierre
aplicacion.mainloop()

