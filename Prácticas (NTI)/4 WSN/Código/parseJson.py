#Python 3.7.2
import json
import socket
import networkx as nx
import matplotlib.pyplot as plt

# Metodos
# Recibe un query para mandarlo y regresa el JSON de respuesta
def enviaSolicitud(query):
    try:    
        sock.sendall(wsnQuery.encode())    
        received = sock.recv(1024)
    except:
        print("Excepcion de comunicacion")
    return received

# Configuraciones y variables
HOST, PORT = "148.205.37.122", 6000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
macLocal = "0002"
sock.connect((HOST, PORT))

#Obtener las direcciones mac de todos los radios cercanos
print("==================Todas las mac de los radios==================")
wsnQuery ='{"id": "routes", "mac": \"'+macLocal+'\"}'
respuesta = enviaSolicitud(wsnQuery)
arregloTodosRadios = json.loads(respuesta)
arregloTodosRadios.append({"hops":"-1","mac":macLocal,"next_hop":"null"})
for radio in arregloTodosRadios:
    print(radio['mac'])

#Direcciones mac de las PC de la red
arregloTodasPC = []
print("==================Todas las mac de las PC==================")
for radio in arregloTodosRadios:
    wsnQuery ='{"id": "attached_devices", "mac": \"'+radio['mac']+'\"}'
    respuesta = enviaSolicitud(wsnQuery)
    if str(json.loads(respuesta)) != "[]"  :        
        arregloTodasPC.append(json.loads(respuesta))
for pcEnRed in arregloTodasPC:    
    print(pcEnRed[0]['mac'])

#Todas las rutas de mi nodo local
print("==================Todas las rutas del radio local==================")
wsnQuery ='{"id": "routes", "mac": \"'+macLocal+'\"}'
respuesta = enviaSolicitud(wsnQuery)
diccionarioRutas = {}
arregloRutas = []
arregloRutas = json.loads(respuesta)
print(arregloRutas)
for ruta in arregloRutas:
    diccionarioRutas[ruta['mac']] = []
    rutaAuxiliar = ruta
    i = 0
    while True:
        diccionarioRutas[ruta['mac']].append(rutaAuxiliar['next_hop'])
        wsnQuery = wsnQuery ='{"id": "routes", "mac": \"'+rutaAuxiliar['next_hop']+'\"}'
        respuestaActual = enviaSolicitud(wsnQuery)
        i+=1
        if i >= int(ruta['hops'])-1:
            break
        for subruta in json.loads(respuestaActual):
            if subruta['mac'] == ruta['mac']:
                rutaAuxiliar = subruta
                break
    print(diccionarioRutas[ruta['mac']])

#Dibujar grafo de conexiones
print("==================Dibujo del grafo==================")
topologia = nx.DiGraph()
for radio in arregloTodosRadios:
    topologia.add_node(radio['mac'])
    wsnQuery ='{"id": "routes", "mac": \"'+radio['mac']+'\"}'
    rutasIndiv = enviaSolicitud(wsnQuery)
    for ruta in json.loads(rutasIndiv):
        if ruta['hops'] == '1':
            topologia.add_edge(radio['mac'],ruta['mac'])
print("El número total de nodos en la red es de: "+str(topologia.number_of_nodes()))
print("El número total de enlaces entre los nodos es de: "+str(topologia.number_of_edges()))
nx.draw(topologia,with_labels=True)
plt.show()

#Cerrado del socket de conexion
sock.close()