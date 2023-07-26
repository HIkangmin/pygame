import pygame

import Storage
from Settings import SCREEN_WIDTH , SCREEN_HEIGHT , VOLUME

# 미사일 객체
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed , mx, my):
        super(EnemyBullet, self).__init__()
        self.image = pygame.image.load(Storage.IMAGES.NPC.ENEMYBULLET)
        self.image = pygame.transform.scale(self.image , (15,15)  ) 
        self.fire = pygame.image.load(Storage.IMAGES.EXPLOSION)
        self.fire = pygame.transform.scale(self.image , (15,15)  ) 

        self.sound = pygame.mixer.Sound(Storage.SOUNDS.NPC.TROWBOMB)
        self.sound.set_volume( 0.1)
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
        # TODO 사분면에 따라 미사일이 기울어서 날아가기는 하지만, 총알을 원형으로 쓸 것이 이기에 문제가 되지는 않음. ( 1사분면만 정상 )

    # 미사일 발사
    def launch(self):
        self.sound.set_volume( 0.1)
        self.sound.play()

    # 미사일 업데이트
    def update(self):
        # self.rect.y -= self.speed
        self.vpos += self.nrmv
        self.rect.center = self.vpos
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH or self.rect.top < 0  or self.rect.bottom > SCREEN_HEIGHT or self.rect.y + self.rect.height < 0 : 
           self.kill()


        
    def out_of_screen(self):    
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH or self.rect.top < 0  or self.rect.bottom > SCREEN_HEIGHT or self.rect.y + self.rect.height < 0 : 
           self.kill()

    # 미사일 충돌 체크
    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite