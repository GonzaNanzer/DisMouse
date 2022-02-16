import serial
import time
"""
Primero enviar hDm para que Dismouse entre en modo configuracion
"""
for i in range(6):
    try:
        puerto = "COM" + str(i)
        serialArduino = serial.Serial(str(puerto),9600)
        time.sleep(1)
        while True:
            val = serialArduino.readline().decode('ascii')
            print(val)
            print('***************')
    except:
        print('No logre conectarme')

