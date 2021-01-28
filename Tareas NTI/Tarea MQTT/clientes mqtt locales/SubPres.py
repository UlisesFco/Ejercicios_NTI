#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python 3.6
#Cliente receptor -> Presión
import ssl
import sys
import paho.mqtt.client
 
def on_connect(client, userdata, flags, rc):
    #Función que determina que hace el cliente al conectarse
    print('Conectado (%s)' % client._client_id)
    client.subscribe(topic='Pres', qos=2) #conectarse al tópico /Pres
 
def on_message(client, userdata, message):
    #Función que determina que hará el cliente al detectar
    # que se envió un mensaje al tópico al que está suscrito
    print('------------------------------')
    print('Topico: %s' % message.topic)
    print('Carga: %s' % message.payload)
    print('Nivel de QoS: %d' % message.qos)
 
def main():
    #Instanciar el cliente
    client = paho.mqtt.client.Client(client_id='CliPres', clean_session=False)
    client.on_connect = on_connect #asignar acciones al conectarse
    client.on_message = on_message #asignar acciones al detectar el envío de mensajes
    client.connect(host='localhost', port=1884) #conectarse al host por el puerto asignado
    client.loop_forever() #dejar el cliente activo indefinidamente
 
main()
sys.exit(0)