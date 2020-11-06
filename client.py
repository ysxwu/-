from  socket import *

address = ('127.0.0.1',8888)


udp_socket = socket(AF_INET,SOCK_DGRAM)

msg = input('>>')
udp_socket.sendto(msg.encode(),address)
data,addr = udp_socket.recvfrom(1024)
print('從服務端收到: %s' % data.decode())

udp_socket.close()



