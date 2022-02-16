import serial, time
import FuncionBotones

def SeleccionPueto():
    for i in range(10):
        puerto = 'COM'+str(i)
        try:
            arduino = serial.Serial(puerto,9600)
            time.sleep(0.5)

            """            text = str(input('Ingrese el comando que desea realizar: '))
            arduino.write(text.encode())
            lectura = arduino.readline().decode()
            print(lectura)
            arduino.close()"""
            break
        except:
            print('No me pude conectar, intentare con otro puerto.')
            time.sleep(2)
    return puerto


arduino = serial.Serial(SeleccionPueto(),9600)

text = str(input('Ingrese el comando que desea realizar: '))
arduino.write(text.encode('ascii'))
lectura = arduino.readline().decode('ascii')

com = str(input('Ingrese un comando: \n'))
FuncionBotones.ComandasHabilitados(com)




arduino.close()

