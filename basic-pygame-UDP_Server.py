import pygame
import socket

width  = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0
buff_size = 1

# SETUP THE SOCKET
udp_host = "192.168.1.108"		# Host IP
# udp_host = "127.0.0.1"		# Host IPudp_port = 8080			        # specified port to connect
udp_port = 8080
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      # For UDP
sock.bind((udp_host,udp_port))
print("Waiting for client...")


#                 # specified port to connect
#
# msg = b"Hello Python!"
# print ("UDP target IP:", udp_host)
# print ("UDP target Port:", udp_port)

# sock.sendto(msg,(udp_host,udp_port))




class Player():
    def __init__(self, x,y, width, height, color):
        self.x = x
        self.y = x
        self.width = width
        self.height = height
        self.color = color
        self.rect= (x,y,width, height)
        self.vel = 3



    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move_socket(self):
        data,addr = sock.recvfrom(buff_size)	        #receive data from client
        print ("Received Messages:",data," from",addr, "wihe len: ", len(data))
        msg = None

        if data == b'L':
            self.x -= self.vel
        elif data == b'R':
            self.x += self.vel
        elif data == b'U':
            self.y -= self.vel
        elif data == b'D':
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)


    def move_keyboard(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)


def redrawWindow(win, player):

    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()

def main():
    run = True
    p = Player(50, 50, 100, 100, (0,255,0))



    while run:
        # we change the typy of interaction here.
        # instead of waiting for a key,
        # we wait for a client.
        # The difference is:
        # KEYS: if a key event is not received, the loop resumes
        # SOCKET: if the client is not sendind data AND the data is receved,
        #   the loop is BLOCKED.
        #


        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False
        #         pygame.quit()



        p.move_socket()
        redrawWindow(win, p)
        print("/")

main()
