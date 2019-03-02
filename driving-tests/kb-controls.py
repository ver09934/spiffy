# https://nerdparadise.com/programming/pygame/part6

import pygame
import time
from pygame.locals import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    x = 0
    y = 0

    up = False
    down = False
    right = False
    left = False

    while True:

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    up = True
                if event.key == K_DOWN:
                    down = True
                if event.key == K_RIGHT:
                    right = True
                if event.key == K_LEFT:
                    left = True

            if event.type == KEYUP:
                if event.key == K_UP:
                    up = False
                if event.key == K_DOWN:
                    down = False
                if event.key == K_RIGHT:
                    right = False
                if event.key == K_LEFT:
                    left = False

        if up:
            y += 1
        if down:
            y -= 1
        if right:
            x += 1
        if left:
            x -= 1

        print("x: {} y: {}".format(x, y))
    
        time.sleep(0.05)
        
main()