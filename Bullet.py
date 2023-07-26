import pygame

import Storage
from Settings import SCREEN_WIDTH , SCREEN_HEIGHT , VOLUME

# 미사일 객체
class Bullet(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed , mx, my):
        super(Bullet, self).__init__()
        self.image = pygame.image.load(Storage.IMAGES.BULLET)
        self.image = pygame.transform.scale(self.image , (20,20)  ) 
        self.defImg = self.image
        self.fire = pygame.image.load(Storage.IMAGES.EXPLOSION)
        self.fire = pygame.transform.scale(self.image , (50,50)  ) 

        self.sound = pygame.mixer.Sound(Storage.SOUNDS.NPC.GUN)
        
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

        self.vmpos = pygame.Vector2( mx, my ) # 벡터 마우스 포지션
        self.vpos = pygame.Vector2( xpos, ypos ) # 벡터 미사일 포지션
        self.rect.center = self.vpos # 이미지의 중앙 = 벡터 미사일 포지션

        self.vspd = self.vmpos - self.vpos    # 벡터 마우스 포지션 * 벡터 미사일 포지션
        self.nrmv = self.vspd.normalize( ) * self.speed # 미사일의 방향 ( 유닛벡터 ) * 속도d

        self.angle =  self.vpos.angle_to( self.vmpos ) # self.angle = 미사일 포지션을 기준으로 각도를 구함
        self.image = pygame.transform.rotate(self.image,  self.angle ) # 미사일 이미지의 회전율 = 각도
        # rotate에 자기자신을 사용하면 왜곡된 이미지가 생성 됨.
        
    # 미사일 발사
    def launch(self):
        self.sound.set_volume(VOLUME)
        self.sound.play()
        self.sound.set_volume(VOLUME)
    # 미사일 업데이트
    def update(self):
        # self.rect.y -= self.speed
        self.vpos += self.nrmv
        self.rect.center = self.vpos
        
        if self.rect.y + self.rect.height < 0 :
            self.kill()

    # 미사일 충돌 체크
    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite