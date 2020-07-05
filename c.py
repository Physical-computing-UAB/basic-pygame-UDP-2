# in this example, all the data is sent and the process is blocked meanwhile
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.108', 8080))

data_str = '&' * 10 * 1024 * 1024  # 70 MB of data
data =bytes(data_str, 'utf-8')
print("{} data sent from {} orginal data".format(sock.send(data), len(data)))  # True
