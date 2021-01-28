#Python 3.7
import time
import random
from losantmqtt import Device

device_id = "5cdc2beaa23e5200092d630c"
app_access = "342a22e7-5cf7-44e8-8821-cee9f270260d"
app_secret = "b1aa40ed5b551dcc5d69615b8a744954375098c732dfdf2dabdf4e237b22081e"
dispositivo = Device(device_id,app_access,app_secret)

def on_command(device, command):
    print ("Comando recibido")
    print (command["name"])
    print (command["payload"])
dispositivo.add_event_observer("command", on_command)
dispositivo.connect(blocking=False)
if dispositivo.is_connected:
    print ("Conexion chida")
else:
    print ("Algo fallo lol")
while True:
    dispositivo.loop()
    if dispositivo.is_connected:
        pres = random.random()*1000 #hPa
        dispositivo.send_state({"Pres" : pres})
        print ("Se mando informacion de presion")
    time.sleep(1)