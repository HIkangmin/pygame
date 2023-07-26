import pygame
import time

from Settings import *
from Storage import *


class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super(Cursor, self).__init__()
        self.image = pygame.image.load(path(IMAGES.CROSSHAIR))
        self.image = pygame.transform.scale(self.image , (100,100)  )
        self.rect = self.image.get_rect()
        self.reset()


    def reset(self):
        self.rect.center = pygame.mouse.get_pos()

    # 전투기 업데이트
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    # 전투기 그리기
    def draw(self, screen):
        screen.blit(self.image, self.rect)   
