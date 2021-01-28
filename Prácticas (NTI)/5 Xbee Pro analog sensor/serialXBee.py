#python 3.7.1
import serial
from decimal import Decimal

#abrir el puerto serial para el receptor
ser = serial.Serial(port='/dev/ttyUSB1')
#leer la trama de 22 bytes que llegue por el puerto serial
aux = ser.read(22)

#Ejemplos de lecturas del puerto serial
#aux = b'~\x00\x12\x92\x00\x13\xa2\x00A[\x114\xff\xfe\xc1\x01\x00\x00\x08\x00\xbaV'
#aux = b'~\x00\x12\x92\x00\x13\xa2\x00A[\x114\xff\xfe\xc1\x01\x00\x00\x08\x00\xb7Y'

print(str(aux) + ' <- trama del Xbee')
#tomar sólo los valores del sensor
x = aux[-3:-1]
print(str(x) + '<- bytes del voltaje')

#reemplazar los símbolos que representan un valor hexadecimal
x2 = str(x).replace("x","")
x3 = str(x2).replace("\\","")

#separar los valores deseados de la trama
valor = x3[-5:-1]

#convertir a decimal
val = int(valor,16)
print(str(val) + ' <- valor decimal de los bytes')

#conversion a volts
Vmax = 3.3 #valor max posible del potenciometro
maxBits = 2**16 #numero de combinaciones de bits posibles
vPot = val*Vmax/maxBits  #voltaje del potenciometro
print (vPot)
print('%.2E' % Decimal(str(vPot)) + ' v medidos del potenciometro')

#cerrar el puero serial
ser.close()