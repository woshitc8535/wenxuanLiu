#game project
import pygame,sys
from pygame import *


if __name__ == '__main__':
    screen=pygame.display.set_mode((1080,1480),0,32)
    bgImaeFile = r'C:\Users\woshi\PycharmProjects\untitled1\pygame\project\ID card.jpg'
    background = pygame.image.load(bgImaeFile).convert()
    while True:
        screen.blit(background,(0,0))
        pygame.display.update()


