import socket

#funcion para mandar info que sirve junto con echo.py
#ejecutar después de echo.py
def publish(msg=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost',5555)
    sock.connect(server_address)
    if msg != None:
        msg = msg.encode()
        print('Enviando mensaje ...')
        sock.sendall(msg)
        print('... Saliendo del programa')
        sock.close()
        #sock.shutdown(1)
    else:
        while True:
            print('Escriba salir para terminar el programa')
            msg = input('Escriba su mensaje:\n')
            if msg == 'salir':
                print('... Saliendo del programa')
                sock.close()
                #sock.shutdown(1)
                break
            msg = msg.encode()
            sock.sendall(msg)


#publish()