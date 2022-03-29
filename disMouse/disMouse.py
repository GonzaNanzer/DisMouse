import tkinter as tk
import serial
import serial.tools.list_ports
from tkinter import ttk as ttk

class DisMouse (tk.Frame):

    def __init__(self,master = None):
        self.arduino = serial.Serial()
        self.PuertoCOM = []
        self.baudrate = ['1200', '2400', '4800', '9600', '19200', '38400', '115200']
        self.valor_letra = ''


    def puertos_disponibles(self):
        self.puertos = [port.device for port in serial.tools.list_ports.comports()]
        return list(self.puertos)

    def conectar(self):
        a = self.combobox_port.get()
        b = '9600'
        self.arduino = serial.Serial(a,b)
        if self.arduino.isOpen():
            pass
        else:
            print('No me puedo conectar')

    def leer_dato(self):
        if self.arduino.isOpen():
            print(self.arduino.readline().decode())
        else:
            print('no estoy conectado')

    """    def Set_caracter(self):
        self.valor_letra= str(self.text.get())
        print(self.valor_letra)
        return self.raiz2.destroy()"""

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

    def BotonVelocidad(self):
        com = 'bV'
        self.arduino.write(com.encode('ascii'))
        return

    def set_config_Rojo(self):
        com = str(self.combobox_Rojo.current() + 1)
        if com == '7':
            self.raiz2 = tk.Toplevel()
            self.FrameVentana = tk.LabelFrame(self.raiz2)
            self.n = DisMouse(master=self.raiz2)
            self.label = tk.Label(self.FrameVentana, text='Ingrese un caracter: ')
            self.label.grid(row=1, column=0)
            self.text = tk.Entry(self.FrameVentana)
            self.text.grid(row=2, column=0)
            self.button = tk.Button(self.FrameVentana, text='Set Letra', bg='Grey', fg='black', font=10,
                                    command=self.Set_caracter)
            self.button.grid(row=3, column=0)
            self.FrameVentana.pack()
            self.raiz2.grab_set()
            self.arduino.write(self.valor_letra.encode())
            pass
        else:
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

    def set_Velocidad(self):
        com = str(self.valorVel.get())
        print(com)
        self.arduino.write(com.encode('ascii'))
        return

    def ChauDisMouse(self):
        com = 'cDm'
        self.arduino.write(com.encode('ascii'))
        self.leer_dato()

        self.arduino.close()
        return exit()

    def Set_caracter(self):
        text = str(self.una_letra.get())
        self.arduino.write(text.encode())
        print(text)
        return

    def widgets(self):

        # (1)*****---------------------Frame 1---------------------*****#

        # (1.1)*****---------------------Conectar tu dispositivo---------------------*****#

        self.ventana = tk.Tk()
        self.ventana.title('disMouse')
        #self.ventana.iconbitmap(r'..\dist\DisMouseIco.ico')
        self.ventana.resizable(False,False)

        #principal = Principal(master = self.ventana)

        self.Frame1 = tk.LabelFrame(self.ventana, text='Configure su dispositivo')

        # **-------------Puertos COM Disponibles---------------**

        self.port = self.puertos_disponibles()

        self.titulo2 = tk.Label(self.Frame1, text='Seleccionar puerto: ')
        self.titulo2.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

        self.combobox_port = ttk.Combobox(self.Frame1)
        self.combobox_port['values'] = self.port
        self.combobox_port.config(width=15)
        self.combobox_port.grid(row=1, column=3, padx=30, pady=5, columnspan=3)

        self.conectar = tk.Button(self.Frame1, text='Conectar', bg='Grey', fg='black', font=18
                                  , command= self.conectar)
        self.conectar.grid(row=1, column=6, padx=30, pady=5, columnspan=3)
        self.conectar.config(width=10)

        self.Frame1.pack()

        # (2)*****---------------------Frame 2---------------------*****#
        self.Frame2 = tk.LabelFrame(self.ventana, text='Ingresar/Salir del Modo Configuracion.')
        self.botonConfig = tk.Button(self.Frame2, text='Ingresar al Modo Configuracion', bg='Grey', fg='black', font=10
                                     ,command= self.HolaDisMouse)
        self.botonConfig.grid(row=1, column=2, padx=5,pady=5, columnspan=5)
        self.botonConfig.config(width=24)

        self.botonSalirConfig = tk.Button(self.Frame2, text='Salir del Modo Configuracion', bg='Grey', fg='black', font=10
                                          , command= self.ChauDisMouse)
        self.botonSalirConfig.grid(row=1, column=10, pady=5, columnspan=5)
        self.botonSalirConfig.config(width=24)
        self.Frame2.pack()

        # (3)*****---------------------Frame 3---------------------*****#

        # (3.1)*****---------------------Frame 3 - Botones ---------------------*****#

        self.Frame3 = tk.LabelFrame(self.ventana, text='Configura tu disMouse')

        self.Frame4 = tk.Frame(self.Frame3)

        # (3.2)*****---------------------Frame 3 - Botones ---------------------*****#

        self.SubFrame1 = tk.LabelFrame(self.Frame4, text='Boton o Funcion')

        self.botonRojo = tk.Button(self.SubFrame1, text='Boton Rojo', bg='red', fg='black', font=18
                                   , command= self.BotonRojo)
        self.botonRojo.grid(row=3, column=1, padx=10, pady=5, columnspan=3)
        self.botonRojo.config(width=15)

        self.botonAzul = tk.Button(self.SubFrame1, text='Boton Azul', bg='blue', fg='black', font=18
                                   , command= self.BotonAzul)
        self.botonAzul.grid(row=4, column=1, padx=10, pady=5, columnspan=3)
        self.botonAzul.config(width=15)

        self.botonNaranja = tk.Button(self.SubFrame1, text='Boton Naranja', bg='orange', fg='black', font=18
                                      , command= self.BotonNaranja)
        self.botonNaranja.grid(row=5, column=1, padx=10, pady=5, columnspan=3)
        self.botonNaranja.config(width=15)

        self.botonCeleste = tk.Button(self.SubFrame1, text='Boton Celeste', bg='skyblue', fg='black', font=18
                                      , command= self.BotonCeleste)
        self.botonCeleste.grid(row=6, column=1, padx=10, pady=5, columnspan=3)
        self.botonCeleste.config(width=15)

        self.botonFunciones = tk.Button(self.SubFrame1, text='Boton Funcion', bg='Green', fg='black', font=18
                                        , command= self.BotonFunciones)
        self.botonFunciones.grid(row=7, column=1, padx=10, pady=5, columnspan=3)
        self.botonFunciones.config(width=15)

        self.botonOrientacion = tk.Button(self.SubFrame1, text='Boton Orientacion', bg='yellow', fg='black', font=18
                                          , command= self.BotonOrientacion)
        self.botonOrientacion.grid(row=8, column=1, padx=10, pady=5, columnspan=3)
        self.botonOrientacion.config(width=15)

        self.botonVelocidad = tk.Button(self.SubFrame1, text='Boton Velocidad', bg='brown', fg='black', font=18
                                        , command= self.BotonVelocidad)
        self.botonVelocidad.grid(row=9, column=1, padx=10, pady=5, columnspan=3)
        self.botonVelocidad.config(width=15)

        self.botonNull = tk.Button(self.SubFrame1)
        self.botonNull.grid(row=10, column=1, padx=10, pady=5, columnspan=3)
        self.botonNull.config(width=15)

        # (3.3)*****---------------------Frame 3 - Botones desplegables ---------------------*****#

        self.SubFrame2 = tk.LabelFrame(self.Frame4, text='Opciones')

        OpBotones = ['Clic izquierdo', 'Clic derecho', 'Clic central', 'Barra espaciadora', 'Tecla enter', 'Doble clic',
                     'Una letra', 'Anular boton']
        self.combobox_Rojo = ttk.Combobox(self.SubFrame2)
        self.combobox_Rojo['values'] = OpBotones
        self.combobox_Rojo.config(width=15)
        self.combobox_Rojo.grid(row=3, column=4, padx=10, pady=10, columnspan=3)
        self.combobox_Rojo.current(0)

        self.combobox_Azul = ttk.Combobox(self.SubFrame2)
        self.combobox_Azul['values'] = OpBotones
        self.combobox_Azul.config(width=15)
        self.combobox_Azul.grid(row=4, column=4, padx=10, pady=10, columnspan=3)
        self.combobox_Azul.current(1)

        self.combobox_Naranja = ttk.Combobox(self.SubFrame2)
        self.combobox_Naranja['values'] = OpBotones
        self.combobox_Naranja.config(width=15)
        self.combobox_Naranja.grid(row=5, column=4, padx=10, pady=10, columnspan=3)
        self.combobox_Naranja.current(2)

        self.combobox_Celeste = ttk.Combobox(self.SubFrame2)
        self.combobox_Celeste['values'] = OpBotones
        self.combobox_Celeste.config(width=15)
        self.combobox_Celeste.grid(row=6, column=4, padx=10, pady=10, columnspan=3)
        self.combobox_Celeste.current(3)

        OpBotonF = ['Desplazar el cursor', 'Simular flechas']

        self.combobox_Funcion = ttk.Combobox(self.SubFrame2)
        self.combobox_Funcion['values'] = OpBotonF
        self.combobox_Funcion.config(width=15)
        self.combobox_Funcion.grid(row=7, column=4, padx=10, pady=10, columnspan=3)
        self.combobox_Funcion.current(0)

        OpBotonO = ['Posicion normal', 'Rotar 90° horario', 'Rotar 90° anti-horario', 'Rotar 180°']

        self.combobox_Orientacion = ttk.Combobox(self.SubFrame2)
        self.combobox_Orientacion['values'] = OpBotonO
        self.combobox_Orientacion.config(width=15)
        self.combobox_Orientacion.grid(row=8, column=4, padx=10, pady=10, columnspan=3)
        self.combobox_Orientacion.current(0)

        self.valorVel = tk.StringVar()
        self.slider = tk.Scale(self.SubFrame2, from_=5, to=50, orient='horizontal'
                          , length=100, variable=self.valorVel)
        self.slider.grid(row=9, column=4, padx=10, pady=5, columnspan=6)
        self.slider.config(width=15)

        self.una_letra = tk.Entry(self.SubFrame2)
        self.una_letra.grid(row=10, column=4, padx=10, pady=10, columnspan=3)
        self.una_letra.config(width=15)

        # (3.4)*****---------------------Frame 3 - Botones Set ---------------------*****#

        self.SubFrame3 = tk.LabelFrame(self.Frame3, text='Confirmar seleccion')
        self.botonSetRojo = tk.Button(self.SubFrame3, text='Set Rojo', bg='Red', fg='black', font=18
                                      , command= self.set_config_Rojo)
        self.botonSetRojo.grid(row=3, column=10, padx=10, pady=5, columnspan=6)
        self.botonSetRojo.config(width=15)

        self.botonSetAzul = tk.Button(self.SubFrame3, text='Set Azul', bg='blue', fg='black', font=18
                                      , command= self.set_config_Azul)
        self.botonSetAzul.grid(row=4, column=10, padx=10, pady=5, columnspan=6)
        self.botonSetAzul.config(width=15)

        self.botonSetNaranja = tk.Button(self.SubFrame3, text='Set Naranja', bg='orange', fg='black', font=18
                                         , command= self.set_config_Naranja)
        self.botonSetNaranja.grid(row=5, column=10, padx=10, pady=5, columnspan=6)
        self.botonSetNaranja.config(width=15)

        self.botonSetCeleste = tk.Button(self.SubFrame3, text='Set Celeste', bg='skyblue', fg='black', font=18
                                         , command= self.set_config_Celeste)
        self.botonSetCeleste.grid(row=6, column=10, padx=10, pady=5, columnspan=6)
        self.botonSetCeleste.config(width=15)

        self.botonSetFuncion = tk.Button(self.SubFrame3, text='Set Funcion', bg='green', fg='black', font=18
                                         , command= self.set_config_Funcion)
        self.botonSetFuncion.grid(row=7, column=10, padx=10, pady=5, columnspan=6)
        self.botonSetFuncion.config(width=15)

        self.botonSetOrientacion = tk.Button(self.SubFrame3, text='Set Orientacion', bg='yellow', fg='black', font=18
                                             , command= self.set_config_Orientacion)
        self.botonSetOrientacion.grid(row=8, column=10, padx=10, pady=5, columnspan=6)
        self.botonSetOrientacion.config(width=15)

        self.botonSetVelocidad = tk.Button(self.SubFrame3, text='Set Velocidad', bg='brown', fg='black', font=18
                                           , command= self.set_Velocidad)
        self.botonSetVelocidad.grid(row=9, column=10, padx=10, pady=5, columnspan=6)
        self.botonSetVelocidad.config(width=15)

        self.botonSetLetra = tk.Button(self.SubFrame3, text='Set Letra', bg='Grey', fg='black', font=18
                                       ,command= self.Set_caracter)
        self.botonSetLetra.grid(row=10, column=10, padx=10, pady=5, columnspan=6)
        self.botonSetLetra.config(width=15)

        self.SubFrame1.pack(side='left')
        self.SubFrame2.pack()
        self.SubFrame3.pack(side='right')
        self.Frame3.pack(side='bottom')
        self.Frame4.pack()
        self.ventana.mainloop()

if __name__ == "__main__":

    app = DisMouse()
    app.widgets()

