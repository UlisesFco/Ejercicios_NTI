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
    arregloTodosRadios = json.loads(respuesta)
    #print(arregloTodosRadios)
    arregloTodosRadios.append({"hops":"-1","mac":macLocal,"next_hop":"null"})
    #for radio in arregloTodosRadios:
    #     print(radio['mac'])
    return arregloTodosRadios

#obtener valores de rssi, lqi y latencia de los radios cercanos
def val_rssi_lqi_latencia(macLocal):
    print("==================Valores de LQI y RSSI==================")
    wsnQuery ='{"id": "all_neighbours", "mac": \"'+macLocal+'\"}'
    start_time = time.time() #tiempo desde 1/1/1970 en segundos
    respuesta = envia_solicitud(wsnQuery)
    end_time = time.time()
    elapsed_time = end_time - start_time #en segundos
    desc = 0
    if elapsed_time > 1:
        desc = 1
    try:
        arregloTodosRadios = json.loads(respuesta)
        arrStats = []
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
    HOST, PORT = "148.205.37.122", 6000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    macLocal = "0002"
    sock.connect((HOST, PORT))

    #encabezados del archivo de valores separados por comas
    # titulos = 'ini_monit,mac,rssi,lqi,latencia'
    # print(titulos, end='\n', file=open("monitoreo.csv", "a"))

    temp = []
    int_t = 1 #segundos

    inicio = time.time()
    while 1:
        macs = ["0002","0004","0005","0006","0008","0010"]
        num = random.randint(0,5)
        num = 0
        macLocal = macs[num]
        radios = MAC_radios(macLocal)
        for r in radios:
            macLocal = r['mac']
            t_trans = time.time()-inicio #seg
            if  t_trans >= int_t:
                temp = val_rssi_lqi_latencia(macLocal)
                for radio in temp:
                    #formato para las observaciones
                    st = '{},{},{},{},{},{},{}'
                    st = st.format(radio['ini_monit'],radio['mac_local'],radio['mac_destino'],\
                    radio['rssi'], radio['lqi'],radio['latencia'],radio['desconexion'])
                    print(st, end='\n', file=open("monitoreo.csv", "a"))
                inicio = time.time() #seg
except KeyboardInterrupt:
    print('\nTerminación del programa por el usuario')
#cerrar el socket
sock.close()