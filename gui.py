
#importar librerias
import tkinter as tk
import funciones

#Caracteristicas pantalla
pantalla=tk.Tk()
pantalla.title('juego del ahorcado')
pantalla.geometry('400x470')
#pantalla.attributes("-toolwindow",-1)


###============================================
###============================================
###============================================
###============================================
###============================================
###============================================
###============================================

def _cerrarventana():
    pantalla.destroy()

###============================================
###============================================
###============================================
###============================================
###============================================
###============================================

#imprime maniqui
Figura=tk.Label(pantalla,text=funciones.maniqui(1),font=('consolas',14),justify='left').pack()

#imprime baner de texto
Texto=tk.Label(pantalla,text='GUITARRER_',font=('Arial',22),fg='red',justify='left').pack()

#separador facil ===================
tk.Label(pantalla,text=' ',font=('Arial',5)).pack()
#=============================


TextoEntrada=tk.Entry().pack()

#separador facil ===================
tk.Label(pantalla,text=' ',font=('Arial',5)).pack()
#=============================


Boton1=tk.Button(pantalla,text='  Enviar  ',font=('Arial',10),justify='left').pack()

#separador facil ===================
tk.Label(pantalla,text=' ',font=('Arial',5)).pack()
#=============================

Boton1=tk.Button(pantalla,text='  Cerrar ventana  ',font=('Arial',10),justify='left',command=lambda:_cerrarventana()).pack()

#separador facil ===================
tk.Label(pantalla,text=' ',font=('Arial',5)).pack()
#=============================

#imprime Anuncio
Anuncio=tk.Label(pantalla,text='Este programa fue escrito por Edwin Saul Pareja Molina, GPL3',font=('Arial',8),justify='left').pack(side='bottom')


pantalla.mainloop()

