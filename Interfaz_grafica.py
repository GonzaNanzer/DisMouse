import tkinter as tk
"""
Creamos la ventana, le asignamos nombre e icono y definimos que se pueda modificar el tamaño de la misma.
"""

ventana = tk.Tk()
ventana.title('DisMouse')
ventana.resizable(True,True)
ventana.iconbitmap(r'D:\Pycharm\DisMouse\DisMouseIco.ico')


"""
Creamos un frame, le damos un tamaño y lo empaquetamos.
"""
miFrame = tk.Frame(ventana)
miFrame.pack()
miFrame.grid()

"""
Creo botones y cuadros de opciones.
"""

minombre = tk.StringVar()
#**-------------Boton Rojo---------------**
botonRojo = tk.Button(ventana, text = 'Boton Rojo',bg = 'red',fg = 'black',font=18)
botonRojo.grid(row= 0,column=1,padx=5,pady=5, columnspan=3)

ventanaBotonRojo = tk.Button(ventana)
ventanaBotonRojo.grid(row= 0,column=4,padx=5,pady=5, columnspan=3)

#**-------------Boton Azul---------------**
botonAzul = tk.Button(ventana, text = 'Boton Azul',bg = 'blue',fg = 'black',font=18)
botonAzul.grid(row= 1,column=1,padx=5,pady=5, columnspan=3)

#**-------------Boton Naranja---------------**
botonNaranja = tk.Button(ventana, text = 'Boton Naranja',bg = 'orange',fg = 'black',font=18)
botonNaranja.grid(row= 2,column=1,padx=5,pady=5, columnspan=3)

#**-------------Boton Celeste---------------**
botonCeleste = tk.Button(ventana, text = 'Boton Celeste',bg = 'skyblue',fg = 'black',font=18)
botonCeleste.grid(row= 3,column=1,padx=5,pady=5, columnspan=3)

#**-------------Boton Funciones---------------**
botonFunc = tk.Button(ventana, text = 'Boton Funciones',bg = 'green',fg = 'black',font=18)
botonFunc.grid(row= 4,column=1,padx=5,pady=5, columnspan=3)

#**-------------Boton Orientacion---------------**
botonOrientacion = tk.Button(ventana, text = 'Boton Orintacion',bg = 'yellow',fg = 'black',font=18)
botonOrientacion.grid(row= 5,column=1,padx=5,pady=5, columnspan=3)

ventana.mainloop()