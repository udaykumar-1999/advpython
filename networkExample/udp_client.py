import socket

msg_from_client = "hello udp server"

bytesToSend = str.encode(msg_from_client)

serverAddrPort = ('127.0.0.1', 20001)
buffersize = 1024

UDP_SERVER_SOCKET = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDP_SERVER_SOCKET.sendto(bytesToSend, serverAddrPort)

msg_from_server = UDP_SERVER_SOCKET.recvfrom(buffersize)

msg = "message from server {}".format(msg_from_server[0])

print(msg)