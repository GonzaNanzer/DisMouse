#%%--------------Funcion Botones----------------

def ChauDisMouse(LecturaArduino):
    arduino = LecturaArduino
    cDmtext = 'cDm'
    print(arduino.write(cDmtext.encode('ascii')))
    lectura = arduino.readline().decode('ascii')
    print(lectura)
    return lectura

#%%--------------Funcion Boton Rojo----------------

def BotonRojo(LecturaArduino):
    """

    :param LecturaArduino: Recibe informacion del arduino
    :return: Ingresa al modo de configuracion del boton rojo
    """
    arduino = LecturaArduino
    bRtext = 'bR'
    print(arduino.write(bRtext.encode('ascii')))
    lectura = arduino.readline().decode('ascii')
    print(lectura)
    return lectura

#%%--------------Funcion Boton Azul----------------
def BotonAzul(LecturaArduino):
    """
    :param LecturaArduino: Recibe informacion del arduino
    :return: Ingresa al modo de configuracion del boton Azul
    """
    arduino = LecturaArduino
    bAtext = 'bA'
    print(arduino.write(bAtext.encode('ascii')))
    lectura = arduino.readline().decode('ascii')
    print(lectura)
    return lectura

#%%--------------Funcion Boton Celeste----------------

def BotonCeleste(LecturaArduino):
    """

    :param LecturaArduino: Recibe informacion del arduino
    :return: Ingresa al modo de configuracion del boton Celeste
    """
    arduino = LecturaArduino
    bCtext = 'bC'
    print(arduino.write(bCtext.encode('ascii')))
    lectura = arduino.readline().decode('ascii')
    print(lectura)
    return lectura

#%%--------------Funcion Boton Naranja----------------

def BotonNaranja(LecturaArduino):
    """

    :param LecturaArduino: Recibe informacion del arduino
    :return: Ingresa al modo de configuracion del boton Naranja
    """
    arduino = LecturaArduino
    bNtext = 'bN'
    print(arduino.write(bNtext.encode('ascii')))
    lectura = arduino.readline().decode('ascii')
    print(lectura)
    return lectura


#%%--------------Funcion Boton Amarillo (Funcion) ----------------

def BotonNaranja(LecturaArduino):
    """

    :param LecturaArduino: Recibe informacion del arduino
    :return: Ingresa al modo de configuracion del boton Amarillo (Funcion)
    """
    arduino = LecturaArduino
    bFtext = 'bF'
    print(arduino.write(bFtext.encode('ascii')))
    lectura = arduino.readline().decode('ascii')
    print(lectura)
    return lectura


#%%--------------Funcion Boton Amarillo (Orientacion)----------------

def BotonNaranja(LecturaArduino):
    """

    :param LecturaArduino: Recibe informacion del arduino
    :return: Ingresa al modo de configuracion del boton Amarillo (Orientacion)
    """
    arduino = LecturaArduino
    bOtext = 'bO'
    print(arduino.write(bOtext.encode('ascii')))
    lectura = arduino.readline().decode('ascii')
    print(lectura)
    return lectura


#%%-------------- Comandos Validos de Operacion ---------------
def ComandasHabilitados(comando):
    coms = ['bA','bR','bN','bC','bF','bO','cDm']
    while True:
        try:
            if comando in coms:
                print('comando valido')
                return comando
            else:
                print('Comando no valido, intentelo de nuevo')

