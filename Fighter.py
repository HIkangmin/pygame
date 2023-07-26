import pygame
import time

from Settings import *
from Storage import *
# 플레이어 객체
# class Player(pygame.sprite.Sprite): # Player로 이름을 바꾸고 싶지만, 나중에 소스를 합칠 때 문제가 될 것 같아 보류 
class Fighter(pygame.sprite.Sprite):
    def __init__(self):
        super(Fighter, self).__init__()
        self.image = pygame.image.load(IMAGES.MAN01)
        # self.image = pygame.transform.scale(self.image , ( 69 , 183) ) # 기존 이미지 크기 * 3
        self.image = pygame.transform.scale(self.image , ( 40 , 150) ) # 기존 이미지 크기 * 3
        self.defImg = self.image
        self.LdefImg = pygame.transform.flip( self.defImg, True, False)
        self.rect = self.image.get_rect()
        self.reset()

        self.rotate = 1 # 1 = R , L = -1
        #TODO 이미지 로드 할 떄 이미지 크기 조정 ( 누끼 기준 *3을 하였으나, )
        self.rolImgs = [ self.defImg ,
                        pygame.transform.scale( pygame.image.load(IMAGES.ROLLING_IMAGE_1), (96,159)),
                        pygame.transform.scale( pygame.image.load(IMAGES.ROLLING_IMAGE_2), (192,96)),
                        pygame.transform.scale( pygame.image.load(IMAGES.ROLLING_IMAGE_3), (114,189)),
                        pygame.transform.scale( pygame.image.load(IMAGES.ROLLING_IMAGE_4), (174,162)),
                        pygame.transform.scale( pygame.image.load(IMAGES.ROLLING_IMAGE_5), (96,156)),
                        pygame.transform.scale( pygame.image.load(IMAGES.ROLLING_IMAGE_6), (144,96)),
                        pygame.transform.scale( pygame.image.load(IMAGES.ROLLING_IMAGE_7), (138,93)),
                        pygame.transform.scale( pygame.image.load(IMAGES.ROLLING_IMAGE_8), (96,144))
                        ]       
        self.LrolImgs = []        
        self.rolImagSize = len(self.rolImgs)
        for n in range( self.rolImagSize ) :
            self.rolImgs[n] = pygame.transform.scale( self.rolImgs[n] , (50,140)  ) 
            self.LrolImgs.append ( pygame.transform.flip( self.rolImgs[n] , True, False) )
        
        self.curtRolTime = 0
        self.rolTime = ROLLRING_TIME
        # 100 = 1초         
        self.unitTd =  pygame.time.Clock().tick_busy_loop(FPS) / self.rolTime
        self.futd = round( self.rolTime / (self.rolImagSize ) , 2 )
        
        self.ImageState = 0 
        # 0 기본이미지, 1~8 구르는 이미지
        
        # 구르는 시간 
        


    # 플레이어 리셋
    def reset(self):
        self.rect.x = int(SCREEN_WIDTH / 2)
        self.rect.y = SCREEN_HEIGHT - self.rect.height
        self.dx = 0
        self.dy = 0

    # 플레이어 업데이트
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        # dx 값에 따라 내민 팔이 다른 이미지 출력 
        if ( 0 == self.ImageState and  0 < self.dx ) :
            self.image = self.defImg
        elif 0 == self.ImageState :
            self.image = self.LdefImg

        if self.rect.x < 0 or self.rect.x + self.rect.width > SCREEN_WIDTH:
            self.rect.x -= self.dx

        if self.rect.y < 0 or self.rect.y + self.rect.height > SCREEN_HEIGHT:
            self.rect.y -= self.dy
        self.rolImagUpdate()

    def rolling(self , rotate ) : 
        self.rotate = rotate
        # 구르는 중이 아니면 구른다.
        if ( 0 == self.ImageState ) :
            self.ImageState = 1

    def rolImagUpdate( self ) :
        if ( 0 != self.ImageState ) :
            
            self.curtRolTime += 1
            if self.rotate == 1 :
                if self.curtRolTime >= self.futd * self.ImageState : 
                    self.image = self.rolImgs[self.ImageState]
                    self.ImageState += 1
                    # self.dx += 2
                    if( self.ImageState == self.rolImagSize  ) :
                        self.ImageState = 0
                        self.curtRolTime = 0 
                        self.image = self.defImg
                        self.rotate == 0
                        # 마지막 구르는 이미지이면 기본 이미지로 변경

            if self.rotate == -1 :
                if self.curtRolTime >= self.futd * self.ImageState : 
                    self.image = self.LrolImgs[self.ImageState]
                    self.ImageState += 1
                    # self.dx -= 2
                    if( self.ImageState == self.rolImagSize  ) :
                        self.ImageState = 0
                        self.curtRolTime = 0 
                        self.image = self.LdefImg
                        self.rotate == 0
                        # 마지막 구르는 이미지이면 기본 이미지로 변경



    # 플레이어 그리기
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # 플레이어 충돌 체크
    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite
