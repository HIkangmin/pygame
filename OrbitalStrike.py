import pygame

import Storage
from Settings import *

# 포격 객체
class OrbitalStrike(pygame.sprite.Sprite):
    def __init__(self):
        super(OrbitalStrike, self).__init__()
        self.images = [ pygame.image.load(Storage.IMAGES.ORBITAL_STRIKE00), # 전조 2초
                        pygame.image.load(Storage.IMAGES.ORBITAL_STRIKE01), # 조준 2초
                        pygame.image.load(Storage.IMAGES.ORBITAL_STRIKE02), # 동시사격
                        pygame.image.load(Storage.IMAGES.ORBITAL_STRIKE03), # 동시사격
                        pygame.image.load(Storage.IMAGES.ORBITAL_STRIKE04)  # 동시사격 방향 전환 필요
                        ]
        
        for img in self.images : 
            img = img.set_alpha(200)

        self.images[0] = pygame.transform.rotate( self.images[0], 90 )
        self.images[1] = pygame.transform.rotate( self.images[1], 90 )
        self.images[2] = pygame.transform.rotate( self.images[2], 90 )
        self.images[3] = pygame.transform.rotate( self.images[3], 90 )
        # self.images[4] = pygame.transform.rotate( img, 90 )

        self.images[0] = pygame.transform.scale(self.images[0] , ( SCREEN_WIDTH , SCREEN_HEIGHT + 100 - SAFE_HRIGHT/2 )  ) 
        self.images[1] = pygame.transform.scale(self.images[1] , ( SCREEN_WIDTH / 10 , SCREEN_HEIGHT + 100 - SAFE_HRIGHT/2 )  ) 
        self.images[2] = pygame.transform.scale(self.images[2] , ( SCREEN_WIDTH , SCREEN_HEIGHT  - SAFE_HRIGHT/2)  ) 
        self.images[3] = pygame.transform.scale(self.images[3] , ( SCREEN_WIDTH , SCREEN_HEIGHT  - SAFE_HRIGHT/2)  ) 
        self.images[4] = pygame.transform.scale(self.images[4] , ( SCREEN_WIDTH , SCREEN_HEIGHT   - SAFE_HRIGHT/2)  ) 
        # 이미지를 먼저 돌리는지, 크기를 먼저 키우는지에 따라서 모양이 다르게 나옴.

        self.image = self.images[3]
        self.startSound = pygame.mixer.Sound(Storage.SOUNDS.ORBITAL_STRIKE00)
        self.startSound.set_volume( VOLUME * 1.3 )
        self.endSound = pygame.mixer.Sound(Storage.SOUNDS.ORBITAL_STRIKE01)
        self.endSound.set_volume( VOLUME * 1.3 )
        
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT
        # self.rect.y = 0

        self.attack = False

        self.preTime = MS * 200

        self.limitTime = MS * ( 300 + self.preTime )
        self.lifeTime = 0
        self.state = 0

    # 포격 발사
    def launch(self):
        self.image = self.images[self.state]
        self.rect = self.image.get_rect()
        self.attack = True
        self.startSound.play()
        
    # 포격 업데이트
    def update(self):
        # self.rect.center = ( SCREEN_WIDTH , SCREEN_HEIGHT )
        if self.attack :
            self.lifeTime += 1 
            if self.lifeTime == int( self.preTime/2.2 ) :
                self.state += 1
                self.image = self.images[self.state]
                self.rect = self.image.get_rect()
                self.rect.centerx = SCREEN_WIDTH / 2
                self.endSound.play()
            if self.lifeTime ==  self.preTime :
                self.state += 1
                # self.rect.x = 0
                self.image = self.images[self.state]
                self.rect = self.image.get_rect()
            if self.lifeTime == int( self.limitTime/3 ) :
                self.state += 1
                self.image = self.images[self.state]
                self.rect = self.image.get_rect()
            if self.lifeTime == int( self.limitTime ) :
                self.state += 1
                self.image = self.images[self.state]
                self.rect = self.image.get_rect()
                self.endSound.stop()


        if self.lifeTime > self.limitTime :
            self.state = 0
            self.attack = False
            self.kill()

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite