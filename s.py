import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8080 if len(sys.argv) == 1 else int(sys.argv[1])
sock.bind(('192.168.1.108', port))
sock.listen(5)

buff_size = 2048

try:
    while True:
        conn, info = sock.accept()

        data = conn.recv(buff_size)
        while data:
            print(data)
            data = conn.recv(buff_size)
except KeyboardInterrupt:
    sock.close
