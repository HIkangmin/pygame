import random
import pygame

import Storage
from Settings import *

# 수류탄 객체
class Grenade(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed , mx, my):
        super(Grenade, self).__init__()
        self.image = pygame.image.load( Storage.IMAGES.GRENADE )
        self.image = pygame.transform.scale(self.image , (50,50)  ) 
        self.defImg = self.image
 
        self.sound = pygame.mixer.Sound(Storage.SOUNDS.MISSILE)
        self.sound.set_volume( VOLUME / 2 )


        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

        self.vmpos = pygame.Vector2( mx, my ) # 벡터 마우스 포지션
        self.vpos = pygame.Vector2( xpos, ypos ) # 벡터 수류탄 포지션
        self.rect.center = self.vpos # 이미지의 중앙 = 벡터 수류탄 포지션

        self.vspd = self.vmpos - self.vpos    # 벡터 마우스 포지션 * 벡터 수류탄 포지션
        self.nrmv = self.vspd.normalize( ) * self.speed # 수류탄의 방향 ( 유닛벡터 ) * 속도d

        self.angle =  self.vpos.angle_to( self.vmpos ) # self.angle = 수류탄 포지션을 기준으로 각도를 구함
        self.image = pygame.transform.rotate(self.image,  self.angle ) # 수류탄 이미지의 회전율 = 각도
        self.imgAngle = 10

    # 수류탄 발사
    def launch(self):
        self.sound.play()



    # 수류탄 업데이트
    def update(self):
        # self.rect.y -= self.speed
        self.vpos += self.nrmv
        self.rect.center = self.vpos

        
        self.image = pygame.transform.rotate( self.defImg, self.imgAngle )

        
        self.imgAngle += 5
        
        if self.rect.y + self.rect.height < 0 or self.rect.y > SCREEN_HEIGHT :
            self.kill()

        if self.rect.x + self.rect.width < 0 or self.rect.x > SCREEN_WIDTH :
            self.kill()

    # 수류탄 충돌 체크
    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite