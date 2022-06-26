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
            self.botonConfig['state'] = 'normal'
            self.botonSalirConfig['state'] = 'normal'
            pass
        else:
            print('No me puedo conectar')

    def leer_dato(self):
        if self.arduino.isOpen():
            print(self.arduino.readline().decode())
        else:
            print('no estoy conectado')

    def Set_caracter(self):
        text = str(self.una_letra.get())
        self.arduino.write(text.encode('ascii'))
        print(text)
        return

    def cerrar_ventana(self):
        return self.raiz2.destroy()

    def nueva_ventana(self):
        if self.arduino.isOpen():
            self.raiz2 = tk.Toplevel()
            self.FrameVentana = tk.LabelFrame(self.raiz2)
            self.n = DisMouse(master=self.raiz2)
            self.raiz2.title('IMPORTANTE')
            self.label = tk.Label(self.FrameVentana, text='Para ingresar un caracter digitelo en la ventana de texto '
                                                          'ubicada en la parte inferior\n de la ventana principal en la seccion configuracion caracter.'
                                                          '\nPosteriormente presione el boton Set Letra.\n Para continuar presione Aceptar!')
            self.label.grid(row=1, column=0)
            self.button = tk.Button(self.FrameVentana, text='Aceptar!', bg='Grey', fg='black', font=10,
                                    command=self.cerrar_ventana)
            self.button.grid(row=3, column=0)
            self.raiz2.grab_set()
            self.FrameVentana.pack()
            pass
        else:
            pass
        return

    def HolaDisMouse(self):
        com = 'hDm'
        self.arduino.write(com.encode('ascii'))

        self.botonRojo['state'] = 'normal'
        self.combobox_Rojo['state'] = 'normal'
        self.botonSetRojo['state'] = 'normal'

        self.botonAzul['state'] = 'normal'
        self.combobox_Azul['state'] = 'normal'
        self.botonSetAzul['state'] = 'normal'

        self.botonNaranja['state'] = 'normal'
        self.combobox_Naranja['state'] = 'normal'
        self.botonSetNaranja['state'] = 'normal'

        self.botonCeleste['state'] = 'normal'
        self.combobox_Celeste['state'] = 'normal'
        self.botonSetCeleste['state'] = 'normal'

        self.botonFunciones['state'] = 'normal'
        self.combobox_Funcion['state'] = 'normal'
        self.botonSetFuncion['state'] = 'normal'

        self.botonOrientacion['state'] = 'normal'
        self.combobox_Orientacion['state'] = 'normal'
        self.botonSetOrientacion['state'] = 'normal'

        self.botonVelocidad['state'] = 'normal'
        self.slider['state'] = 'normal'
        self.botonSetVelocidad['state'] = 'normal'

        self.botonSetLetra['state'] = 'active'
        self.una_letra['state'] = 'normal'
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
            self.arduino.write(com.encode('ascii'))
            self.nueva_ventana()
        if com == '10':
            com = 'a'
            self.arduino.write(com.encode('ascii'))
        if com == '11':
            com = 'b'
            self.arduino.write(com.encode('ascii'))
        if com == '12':
            com = 'c'
            self.arduino.write(com.encode('ascii'))
        else:
            self.arduino.write(com.encode('ascii'))
        return

    def set_config_Azul(self):
        com = str(self.combobox_Azul.current() + 1)
        if com == '7':
            self.arduino.write(com.encode('ascii'))
            self.nueva_ventana()
        if com == '10':
            com = 'a'
            self.arduino.write(com.encode('ascii'))
        if com == '11':
            com = 'b'
            self.arduino.write(com.encode('ascii'))
        if com == '12':
            com = 'c'
            self.arduino.write(com.encode('ascii'))
        else:
            self.arduino.write(com.encode('ascii'))
        return

    def set_config_Naranja(self):
        com = str(self.combobox_Naranja.current() + 1)
        if com == '7':
            self.arduino.write(com.encode('ascii'))
            self.nueva_ventana()
        if com == '10':
            com = 'a'
            self.arduino.write(com.encode('ascii'))
        if com == '11':
            com = 'b'
            self.arduino.write(com.encode('ascii'))
        if com == '12':
            com = 'c'
            self.arduino.write(com.encode('ascii'))
        else:
            self.arduino.write(com.encode('ascii'))
        return

    def set_config_Celeste(self):
        com = str(self.combobox_Celeste.current() + 1)
        if com == '7':
            self.arduino.write(com.encode('ascii'))
            self.nueva_ventana()
        if com == '10':
            com = 'a'
            self.arduino.write(com.encode('ascii'))
        if com == '11':
            com = 'b'
            self.arduino.write(com.encode('ascii'))
        if com == '12':
            com = 'c'
            self.arduino.write(com.encode('ascii'))
        else:
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
        com = self.valorVel.get()
        print(com)
        str(self.arduino.write(com.encode('ascii')))
        return

    def ChauDisMouse(self):
        com = 'cDm'
        self.arduino.write(com.encode('ascii'))
        self.leer_dato()

        self.botonRojo['state'] = 'disable'
        self.combobox_Rojo['state'] = 'disable'
        self.botonSetRojo['state'] = 'disable'

        self.botonAzul['state'] = 'disable'
        self.combobox_Azul['state'] = 'disable'
        self.botonSetAzul['state'] = 'disable'

        self.botonNaranja['state'] = 'disable'
        self.combobox_Naranja['state'] = 'disable'
        self.botonSetNaranja['state'] = 'disable'

        self.botonCeleste['state'] = 'disable'
        self.combobox_Celeste['state'] = 'disable'
        self.botonSetCeleste['state'] = 'disable'

        self.botonFunciones['state'] = 'disable'
        self.combobox_Funcion['state'] = 'disable'
        self.botonSetFuncion['state'] = 'disable'

        self.botonOrientacion['state'] = 'disable'
        self.combobox_Orientacion['state'] = 'disable'
        self.botonSetOrientacion['state'] = 'disable'

        self.botonVelocidad['state'] = 'disable'
        self.slider['state'] = 'disable'
        self.botonSetVelocidad['state'] = 'disable'

        self.botonSetLetra['state'] = 'disable'
        self.una_letra['state'] = 'disable'

        self.botonSalirConfig['state'] = 'disable'

        self.arduino.close()
        return


    def widgets(self):

        # (1)*****---------------------Frame 1---------------------*****#

        # (1.1)*****---------------------Conectar tu dispositivo---------------------*****#

        self.ventana = tk.Tk()
        self.ventana.title('Configurador de disMouse v1.0')
        #self.ventana.iconbitmap(r'..\DisMouse\DisMouseIco.ico')
        self.ventana.resizable(False,False)

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
        self.botonConfig['state'] = 'disabled'

        self.botonSalirConfig = tk.Button(self.Frame2, text='Salir del Modo Configuracion', bg='Grey', fg='black', font=10
                                          , command= self.ChauDisMouse)
        self.botonSalirConfig.grid(row=1, column=10, pady=5, columnspan=5)
        self.botonSalirConfig.config(width=24)
        self.botonSalirConfig['state'] = 'disabled'
        self.Frame2.pack()

        # (3)*****---------------------Frame 3---------------------*****#

        # (3.1)*****---------------------Frame 3 - Botones ---------------------*****#

        self.Frame3 = tk.LabelFrame(self.ventana, text='Configura tu disMouse')

        self.Frame4 = tk.Frame(self.Frame3)

        # (3.2)*****---------------------Frame 3 - Botones Rojo---------------------*****#

            # (3.2.1    )*****---------------------Frame 3 - Botones ---------------------*****#
        self.SubFrame1 = tk.LabelFrame(self.Frame3, text='Configuracion boton rojo')

        self.botonRojo = tk.Button(self.SubFrame1, text='Boton Rojo', bg='red', fg='black', font=18
                                   , command= self.BotonRojo)
        self.botonRojo.grid(row=3, column=1, padx=10, pady=5, columnspan=3)
        self.botonRojo.config(width=15)

        OpBotones = ['Clic izquierdo', 'Clic derecho', 'Clic central', 'Barra espaciadora', 'Tecla enter', 'Doble clic',
                     'Una letra', 'Anular boton', 'Tecla Tab', 'F1', 'F2', 'F3']
        self.combobox_Rojo = ttk.Combobox(self.SubFrame1)
        self.combobox_Rojo['values'] = OpBotones
        self.combobox_Rojo.config(width=15)
        self.combobox_Rojo.grid(row=3, column=4, padx=10, pady=10, columnspan=3)
        self.combobox_Rojo.current(0)


        self.botonSetRojo = tk.Button(self.SubFrame1, text='Set Rojo', bg='Red', fg='black', font=18
                                      , command= self.set_config_Rojo)
        self.botonSetRojo.grid(row=3, column=10, padx=10, pady=5, columnspan=6)
        self.botonSetRojo.config(width=15)

        self.botonRojo['state'] = 'disabled'
        self.combobox_Rojo['state'] = 'disabled'
        self.botonSetRojo['state'] = 'disabled'

        # (3.2.3    )*****---------------------Frame 3 - Botones Azul ---------------------*****#

        self.SubFrame2 = tk.LabelFrame(self.Frame3, text='Configuracion boton azul')

        self.botonAzul = tk.Button(self.SubFrame2, text='Boton Azul', bg='blue', fg='black', font=18
                                   , command=self.BotonAzul)
        self.botonAzul.grid(row=4, column=1, padx=10, pady=5, columnspan=3)
        self.botonAzul.config(width=15)


        self.combobox_Azul = ttk.Combobox(self.SubFrame2)
        self.combobox_Azul['values'] = OpBotones
        self.combobox_Azul.config(width=15)
        self.combobox_Azul.grid(row=4, column=4, padx=10, pady=10, columnspan=3)
        self.combobox_Azul.current(1)

        self.botonSetAzul = tk.Button(self.SubFrame2, text='Set Azul', bg='blue', fg='black', font=18
                                      , command= self.set_config_Azul)
        self.botonSetAzul.grid(row=4, column=10, padx=10, pady=5, columnspan=6)
        self.botonSetAzul.config(width=15)

        self.botonAzul['state'] = 'disabled'
        self.combobox_Azul['state'] = 'disabled'
        self.botonSetAzul['state'] = 'disabled'

        # (3.2.3    )*****---------------------Frame 3 - Botones Naranja ---------------------*****#

        self.SubFrame3 = tk.LabelFrame(self.Frame3, text='Configuracion boton naranja')

        self.botonNaranja = tk.Button(self.SubFrame3, text='Boton Naranja', bg='orange', fg='black', font=18
                                      , command=self.BotonNaranja)
        self.botonNaranja.grid(row=5, column=1, padx=10, pady=5, columnspan=3)
        self.botonNaranja.config(width=15)


        self.combobox_Naranja = ttk.Combobox(self.SubFrame3)
        self.combobox_Naranja['values'] = OpBotones
        self.combobox_Naranja.config(width=15)
        self.combobox_Naranja.grid(row=5, column=4, padx=10, pady=10, columnspan=3)
        self.combobox_Naranja.current(5)

        self.botonSetNaranja = tk.Button(self.SubFrame3, text='Set Naranja', bg='orange', fg='black', font=18
                                         , command= self.set_config_Naranja)
        self.botonSetNaranja.grid(row=5, column=10, padx=10, pady=5, columnspan=6)
        self.botonSetNaranja.config(width=15)

        self.botonNaranja['state'] = 'disabled'
        self.combobox_Naranja['state'] = 'disabled'
        self.botonSetNaranja['state'] = 'disabled'

        # (3.2.4    )*****---------------------Frame 3 - Botones Celeste ---------------------*****#

        self.SubFrame4 = tk.LabelFrame(self.Frame3, text='Configuracion boton naranja')

        self.botonCeleste = tk.Button(self.SubFrame4, text='Boton Celeste', bg='skyblue', fg='black', font=18
                                      , command= self.BotonCeleste)
        self.botonCeleste.grid(row=6, column=1, padx=10, pady=5, columnspan=3)
        self.botonCeleste.config(width=15)

        self.combobox_Celeste = ttk.Combobox(self.SubFrame4)
        self.combobox_Celeste['values'] = OpBotones
        self.combobox_Celeste.config(width=15)
        self.combobox_Celeste.grid(row=6, column=4, padx=10, pady=10, columnspan=3)
        self.combobox_Celeste.current(4)

        self.botonSetCeleste = tk.Button(self.SubFrame4, text='Set Celeste', bg='skyblue', fg='black', font=18
                                         , command= self.set_config_Celeste)
        self.botonSetCeleste.grid(row=6, column=10, padx=10, pady=5, columnspan=6)
        self.botonSetCeleste.config(width=15)

        self.botonCeleste['state'] = 'disabled'
        self.combobox_Celeste['state'] = 'disabled'
        self.botonSetCeleste['state'] = 'disabled'

               # (3.2.5   )*****---------------------Frame 3 - Botones Funciones ---------------------*****#

        self.SubFrame5 = tk.LabelFrame(self.Frame3, text='Configuracion botones amarillos')

        self.botonFunciones = tk.Button(self.SubFrame5, text='Amarillos', bg='Yellow', fg='black', font=18
                                        , command= self.BotonFunciones)
        self.botonFunciones.grid(row=7, column=1, padx=10, pady=5, columnspan=3)
        self.botonFunciones.config(width=15)

        OpBotonF = ['Desplazan el cursor', 'Simulan flechas']

        self.combobox_Funcion = ttk.Combobox(self.SubFrame5)
        self.combobox_Funcion['values'] = OpBotonF
        self.combobox_Funcion.config(width=15)
        self.combobox_Funcion.grid(row=7, column=4, padx=10, pady=10, columnspan=3)
        self.combobox_Funcion.current(0)

        self.botonSetFuncion = tk.Button(self.SubFrame5, text='Set Amarillos', bg='Yellow', fg='black', font=18
                                         , command= self.set_config_Funcion)
        self.botonSetFuncion.grid(row=7, column=10, padx=10, pady=5, columnspan=6)
        self.botonSetFuncion.config(width=15)

        self.botonFunciones['state'] = 'disabled'
        self.combobox_Funcion['state'] = 'disabled'
        self.botonSetFuncion['state'] = 'disabled'

               # (3.2.6    )*****---------------------Frame 3 - Botones orientacion ---------------------*****#

        self.SubFrame6 = tk.LabelFrame(self.Frame3, text='Configuracion orientacion')

        self.botonOrientacion = tk.Button(self.SubFrame6, text='Orientacion', bg='yellow', fg='black', font=18
                                          , command= self.BotonOrientacion)
        self.botonOrientacion.grid(row=8, column=1, padx=10, pady=5, columnspan=3)
        self.botonOrientacion.config(width=15)


        OpBotonO = ['Posicion normal', 'Rotar 90° horario', 'Rotar 90° anti-horario', 'Rotar 180°']

        self.combobox_Orientacion = ttk.Combobox(self.SubFrame6)
        self.combobox_Orientacion['values'] = OpBotonO
        self.combobox_Orientacion.config(width=15)
        self.combobox_Orientacion.grid(row=8, column=4, padx=10, pady=10, columnspan=3)
        self.combobox_Orientacion.current(0)



        self.botonSetOrientacion = tk.Button(self.SubFrame6, text='Set Orientacion', bg='yellow', fg='black', font=18
                                             , command= self.set_config_Orientacion)
        self.botonSetOrientacion.grid(row=8, column=10, padx=10, pady=5, columnspan=6)
        self.botonSetOrientacion.config(width=15)

        self.botonOrientacion['state'] = 'disabled'
        self.combobox_Orientacion['state'] = 'disabled'
        self.botonSetOrientacion['state'] = 'disabled'

               # (3.2.7    )*****---------------------Frame 3 - Botones Velocidad---------------------*****#

        self.SubFrame7 = tk.LabelFrame(self.Frame3, text='Configuracion velocidad')

        self.botonVelocidad = tk.Button(self.SubFrame7, text='Velocidad cursor', bg='brown', fg='black', font=18
                                        , command=self.BotonVelocidad)
        self.botonVelocidad.grid(row=9, column=1, padx=10, pady=5, columnspan=3)
        self.botonVelocidad.config(width=15)

        self.valorVel = tk.StringVar()
        self.slider = tk.Scale(self.SubFrame7, from_=5, to=50, orient='horizontal',
                           length=100, variable=self.valorVel)
        self.slider.grid(row=9, column=4, padx=10, pady=5, columnspan=6)
        self.slider.config(width=15)

        self.botonSetVelocidad = tk.Button(self.SubFrame7, text='Set Velocidad', bg='brown', fg='black', font=18
                                           , command= self.set_Velocidad)
        self.botonSetVelocidad.grid(row=9, column=10, padx=10, pady=5, columnspan=6)
        self.botonSetVelocidad.config(width=15)

        self.botonVelocidad['state'] = 'disabled'
        self.slider['state'] = 'disabled'
        self.botonSetVelocidad['state'] = 'disabled'

               # (3.2.8    )*****---------------------Frame 3 - Botones orientacion ---------------------*****#

        self.SubFrame8 = tk.LabelFrame(self.Frame3, text='Configuracion caracter')

        self.botonNull = tk.Button(self.SubFrame8)
        self.botonNull.grid(row=10, column=1, padx=10, pady=5, columnspan=3)
        self.botonNull.config(width=15)

        self.una_letra = tk.Entry(self.SubFrame8)
        self.una_letra.grid(row=10, column=4, padx=10, pady=10, columnspan=3)
        self.una_letra.config(width=15)

        self.botonSetLetra = tk.Button(self.SubFrame8, text='Set Letra', bg='Grey', fg='black', font=18
                                       ,command= self.Set_caracter)
        self.botonSetLetra.grid(row=10, column=10, padx=15, pady=5, columnspan=6)
        self.botonSetLetra.config(width=15)

        self.botonSetLetra['state'] = 'disabled'
        self.una_letra['state'] = 'disabled'

        self.SubFrame1.pack()
        self.SubFrame2.pack()
        self.SubFrame3.pack()
        self.SubFrame4.pack()
        self.SubFrame5.pack()
        self.SubFrame6.pack()
        self.SubFrame7.pack()
        self.SubFrame8.pack()
        self.Frame3.pack()
        self.Frame4.pack()
        self.ventana.mainloop()


if __name__ == "__main__":

    app = DisMouse()
    app.widgets()