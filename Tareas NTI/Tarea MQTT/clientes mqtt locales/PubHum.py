#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#python 3.6
#Sensor Humedad
import random
import paho.mqtt.client as mqtt
import time

def sim_hum():
    #Función que simula un sensor se humedad.
    #Regresa un float aleatorio entre 0 y 100
    temperatura = random.random()*100
    return temperatura


def on_publish(client,userdata,result): 
    #Función que determina la acción del cliente al publicar un mensaje
    print("Datos publicados en TempHum")
    pass


broker="localhost" #dominio o IP del broker mqtt
port=1884 #puerto que se usará

client1= mqtt.Client(client_id="Humedad")  #instancia del cliente mqtt                        
client1.on_publish = on_publish   #asignar acciones al publicar
client1.connect(broker,port) #conectarse al broker mediante el puerto asignado

#Correr cliente indefinidamente, publicando un valor aleatorio
# de temperatura al tópico /TempHum cada 10 segundos
while True:
    ret= client1.publish("TempHum",sim_hum())
    time.sleep(10)