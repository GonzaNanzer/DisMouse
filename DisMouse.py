import serial
import time

def DisMouse():
    for i in range(10):
        puerto = 'COM'+str(i)
        try:
            arduino = serial.Serial(puerto,9600)
            time.sleep(2)
            text = str(input('Lista de comandos aceptados: \n'
                             '1) hDm = Hola DisMouse,ingresa en el modo configuracion. \n'))
            arduino.write(text.encode())
            lectura = arduino.readline().decode()

            break
        except:
            print('No me pude conectar, intentare con otro puerto.')
            time.sleep(0.5)
    print(lectura)
    print("Se encuentra en el modo de configuracion. Los comandos aceptados: \n"
          "1) cDm = Chau DisMouse.  \n"
          "2) bA = Configuracion boton azul. \n"
          "3) bR = Configuracion boton rojo.\n"
          "4) bN = Configuracion boton naranja.\n"
          "5) bC = Configuracion boton celeste.\n"
          "6) bF = Configuracion botones de direccion.\n"
          "7) bO = Configuracion orientacion botones.\n")
    comando = str(input())
    arduino.write(comando.encode())
    lec = arduino.readline().decode()
    arduino.close()

if __name__ == "__main__":
    DisMouse()