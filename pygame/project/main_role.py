import pygame
from pygame.locals import *


# create class
class Player(object):
    # initialize
    def __init__(self):
        self.bulletList = []
        player_image = r'C:\Users\woshi\PycharmProjects\untitled1\pygame\project\pikachu.jpg'
        self.image = pygame.image.load(player_image).convert()

        self.x = 200
        self.y = 600

        self.speed = 5
        self.playerName = 'player'

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


player = Player()
