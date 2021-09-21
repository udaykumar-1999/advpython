import socket

localIP = '127.0.0.1'
localport = 20001

bufferSize = 1024

msgFromServer = 'Hello UPD Client'

byteToSend = str.encode(msgFromServer)
UDP_SERVER_SOCKET = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDP_SERVER_SOCKET.bind((localIP, localport))

print("UDP server up and listening...")

while True:
    bytesAddressPair = UDP_SERVER_SOCKET.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    client_msg = "Message from client {}".format(message)
    ClientIP = "Client IP address {}".format(address)

    print(client_msg)
    print(ClientIP)
    UDP_SERVER_SOCKET.sendto(byteToSend, address)
