import pygame
import random
from Cursor import Cursor

from Storage import *
from Settings import *

from Bullet import Bullet
from Grenade import Grenade
from GrenadeExplosion import GrenadeExplosion
from OrbitalStrike import OrbitalStrike
from Fighter import Fighter
from Cloude import Cloud
from Enemy import Enemy
from Enemy1 import Enemy1
from Enemy2 import Enemy2
from EnemyBullet import EnemyBullet
# 게임 객체
class Game( ) : 
    def __init__( self ) : 
        self.menu_image = pygame.image.load( IMAGES.BACKGROUND2 )
        self.menu_image = pygame.transform.scale( self.menu_image , SCREEN )
        self.background_image = pygame.image.load( IMAGES.BACKGROUND_NEW_02 )
        self.background_image = pygame.transform.scale( self.background_image , SCREEN )
        self.explosion_image = pygame.image.load( IMAGES.EXPLOSION )
        self.default_font = pygame.font.Font( FONTS.NANUMGOTHIC, 28 )
        self.font_70 = pygame.font.Font( FONTS.NANUMGOTHIC, 70 )
        self.font_30 = pygame.font.Font( FONTS.NANUMGOTHIC, 30 )
        explosion_file = ( SOUNDS.NPC.ENEMYHURT,
                          SOUNDS.NPC.ENEMYPAIN,
                          SOUNDS.NPC.ENEMYSHOT,
                          SOUNDS.NPC.MONSTERPAIN )
        self.explosion_path_list = [path( file ) for file in explosion_file]
        self.gameover_sound = pygame.mixer.Sound( SOUNDS.GAMEOVER )
        self.gameover_sound.set_volume( VOLUME )
        pygame.mixer.music.load( SOUNDS.NPC.BGM )
        pygame.mixer.music.set_volume( 1 )

        self.fighter = Fighter( )
        self.bullets = pygame.sprite.Group( )
        self.grenades = pygame.sprite.Group( )
        self.grenadeExplosions = pygame.sprite.Group( )
        self.obitalStrikes = pygame.sprite.Group( )

        self.cloud01 = Cloud(0, SCREEN_HEIGHT * 0.05 , -7)
        self.cloud02 = Cloud(0, SCREEN_HEIGHT * 0.1 , 5)
        self.cloud03 = Cloud(0, SCREEN_HEIGHT * 0.2 , 1)
        self.cloud04 = Cloud(0, SCREEN_HEIGHT * 1.5 , -2)

        self.cursor = Cursor()

        self.obitalStrikeAmount = DEFALT_OBITAL_STRIKE

        self.enemys = pygame.sprite.Group( )
        self.enemys1 = pygame.sprite.Group( )
        self.enemys2 = pygame.sprite.Group( )
        self.enemyBullets = pygame.sprite.Group( )
        self.occur_prob = 40
        self.shot_count = 0
        self.count_missed = 0
        self.delta_time = 0
        # 게임 메뉴 On/Off
        self.menu_on = True
        self.random_count = 0
    # 게임 이벤트 처리 및 조작
    def process_events( self ) : 
        # 게임 이벤트 처리
        for event in pygame.event.get( ) : 
            if event.type == pygame.QUIT : 
                return True
            # 메뉴 화면 이벤트 처리
            if self.menu_on : 
                if event.type == pygame.KEYDOWN : 
                    if event.key == pygame.K_SPACE : #or event.key == pygame.K_RETURN : 
                        pygame.mixer.music.play( -1 )
                        pygame.mixer.music.set_volume( VOLUME )
                        self.shot_count = 0
                        self.count_missed = 0
                        # 게임 메뉴 On/Off
                        self.menu_on = False

            # 게임 화면 이벤트 처리
            else : 
                # 마우스 이벤트 처리
                if event.type == pygame.MOUSEBUTTONDOWN :
                    # 1 좌클릭 2 스크롤 버튼 3 우클릭 4 휠위로 5 휠아래로
                    if pygame.mouse.get_pressed()[0] :   
                        mpos = pygame.mouse.get_pos( )
                        bullet = Bullet( self.fighter.rect.centerx, self.fighter.rect.y, 10 , mpos[0], mpos[1] )
                        bullet.fire
                        bullet.launch( )
                        self.bullets.add( bullet )

                    elif pygame.mouse.get_pressed()[2] :   
                        mpos = pygame.mouse.get_pos( )
                        if self.grenades.__len__() < MAX_GRENADE :
                            grenade = Grenade( self.fighter.rect.centerx, self.fighter.rect.y, 10 , mpos[0], mpos[1] )
                            grenade.launch( )
                            self.grenades.add( grenade )

                if event.type == pygame.MOUSEMOTION :                       
                    #마우스 이미지 처리
                    self.cursor.rect.center = pygame.mouse.get_pos()
                    pygame.mouse.set_visible(False)

                # 키보드 이벤트 처리 
                    # ISSUE 키가 재대로 인식 되지 않음.  보류
                    # pygame.key.get_pressed()[pygame.K_RIGHT] 방식을 쓰면 입력은 부드럽게 되지만, 프로세스 구조가 완전히 달라서 아예 다시 짜야함으로 보류
                
                elif event.type == pygame.KEYDOWN : 
                    
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a : 
                        self.fighter.dx -= 5
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d : 
                        self.fighter.dx += 5
                    elif event.key == pygame.K_UP or event.key == pygame.K_w : 
                        self.fighter.dy -= 5
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s : 
                        self.fighter.dy += 5
                    elif event.key == pygame.K_SPACE : 
                        if( self.obitalStrikeAmount > 0 and self.obitalStrikes.__len__() == 0 ) :
                            obitalStrike = OrbitalStrike()
                            obitalStrike.launch()
                            self.obitalStrikes.add( obitalStrike )
                            self.obitalStrikeAmount -= 1 
                            # # Orbital Strike
                            # if self.obitalStrikeAmount > 0 :
                            #     self.obitalStrikeAmount -= 1
                            #     for enemyB in self.enemyBullets : 
                            #         enemyB.kill()
                            #     for enemy in self.enemys : 
                            #         enemy.kill()
                            #     for enemy1 in self.enemys1 : 
                            #         enemy1.kill()
                            #     for enemy2 in self.enemys2 : 
                            #         enemy2.kill()
                            
                        
                    elif event.key == pygame.K_RETURN :
                        self.pause( self.screen )

                    elif event.key == pygame.K_LSHIFT :
                        # 키조합이 안 먹혀서, 기존에 이동중이던 방향으로 이동함.
                        if ( 0 < self.fighter.dx  ) :
                            if ( 0 == self.fighter.ImageState ):
                                self.fighter.rolling(1) 
                                self.fighter.dx += 5
                        else: 
                            if ( 0 == self.fighter.ImageState ):
                                self.fighter.rolling(-1) 
                                self.fighter.dx -= 5

                elif event.type == pygame.KEYUP : 
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_a : 
                        self.fighter.dx = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or  event.key == pygame.K_w or event.key == pygame.K_s : 
                        self.fighter.dy = 0

        return False

    # 게임 로직 수행
    def run_logic( self, screen ) : 
        
        self.screen = screen
        # 적 수와 속도 조절
        occur_of_enemys = 1 + int((self.shot_count + 1 ) / 300 )
        min_enemy_speed = 1 + int((self.shot_count + 1 ) / 200 ) # 적총알 수
        max_enemy_speed = 1 + int((self.shot_count + 1 ) / 100 )
        
        if random.randint( 1, self.occur_prob ) == 1 : 
            # 적 생성
            self.random_count += 1
            for i in range( occur_of_enemys ) : 
                speed = random.randint( min_enemy_speed, max_enemy_speed + 10 )
                if self.random_count % 2 == 0  :
                    enemy = Enemy( random.randint(  20  , SCREEN_WIDTH - 20 ), random.randint(  50  , SCREEN_HEIGHT - SAFE_HRIGHT ), speed )
                    self.enemys.add( enemy )
                    enemyBullet = EnemyBullet( enemy.rect.centerx, enemy.rect.centery, speed , random.randint(  20  , SCREEN_WIDTH - 20 ), random.randint(  600  , SCREEN_HEIGHT - 20 ) )
                    enemyBullet.launch( )
                    self.enemyBullets.add( enemyBullet )                       
               
                elif  self.random_count % 3 == 0 :
                    enemy1 = Enemy1( random.randint(  20  , SCREEN_WIDTH - 20  ), random.randint(  50  , SCREEN_HEIGHT - SAFE_HRIGHT ), speed )
                    self.enemys1.add( enemy1 )
                    enemyBullet = EnemyBullet( enemy1.rect.centerx, enemy1.rect.centery, speed , random.randint(  20  , SCREEN_WIDTH - 20), random.randint(  600  , SCREEN_HEIGHT - 20 ) )
                    enemyBullet.launch( )
                    self.enemyBullets.add( enemyBullet )   

                elif  self.random_count % 8 :
                    enemy2 = Enemy2( random.randint(  20  , SCREEN_WIDTH - 20  ), random.randint(  50  , SCREEN_HEIGHT - SAFE_HRIGHT ), speed )
                    self.enemys2.add( enemy2 )
                    enemyBullet = EnemyBullet( enemy2.rect.centerx, enemy2.rect.centery, speed , random.randint(  20  , SCREEN_WIDTH - 20), random.randint(  600  , SCREEN_HEIGHT - 20 ) )
                    enemyBullet.launch( )
                    self.enemyBullets.add( enemyBullet )

        # 미사일 충돌 체크
        for bullet in self.bullets : 
            enemy = bullet.collide( self.enemys )
            if enemy : 
                self.occur_explosion( screen, enemy.rect.x, enemy.rect.y )
                self.shot_count += 1
                bullet.kill( )
                enemy.kill( )        
            enemy1 = bullet.collide( self.enemys1 )
            if enemy1 : 
                self.occur_explosion( screen, enemy1.rect.x, enemy1.rect.y )
                self.shot_count += 1
                bullet.kill( )
                enemy1.kill( )
            enemy2 = bullet.collide( self.enemys2 )
            if enemy2 : 
                self.occur_explosion( screen, enemy2.rect.x, enemy2.rect.y )
                self.shot_count += 1
                bullet.kill( )
                enemy2.kill( )

        # 수류탄 충돌 체크         
        for grenade in self.grenades : 
            enemy = grenade.collide( self.enemys )
            if enemy :                 
                grenadeExplosion = GrenadeExplosion( grenade.rect.x, grenade.rect.y )
                self.grenadeExplosions.add( grenadeExplosion )
                grenadeExplosion.runEplosion()
                grenade.kill( )                
            enemy1 = grenade.collide( self.enemys1 )
            if enemy1 :                 
                grenadeExplosion = GrenadeExplosion( grenade.rect.x, grenade.rect.y )
                self.grenadeExplosions.add( grenadeExplosion )
                grenadeExplosion.runEplosion()
                grenade.kill( )            
            enemy2 = grenade.collide( self.enemys2 )
            if enemy2 :          
                grenadeExplosion = GrenadeExplosion( grenade.rect.x, grenade.rect.y )
                self.grenadeExplosions.add( grenadeExplosion )
                grenadeExplosion.runEplosion()
                grenade.kill( )
            enemyBullet = grenade.collide( self.enemyBullets )
            if enemyBullet :          
                self.shot_count += 1
                grenadeExplosion = GrenadeExplosion( grenade.rect.x, grenade.rect.y )
                self.grenadeExplosions.add( grenadeExplosion )
                grenadeExplosion.runEplosion()
                enemyBullet.kill( ) 
                grenade.kill( )

        # 수류탄 폭발 체크
        for gExplosion in self.grenadeExplosions : 
            enemy = gExplosion.collide( self.enemys )
            if enemy : 
                self.occur_explosion( screen, enemy.rect.x, enemy.rect.y )
                self.shot_count += 1
                enemy.kill( ) 
            enemy1 = gExplosion.collide( self.enemys1 )
            if enemy1 :                 
                self.occur_explosion( screen, enemy1.rect.x, enemy1.rect.y )
                self.shot_count += 1
                enemy1.kill( ) 
            enemy2 = gExplosion.collide( self.enemys2 )
            if enemy2 :          
                self.occur_explosion( screen, enemy2.rect.x, enemy2.rect.y )
                self.shot_count += 1
                enemy2.kill( ) 
            enemyBullet = gExplosion.collide( self.enemyBullets )
            if enemyBullet :          
                self.occur_explosion( screen, enemyBullet.rect.x, enemyBullet.rect.y )
                self.shot_count += 1
                enemyBullet.kill( )
        # 괘도 포격 체크
        for obitalStrike in self.obitalStrikes :
            if obitalStrike.attack :            
                enemyBullet = obitalStrike.collide( self.enemyBullets )
                if enemyBullet :          
                    self.occur_explosion( screen, enemyBullet.rect.x, enemyBullet.rect.y )
                    self.shot_count += 1
                    enemyBullet.kill( )
                if obitalStrike.state > 0 : # 0이후 부터는 빔 
                    enemy = obitalStrike.collide( self.enemys )
                    if enemy : 
                        self.occur_explosion( screen, enemy.rect.x, enemy.rect.y )
                        self.shot_count += 1
                        enemy.kill( ) 
                    enemy1 = obitalStrike.collide( self.enemys1 )
                    if enemy1 :                 
                        self.occur_explosion( screen, enemy1.rect.x, enemy1.rect.y )
                        self.shot_count += 1
                        enemy1.kill( ) 
                    enemy2 = obitalStrike.collide( self.enemys2 )
                    if enemy2 :          
                        self.occur_explosion( screen, enemy2.rect.x, enemy2.rect.y )
                        self.shot_count += 1
                        enemy2.kill( ) 

        for enemyBullet in self.enemyBullets : 
            if enemyBullet.out_of_screen( ) : 
                enemyBullet.kill( )

        for enemy in self.enemys : 
            if enemy:
                if (enemy.addshot(self.delta_time) == True):
                    enemyBullet = EnemyBullet( enemy.rect.centerx, enemy.rect.centery, 1 , random.randint(  20  , SCREEN_WIDTH - 20), random.randint(  600  , SCREEN_HEIGHT - 20 ) )
                    enemyBullet.launch( )
                    self.enemyBullets.add( enemyBullet )          
        for enemy1 in self.enemys1 : 
            if enemy1:
                if (enemy1.addshot(self.delta_time) == True):
                    enemyBullet = EnemyBullet( enemy1.rect.centerx, enemy1.rect.centery, 2 , random.randint(  20  , SCREEN_WIDTH - 20), random.randint(  600  , SCREEN_HEIGHT - 20 ) )
                    enemyBullet.launch( )
                    self.enemyBullets.add( enemyBullet )                      
        for enemy2 in self.enemys2 : 
            if enemy2:
                if (enemy2.addshot(self.delta_time) == True):
                    enemyBullet = EnemyBullet( enemy2.rect.centerx, enemy2.rect.centery, 3 , random.randint(  20  , SCREEN_WIDTH - 20), random.randint(  600  , SCREEN_HEIGHT - 20 ) )
                    enemyBullet.launch( )
                    self.enemyBullets.add( enemyBullet )   

        # 게임오버 조건 ( 충돌 )
        if self.fighter.collide( self.enemyBullets ) or self.fighter.collide( self.enemys ) :
            if ( self.fighter.ImageState == 0 ): # 회피 동작 중이면 무시 
                pygame.mixer_music.stop( )

                self.occur_explosion( screen, self.fighter.rect.x, self.fighter.rect.y )
                self.gameover_sound.play( )
                self.enemys.empty( )
                self.enemys1.empty( )
                self.enemys2.empty( )
                self.enemyBullets.empty( )
                self.obitalStrikes.empty( )
                self.grenadeExplosions.empty( )
                self.grenades.empty()
                self.obitalStrikeAmount = DEFALT_OBITAL_STRIKE
                self.bullets.empty( )
                self.fighter.reset( )
                self.menu_on = True


    # 텍스트 그리기
    def draw_text( self, screen, text, font, x, y, color ) : 
        text_obj = font.render( text, True, color )
        text_rect = text_obj.get_rect( )
        text_rect.center = x, y
        screen.blit( text_obj, text_rect )

    # 충돌 이벤트 발생
    def occur_explosion( self, screen, x, y ) : 
        explosion_rect = self.explosion_image.get_rect( )
        explosion_rect.x = x
        explosion_rect.y = y
        screen.blit( self.explosion_image, explosion_rect )
        pygame.display.update( )
        

        explosion_sound = pygame.mixer.Sound( random.choice( self.explosion_path_list ) )
        explosion_sound.set_volume( VOLUME )
        explosion_sound.play( )

    # 게임 메뉴 출력
    def display_menu( self, screen ) : 
        screen.blit( self.menu_image, [0, 0] )
        draw_x = int( SCREEN_WIDTH / 2 )
        draw_y = int( SCREEN_HEIGHT / 4 )
        self.draw_text( screen, STRING.CAPTION1,
                       self.font_70, draw_x, draw_y, RED )
        self.draw_text( screen, STRING.CAPTION2,
                       self.default_font, draw_x, draw_y + 170, YELLOW )
        self.draw_text( screen, STRING.CAPTION3,
                       self.font_70, draw_x, draw_y + 250, BLACK )
        self.draw_text( screen, STRING.CAPTION4,
                       self.font_70, draw_x, draw_y + 350, BLACK )
        self.draw_text( screen, STRING.CAPTION5,
                       self.font_70, draw_x, draw_y + 450, BLACK )
        self.draw_text( screen, STRING.CAPTION6,
                       self.font_70, draw_x, draw_y + 550, BLACK )
        pygame.display.flip( ) # 화면 업데이트

    # 게임 프레임 출력, 화면 최상위 레이어에 그려질 오브젝트를 마지막순서로 배치합니다.
    def display_frame( self, screen ) : 
        # 배경 이미지
        screen.blit( self.background_image, self.background_image.get_rect( ) )
        self.draw_text( screen, STRING.TOP1 + str ( self.shot_count ) ,
                       self.default_font, 100 , 20, RED )
        self.draw_text( screen, STRING.SKIL_COUNT + str ( self.obitalStrikeAmount ),
                       self.default_font, 100 , SCREEN_HEIGHT - 40, GREEN )
        

        self.delta_time = pygame.time.Clock().tick(60) / 1000.0
        
        self.enemys.update(self.delta_time)
        self.enemys1.update(self.delta_time )
        self.enemys2.update(self.delta_time )
        
        self.grenades.update( )
        
        self.bullets.update( )
        self.enemyBullets.update( )     
        self.grenadeExplosions.update( )
        


        self.cloud01.update()
        self.cloud02.update()
        self.cloud03.update()
        self.cloud04.update()
        self.fighter.update( )
        self.cursor.update()

        self.obitalStrikes.update()
        #Draw 화면에 뿌리는 작업


        self.enemys.draw( screen )
        self.enemys1.draw( screen )
        self.enemys2.draw( screen )

        self.enemyBullets.draw( screen )
        
        self.bullets.draw( screen )
        self.grenades.draw( screen )
        
        self.grenadeExplosions.draw( screen )

        self.cloud01.draw(screen)
        self.cloud02.draw(screen)
        self.cloud03.draw(screen)
        self.cloud04.draw(screen)

        self.obitalStrikes.draw( screen )
        self.fighter.draw( screen )
        self.cursor.draw(screen)
    
    # 일시정지 기능
    def pause ( self , screen ) :
        
        draw_x = int( SCREEN_WIDTH / 2 )
        draw_y = int( SCREEN_HEIGHT / 4 )
        self.draw_text( screen, STRING.CAPTION1,
                       self.font_70, draw_x, draw_y, RED )
        self.draw_text( screen, STRING.PAUSED,
                       self.default_font, draw_x, draw_y + 200, YELLOW )
        self.draw_text( screen, STRING.CAPTION3,
                       self.font_70, draw_x, draw_y + 250, BLACK )
        self.draw_text( screen, STRING.CAPTION4,
                       self.font_70, draw_x, draw_y + 320, BLACK )
        pygame.display.flip( ) # 화면 업데이트


        paused = True
        pygame.event.set_grab( False ) 
        while paused:
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN  :
                    paused = False
                    pygame.event.set_grab( True ) 
                    return

