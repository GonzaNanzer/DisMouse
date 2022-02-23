import tkinter as tk
import serial
import serial.tools.list_ports
from tkinter import ttk as ttk

class DisMouse (tk.Frame):

    def __init__(self):

        self.arduino = serial.Serial()
        self.PuertoCOM = []
        self.baudrate = ['1200', '2400', '4800', '9600', '19200', '38400', '115200']


    def puertos_disponibles(self):
        self.puertos = [port.device for port in serial.tools.list_ports.comports()]
        return list(self.puertos)

    def concetar(self):
        a = self.combobox_port.get()
        b = self.combobox_baud.get()
        self.arduino = serial.Serial(a,b)
        if self.arduino.isOpen():
            print(a,b)
            pass
        else:
            print('No me puedo conectar')

    def leer_dato(self):
        if self.arduino.isOpen():
            print(self.arduino.readline().decode())
        else:
            print('no estoy conectado')


    def HolaDisMouse(self):
        com = 'hDm'
        self.arduino.write(com.encode('ascii'))
        return

    def BotonRojo(self):
        com = 'bR'
        self.arduino.write(com.encode('ascii'))

        return

    def BotonAzul(self):
        com = 'bA'
        self.arduino.write(com.encode('ascii'))
        return

    def BotonNaranja(self):
        com = 'bN'
        self.arduino.write(com.encode('ascii'))
        return

    def BotonCeleste(self):
        com = 'bC'
        self.arduino.write(com.encode('ascii'))
        return

    def BotonFunciones(self):
        com = 'bF'
        self.arduino.write(com.encode('ascii'))
        return

    def BotonOrientacion(self):
        com = 'bO'
        self.arduino.write(com.encode('ascii'))
        return 

    def set_config_Rojo(self):
        com = str(self.combobox_Rojo.current() + 1)
        self.arduino.write(com.encode('ascii'))
        return

    def set_config_Azul(self):
        com = str(self.combobox_Azul.current() + 1)
        self.arduino.write(com.encode('ascii'))
        return

    def set_config_Naranja(self):
        com = str(self.combobox_Naranja.current() + 1)
        self.arduino.write(com.encode('ascii'))
        return

    def set_config_Celeste(self):
        com = str(self.combobox_Celeste.current() + 1)
        self.arduino.write(com.encode('ascii'))
        return

    def set_config_Funcion(self):
        com = str(self.combobox_Funcion.current() + 1)
        self.arduino.write(com.encode('ascii'))
        return

    def set_config_Orientacion(self):
        com = str(self.combobox_Orientacion.current() + 1)
        self.arduino.write(com.encode('ascii'))
        return

    def ChauDisMouse(self):
        com = 'cDm'
        self.arduino.write(com.encode('ascii'))
        self.leer_dato()
        self.arduino.close()
        return exit()

    def widgets(self):

        """
        Creamos la ventana, le asignamos nombre e icono y definimos que se pueda modificar el tamaño de la misma.
        """

        self.ventana = tk.Tk()
        self.ventana.title('DisMouse')
        self.ventana.resizable(True,True)
        self.ventana.iconbitmap(r'DisMouseIco.ico')

        """
        Creo botones y cuadros de opciones.
        """

        #**-------------Entrar en modo config---------------**

        botonConfig = tk.Button(self.ventana, text = 'Entrar Modo Configuracion',bg = 'Grey',fg = 'black',font=18
                                , command = self.HolaDisMouse)
        botonConfig.grid(row=0, column=3, padx=5, pady=5, columnspan=6)
        botonConfig.config(width=40)


        #**-------------Boton Rojo---------------**

        botonRojo = tk.Button(self.ventana, text = 'Boton Rojo',bg = 'red',fg = 'black',font=18
                              ,command = self.BotonRojo)
        botonRojo.grid(row= 1,column=1,padx=5,pady=5, columnspan=3)
        botonRojo.config(width = 20)


        #**-------------Boton Azul---------------**

        botonAzul = tk.Button(self.ventana, text = 'Boton Azul',bg = 'blue',fg = 'black',font=18
                              , command = self.BotonAzul)
        botonAzul.grid(row= 2,column=1,padx=5,pady=5, columnspan=3)
        botonAzul.config(width = 20)


        #**-------------Boton Naranja---------------**
        botonNaranja = tk.Button(self.ventana, text = 'Boton Naranja',bg = 'orange',fg = 'black',font=18
                                 , command = self.BotonNaranja)
        botonNaranja.grid(row= 3,column=1,padx=5,pady=5, columnspan=3)
        botonNaranja.config(width = 20)


        #**-------------Boton Celeste---------------**
        botonCeleste = tk.Button(self.ventana, text = 'Boton Celeste',bg = 'skyblue',fg = 'black',font=18
                                 , command = self.BotonCeleste)
        botonCeleste.grid(row= 4,column=1,padx=5,pady=5, columnspan=3)
        botonCeleste.config(width = 20)


        #**-------------Boton Funciones---------------**
        botonFunc = tk.Button(self.ventana, text = 'Boton Funciones',bg = 'green',fg = 'black',font=18
                              , command = self.BotonFunciones)
        botonFunc.grid(row= 5,column=1,padx=5,pady=5, columnspan=3)
        botonFunc.config(width = 20)


        #**-------------Boton Orientacion---------------**
        botonOrientacion = tk.Button(self.ventana, text = 'Boton Orintacion',bg = 'yellow',fg = 'black',font=18
                                     ,command = self.BotonOrientacion)
        botonOrientacion.grid(row= 6,column=1,padx=5,pady=5, columnspan=3)
        botonOrientacion.config(width = 20)

        #**-------------Salir del modo config---------------**

        botonConfig = tk.Button(self.ventana, text='Salir Del Modo Configuracion', bg='Grey', fg='black', font=18
                                ,command = self.ChauDisMouse)
        botonConfig.grid(row=7, column=3, padx=5, pady=5, columnspan=6)
        botonConfig.config(width=40)

        # **-------------Botones Set---------------**

        botonSetRojo = tk.Button(self.ventana, text='Set Rojo', bg='Grey', fg='black', font=18
                             ,command = self.set_config_Rojo)
        botonSetRojo.grid(row=1, column=18, padx=5, pady=5, columnspan=6)
        botonSetRojo.config(width=40)

        botonSetAzul = tk.Button(self.ventana, text='Set Azul', bg='Grey', fg='black', font=18
                                 , command=self.set_config_Azul)
        botonSetAzul.grid(row=2, column=18, padx=5, pady=5, columnspan=6)
        botonSetAzul.config(width=40)

        botonSetNaranja = tk.Button(self.ventana, text='Set Naranja', bg='Grey', fg='black', font=18
                                 , command=self.set_config_Naranja)
        botonSetNaranja.grid(row=3, column=18, padx=5, pady=5, columnspan=6)
        botonSetNaranja.config(width=40)

        botonSetCeleste = tk.Button(self.ventana, text='Set Celeste', bg='Grey', fg='black', font=18
                                 , command=self.set_config_Celeste)
        botonSetCeleste.grid(row=4, column=18, padx=5, pady=5, columnspan=6)
        botonSetCeleste.config(width=40)

        botonSetFuncion = tk.Button(self.ventana, text='Set Funcion', bg='Grey', fg='black', font=18
                                    , command=self.set_config_Funcion)
        botonSetFuncion.grid(row=5, column=18, padx=5, pady=5, columnspan=6)
        botonSetFuncion.config(width=40)

        botonSetOrientacion = tk.Button(self.ventana, text='Set Orientacion', bg='Grey', fg='black', font=18
                                    , command=self.set_config_Orientacion)
        botonSetOrientacion.grid(row=6, column=18, padx=5, pady=5, columnspan=6)
        botonSetOrientacion.config(width=40)

        #**-------------Ventana desplegable Botones Rojo,Azul,Naranja y Celeste---------------**

        OpBotones = ['Clic izquierdo','Clic derecho','Clic central','Barra espaciadora','Tecla enter','Doble clic',
                     'Una letra','Anular boton']
        self.combobox_Rojo = ttk.Combobox(self.ventana)
        self.combobox_Rojo['values'] = OpBotones
        self.combobox_Rojo.config(width = 20)
        self.combobox_Rojo.grid(row= 1,column=6,padx=5,pady=5, columnspan=3)
        self.combobox_Rojo.current(0)

        self.combobox_Azul = ttk.Combobox(self.ventana)
        self.combobox_Azul['values'] = OpBotones
        self.combobox_Azul.config(width=20)
        self.combobox_Azul.grid(row=2, column=6, padx=5, pady=5, columnspan=3)
        self.combobox_Azul.current(1)

        self.combobox_Naranja = ttk.Combobox(self.ventana)
        self.combobox_Naranja['values'] = OpBotones
        self.combobox_Naranja.config(width=20)
        self.combobox_Naranja.grid(row=3, column=6, padx=5, pady=5, columnspan=3)
        self.combobox_Naranja.current(2)

        self.combobox_Celeste = ttk.Combobox(self.ventana)
        self.combobox_Celeste['values'] = OpBotones
        self.combobox_Celeste.config(width=20)
        self.combobox_Celeste.grid(row=4, column=6, padx=5, pady=5, columnspan=3)
        self.combobox_Celeste.current(3)


        #**-------------Ventana desplegable Boton Funciones---------------**

        OpBotonF = ['Desplazar el cursor','Simular flechas']

        self.combobox_Funcion = ttk.Combobox(self.ventana)
        self.combobox_Funcion['values'] = OpBotonF
        self.combobox_Funcion.config(width=20)
        self.combobox_Funcion.grid(row=5, column=6, padx=5, pady=5, columnspan=3)
        self.combobox_Funcion.current(0)

        #**-------------Ventana desplegable Boton Orientacion---------------**

        OpBotonO = ['Posicion normal','Rotar 90° horario','Rotar 90° anti-horario','Rotar 180°']

        self.combobox_Orientacion = ttk.Combobox(self.ventana)
        self.combobox_Orientacion['values'] = OpBotonO
        self.combobox_Orientacion.config(width=20)
        self.combobox_Orientacion.grid(row=6, column=6, padx=5, pady=5, columnspan=3)
        self.combobox_Orientacion.current(0)

        # **-------------Puertos COM Disponibles---------------**

        port = self.puertos_disponibles()

        self.combobox_port = ttk.Combobox(self.ventana)
        self.combobox_port['values'] = port
        self.combobox_port.config(width = 40)
        self.combobox_port.grid(row = 1, column = 12,padx=5,pady=5, columnspan=3)
        self.combobox_port.current(0)


        self.combobox_baud = ttk.Combobox(self.ventana, values= self.baudrate)
        self.combobox_baud.config(width = 40)
        self.combobox_baud.grid(row = 2, column = 12,padx=5,pady=5, columnspan=3)
        self.combobox_baud.current(3)

        conectar = tk.Button(self.ventana, text='Conectar', bg='Grey', fg='black', font=18
                             , command = self.concetar)
        conectar.grid(row=3, column=12, padx=5, pady=5, columnspan=6)
        conectar.config(width=30)

        # **-------------Dialogo Seria---------------**

        dialogo = tk.Text(self.ventana, width = 30,height = 5)
        dialogo.grid(row=4, column=12, padx=5, pady=5, columnspan=3, rowspan = 3)

        scrollvert = tk.Scrollbar(self.ventana, command = dialogo.yview)
        scrollvert.grid(row=4, column=15,sticky = "nsew", )

        dialogo.config(yscrollcommand=scrollvert.set)

        # **-------------Boton Leer Dato---------------**

        botonLD = tk.Button(self.ventana, text='Leer Dato', bg='grey', fg='black', font=18
                              , command=self.leer_dato)
        botonLD.grid(row=7, column=12, padx=5, pady=5, columnspan=3)
        botonLD.config(width=30)




        self.ventana.mainloop()

if __name__ == "__main__":

    app = DisMouse()
    app.widgets()
