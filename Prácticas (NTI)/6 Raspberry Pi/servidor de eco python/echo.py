# Ejemplo de servidor de eco
# ejecutar antes de echo_cli.py

import socket

def listen():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('localhost', 5555))
    connection.listen(10)
    while True:
        current_connection, address = connection.accept()
        while True:
            data = current_connection.recv(2048)
            if data == 'quit\r\n' or data == 'salir':
                current_connection.shutdown(1)
                current_connection.close()
                break

            elif data == 'stop\r\n' or data == 'parar':
                current_connection.shutdown(1)
                current_connection.close()
                exit()

            elif data:
                current_connection.send(data)
                print (data)


if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass