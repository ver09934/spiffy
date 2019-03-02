# https://nerdparadise.com/programming/pygame/part6

import pygame
import time
from pygame.locals import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    x = 0

    while True:

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            x -= 1
        if keys[pygame.K_DOWN]:
            x += 1

        print(x)
        
main()