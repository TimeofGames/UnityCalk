import socket

# Задаем адрес сервера
SERVER_ADDRESS = ('192.168.32.2', 5000)

# Настраиваем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(10)
print('server is running, please, press ctrl+c to stop')

# Слушаем запросы
while True:
    connection, address = server_socket.accept()
    print("new connection from {address}".format(address=address))

    data = connection.recv(1024)
    print(str(data))
    output=str(eval(data))
    print(output)
    connection.send(bytes(output, encoding='UTF-8'))

    connection.close()