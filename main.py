import math
import pygame
h=0.05
dxdt = lambda x, y: 1
dydt = lambda x, y: math.sin(x)-y
k1x = lambda x, y: dxdt(x, y)
k1y = lambda x, y: dydt(x, y)
k2x = lambda x, y: dxdt(x+h/2*k1x(x, y), y+h/2*k1y(x, y))
k2y = lambda x, y: dydt(x+h/2*k1x(x, y), y+h/2*k1y(x, y))
k3x = lambda x, y: dxdt(x+h/2*k2x(x, y), y+h/2*k2y(x, y))
k3y = lambda x, y: dydt(x+h/2*k2x(x, y), y+h/2*k2y(x, y))
k4x = lambda x, y: dxdt(x+h*k3x(x, y), y+h*k3y(x, y))
k4y = lambda x, y: dydt(x+h*k3x(x, y), y+h*k3y(x, y))
kx = lambda x, y: h/6*(k1x(x, y)+2*k2x(x, y)+2*k3x(x, y)+k4x(x, y))
ky = lambda x, y: h/6*(k1y(x, y)+2*k2y(x, y)+2*k3y(x, y)+k4y(x, y))

l=31
scale = 800/(l+1)
arrow_angle = math.pi/10
arrow_length = 3

a=-10
b=10

pygame.init()
screen = pygame.display.set_mode((800, 800))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    a, b = a+kx(a, b), b+ky(a, b)
    print(a, b)
    for i in range(0, l):
        for j in range(0, l):
            x = i-(l-1)/2
            y = j-(l-1)/2
            dx = kx(x, y)
            dy = ky(x, y)   
            rx = x*scale+400
            ry = 800-y*scale-400
            rdx = dx*scale
            rdy = -dy*scale
            pygame.draw.line(screen, (0, 0, 0), (rx, ry), (rx+rdx, ry+rdy), width=1)
            angle = -math.atan2(rdy, rdx)-math.pi
            pygame.draw.line(screen, (0, 0, 0), (rx+rdx, ry+rdy), (rx+rdx+arrow_length*math.cos(-angle-arrow_angle), ry+rdy+arrow_length*math.sin(-angle-arrow_angle)))
            pygame.draw.line(screen, (0, 0, 0), (rx+rdx, ry+rdy), (rx+rdx+arrow_length*math.cos(-angle+arrow_angle), ry+rdy+arrow_length*math.sin(-angle+arrow_angle)))
    pygame.draw.circle(screen, (255, 0, 0), (a*scale+400, b*scale+400), 3, width=1)
    pygame.display.flip()
pygame.quit()
