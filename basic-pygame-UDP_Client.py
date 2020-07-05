import pygame
import socket

width  = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0


# SETUP THE SOCKET
udp_host = "192.168.1.108"		# Host IP
# udp_host = "127.0.0.1"		# Host IPudp_port = 8080			        # specified port to connect
udp_port = 8080
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      # For UDP
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
        self.vel = 5



    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move_socket(self):
        keys = pygame.key.get_pressed()
        msg = None

        if keys[pygame.K_LEFT]:
            msg = b'L'

        if keys[pygame.K_RIGHT]:
            msg = b'R'

        if keys[pygame.K_UP]:
            msg = b'U'

        if keys[pygame.K_DOWN]:
            msg = b'D'

        if msg:
            sock.sendto(msg,(udp_host,udp_port))
            # data_c, addr_c = sock.recvfrom(1)
            # print("Received from server: ", addr_c, "the data", data_c)

        # self.rect = (self.x, self.y, self.width, self.height)


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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move_socket()
        redrawWindow(win, p)

main()
