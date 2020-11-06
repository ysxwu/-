from socket import *

udp_sockte = socket(AF_INET,SOCK_DGRAM)

udp_sockte.bind(('0.0.0.0',8888))

print('等的花都謝了')
data,addr = udp_sockte.recvfrom(1024)
print(addr,'收到了消息',data.decode())


n = udp_sockte.sendto(b'sdfasf',addr)
print('發送了%d' % n)
