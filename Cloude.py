import pygame
import time

from Settings import *
from Storage import *

# 구름 객체
class Cloud(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Cloud, self).__init__()

        self.image = pygame.image.load(path(IMAGES.CLOUD_01))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

    # 구름 업데이트
    def update(self):
         self.rect.x += self.speed

   
    # 구름 그리기
    def draw(self, screen):
        if self.rect.x > SCREEN_WIDTH:
             self.rect.x = -self.image.get_width()
        screen.blit(self.image, self.rect)
