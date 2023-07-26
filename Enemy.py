
import pygame
import random
import os

import Storage
from Settings import *


# 암석 객체
class Enemy(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Enemy, self).__init__()
        rock_images_path = Storage.path('assets/images/npc/player')
        image_file_list = os.listdir(rock_images_path)
        self.image_path_list = [os.path.join(rock_images_path, file)
                                for file in image_file_list if file.endswith(".png")]
        choice_rock_path = random.choice(self.image_path_list)
        self.images = []
        for image_path in self.image_path_list :
            self.images.append(pygame.image.load(image_path).convert_alpha())
        
        self.index = 0
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
        self.time_delay = 0.2
        self.current_time = 0        
        self.delta_time = 0
        self.current_time1 = 0
        self.last_shot_time = 3

        
    # 애니메이션 설정
    def update(self, delta_time):
        self.current_time += delta_time
        if self.current_time >= self.time_delay:
            self.current_time = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            self.image = pygame.transform.scale(self.image, (60,60))
    def addshot(self, delta_time):
        self.current_time1 += delta_time
        if self.current_time1 >= self.last_shot_time:
            self.current_time1 = 0
            return True
        else:
            return False
    # 암석 게임 화면
    def out_of_screen(self):
        if self.rect.y > SCREEN_HEIGHT:
            return True
