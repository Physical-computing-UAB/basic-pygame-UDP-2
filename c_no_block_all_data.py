# in this example,  all the data is sent,
# but we have the overhead of controlling the flux to the buffer
#  In the this example, select() blocks if there is no file descriptor that is
#  ready to work with

import errno
import select
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.108', 8080))
sock.setblocking(0)

data_str = 'foobar\n' * 1024 * 1024
data = bytes(data_str, 'utf-8')
data_size = len(data)
print ('Bytes to send: ', len(data))

total_sent = 0
while len(data):
    try:
        sent = sock.send(data)
        total_sent += sent
        data = data[sent:]
        # print ('Sending data')
    except socket.error as e:
        if e.errno != errno.EAGAIN:
            raise e
        print ('Blocking with', len(data), 'remaining')
        select.select([], [sock], [])  # This blocks until

assert total_sent == data_size  # True
