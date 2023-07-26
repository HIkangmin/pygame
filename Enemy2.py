
import pygame
import random
import os
import time
import Storage
from Settings import *


# 암석 객체
class Enemy2(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Enemy2, self).__init__()
        random_list = ["/black_soldier_spritesheet.png",
                       "/green_soldier_spritesheet.png",
                       "/red_soldier_spritesheet.png",
                       "/green_ninja_spritesheet.png" ]
        rock_images_path = Storage.path("assets/images/npc"+ random_list[random.randint(0, len(random_list)-1)])

        sprite_sheet = pygame.image.load(rock_images_path)
        frame_size = (50, 78)
        frame_positions = [
            (14, 178),  # 첫번째 프레임
            (78, 179), # 두번째 프레임
            (142, 180),  # 세번째 프레임
            (207, 179),  # 네번째 프레임
            (270, 178), # 다섯번째 프레임
            (336, 178),  # 여섯번째 프레임
            (400, 179),  # 일곱번째 프레임
            (464, 180), # 여덟번째 프레임
        ]
        self.frames = []
 
        for position in frame_positions:
            frame_rect = pygame.Rect(position, frame_size)
            frame_image = sprite_sheet.subsurface(frame_rect)
            self.frames.append(frame_image)

        self.current_frame_index = 0
        self.image = self.frames[self.current_frame_index]
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

            self.current_frame_index += 1
            if self.current_frame_index >= len(self.frames):
                self.current_frame_index = 0
            self.image = self.frames[self.current_frame_index]
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
