# in this example, not all the data is sent, if the buffer is smaller than the
# total amount of data

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.108', 8080))
sock.setblocking(0)

data_str = '&' * 10 * 1024 * 1024  # 70 MB of data
data =bytes(data_str, 'utf-8')
print("{} data sent from {} orginal data".format(sock.send(data), len(data)))  # True
