#Python 3.7.2
import json
import socket
import time
import random

# Metodos
# Recibe un query para mandarlo y regresa el JSON de respuesta
def envia_solicitud(query):
    try:    
        sock.sendall(query.encode())    
        received = sock.recv(1024)
        return received
    except:
        print("Excepcion de comunicacion")
    

#Obtener las direcciones mac de todos los radios cercanos
def MAC_radios(macLocal):
    #print("==================Todas las mac de los radios==================")
    wsnQuery ='{"id": "routes", "mac": \"'+macLocal+'\"}'
    respuesta = envia_solicitud(wsnQuery)
    arregloTodosRadios = json.loads(respuesta.decode('utf-8'))
    #print(arregloTodosRadios)
    arregloTodosRadios.append({"hops":"-1","mac":macLocal,"next_hop":"null"})
    #for radio in arregloTodosRadios:
    #     print(radio['mac'])
    return arregloTodosRadios

#obtener valores de rssi, lqi y latencia de los radios cercanos
def val_rssi_lqi_latencia(macLocal):
    wsnQuery ='{"id": "all_neighbours", "mac": \"'+macLocal+'\"}'
    start_time = time.time() #tiempo desde 1/1/1970 en segundos
    respuesta = envia_solicitud(wsnQuery)
    end_time = time.time()
    elapsed_time = end_time - start_time #en segundos
    desc = 0 #estado de conexion
    if elapsed_time > 1:
        desc = 1
    try:
        arregloTodosRadios = json.loads(respuesta.decode('utf-8'))
        arrStats = []
        #arreglo para los radios conectados
        for radio in arregloTodosRadios:
            print(radio['mac'])
            #diccionario con las mediciones
            dicEstado = {
                "ini_monit" : str(time.ctime(start_time)),
                "mac_local" : macLocal,
                "mac_destino": radio['mac'],
                "rssi" : radio['rssi'],
                "lqi" : radio['lqi'],
                "latencia" : str(elapsed_time),
                "desconexion": desc
            }
            arrStats.append(dicEstado)
        return arrStats
    except:
        pass 
    else:
        #diccionario para radio desconectado / no disponible
        print("Radio " + macLocal + " no disponible")
        dicEstado = {
                "ini_monit" : str(time.ctime(start_time)),
                "mac_local" : macLocal,
                "mac_destino": radio['mac'],
                "rssi" : None,
                "lqi" : None,
                "latencia" : None,
                "desconexion": 1
        }
        arrStats = []
        arrStats.append(dicEstado)
        return arrStats     


try:
    # Configuraciones y variables

    #encabezados del archivo de valores separados por comas
    # titulos = 'ini_monit,mac,rssi,lqi,latencia'
    # print(titulos, end='\n', file=open("monitoreo.csv", "a"))

    temp = []
    #intervalo de tiempo
    int_t = 60*5#segundos

    #inicio = time.time()
    #macs de los radios encontrados
    #macs = ["0002","0004","0005","0006","0008","0010","0014"] 
    macs = ["0002","0004","0005","0006","0010","0014"]
    while 1:
        num = random.randint(0,5)
        macLocal = macs[num]
        HOST, PORT = "148.205.37.122", 6000
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))

        #para lo radios encontrados busca sus estadisticas
        temp = val_rssi_lqi_latencia(macLocal)
        if temp != None:
            for radio in temp:
                #formato para las observaciones
                st = '{},{},{},{},{},{},{}'
                st = st.format(radio['ini_monit'],str(macs[num]),radio['mac_destino'],\
                radio['rssi'], radio['lqi'],radio['latencia'],radio['desconexion'])
                print(st, end='\n', file=open("monitoreo.csv", "a"))
        #esperar por int_t segundos
        time.sleep(int_t)
        sock.close()
except KeyboardInterrupt:
    print('\nTerminación del programa por el usuario')
#cerrar el socket
sock.close()