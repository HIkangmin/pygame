import random
import pygame

import Storage
from Settings import *

# 수류탄 객체
class GrenadeExplosion(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super(GrenadeExplosion, self).__init__()
        
        self.image = pygame.image.load( Storage.IMAGES.GRENADE_EXPLOSION )
        self.image = pygame.transform.scale(self.image , (200,200)  ) 
        self.defImg = self.image

        self.explSound = [ 
            pygame.mixer.Sound( Storage.SOUNDS.GRENADE_EXPL1 ) ,
            pygame.mixer.Sound( Storage.SOUNDS.GRENADE_EXPL2 ) ,
            pygame.mixer.Sound( Storage.SOUNDS.GRENADE_EXPL3 ) ,
            pygame.mixer.Sound( Storage.SOUNDS.GRENADE_EXPL4 ) ,
            pygame.mixer.Sound( Storage.SOUNDS.GRENADE_EXPL5 ) 
        ]
        for ES in self.explSound :
            ES.set_volume( VOLUME )

        
 
        self.rect = self.image.get_rect()
        self.rect.x = xpos - self.rect.width / 2
        self.rect.y = ypos - self.rect.height / 1.3

        self.limitTime = 17
        self.lifeTime = 0

    # 수류탄 발사
    def launch(self):
        self.sound.play()

    def runEplosion (self) :

        explosion_sound = random.choice( self.explSound ) 
        explosion_sound.play( )

     # 수류탄 업데이트
    def update(self):

        self.lifeTime += 1

        if self.lifeTime > self.limitTime :
            self.kill( )
        
        
        if self.rect.y + self.rect.height < 0 or self.rect.y > SCREEN_HEIGHT :
            self.kill()

        if self.rect.x + self.rect.width < 0 or self.rect.x > SCREEN_WIDTH :
            self.kill()

    # 수류탄 충돌 체크
    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite