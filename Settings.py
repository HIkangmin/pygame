import pygame
import time
# 게임 스크린 크기
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN = ( SCREEN_WIDTH , SCREEN_HEIGHT )

SAFE_HRIGHT = 440
# 색 정의
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
YELLOW = (250, 250, 50)
RED = (250, 50, 50)
GREEN = (50, 250, 50)
CRM_BLUE = ( 153, 217,234 ) 
CRM_GREEN = ( 0, 248, 0 )

# 전역 변수 및 설정 값 
FPS = 60
# VOLUME = 0.02
VOLUME = 0.06                   # 사운드 볼륨

MAX_GRENADE = 1                 # 수류탄 동시 사용 갯수
DEFALT_OBITAL_STRIKE = 1        # 필살기 횟수

ROLLRING_TIME = 80              # 회피 무적시간 0.8초 


MS =  pygame.time.Clock( ).tick(FPS) / 16  # MS =  /100 = 1.6MS  / 160 = 0.1

# MS =  time.time().cl.tick(FPS) / 1000