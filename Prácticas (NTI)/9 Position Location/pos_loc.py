#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Práctica 9 - Nuevas Tecnologías Inalámbricas

from sklearn.neighbors import NearestNeighbors
import numpy as np
import mysql.connector

def consulta_actual(tag,fecha,hora,mydb):
    #Consulta el promedio de las mediciones del radio después
    # de cierta hora dada en cierto día
    #Tag es un string como EB0x, x un número entre 1 y 4
    #Fecha es un string en formato aaaa-mm-dd
    #hora es un string en formato hh:mm:ss en formato de 24 horas
    #mydb es un objeto de base de datos de mysql
    try:
        cursor = mydb.cursor()
        query = "select node,avg(rssi) as avg_rssi FROM taglogs.tagmessages \
        where taglogs.tagmessages.tag = '" + tag + "' and \
        taglogs.tagmessages.date =str_to_date('" + fecha + "','%Y-%m-%d') and \
        taglogs.tagmessages.time >= cast(('" + hora + "') as time(0)) \
        group by node \
        order by node"
        cursor.execute(query)
        datos = cursor.fetchall()
        actual = []
        for tupla in datos:
            actual.append(tupla[1])
    except Exception:
        print('Error al hacer la consulta')
    cursor.close()
    return actual

#crear objeto de base de datos de mysql
mydb = mysql.connector.connect(
    host="148.205.37.150",
    user="team3",
    passwd="team3nti#",
    database = "taglogs")
#crear cursor para la bd
mycursor = mydb.cursor()

#obtener los datos de la medición para estimar la ubicacion
actual = consulta_actual('EB03','2019-03-20','11:40:00',mydb)
print('N0004: ' + str(actual[0]) + '\n')
print('N0005: ' + str(actual[1]) + "\n")
print('N0006: ' + str(actual[2]) + "\n")
print('N0007: ' + str(actual[3]) + "\n")
print('N0014: ' + str(actual[4]) + "\n")

#consultar los datos de entrenamiento
consulta = "SELECT * FROM taglogs.rssi_averages"
mycursor.execute(consulta)
prueba = mycursor.fetchall()

#crear los arreglos con datos y ubicaciones
arregloNumeros = [actual]
arregloUbicacion = []

#meter los datos al arreglo
for tupla in prueba:
    arregloNumeros.append(tupla[3:])
    arregloUbicacion.append(tupla[2])
arregloNumerosNP = np.array(arregloNumeros)

#usar el algoritmo kNN para encontrar los vecinos cercanos, usando la librería sklearn 
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(arregloNumerosNP)
#arreglos de índices y distancias de los vecinos más cercanos
distancias, indices = nbrs.kneighbors(arregloNumerosNP)

#cerrar cursores y bases de datos
mycursor.close()
mydb.close()

#determinar la ubicación a partir de los índices
ubicacion = arregloUbicacion[indices[0][1] - 1]
lugar = ''
if ubicacion[0] == 'F':
    lugar = 'Física'
elif ubicacion[0] == 'S':
    lugar = 'Señales'
elif ubicacion[0] == 'A': 
    lugar = 'Circuitos Lógicos'
else:
    lugar = 'Pasillo'

print("Estimación de ubicación del radio en " + lugar + ", celda " + ubicacion)