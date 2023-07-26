import pygame

from Settings import *
from Game import Game
from Storage import * 

def main( ) : 
    pygame.init( )
    pygame.display.set_caption( STRING.TITLE )
    screen = pygame.display.set_mode( SCREEN )
    clock = pygame.time.Clock( )
    game = Game( )

    done = False
    while not done : 
        done = game.process_events( )
        if game.menu_on :   # 게임 메뉴 처리
            game.display_menu( screen )
        else :   # 게임 화면 처리
            pygame.event.set_grab( True ) 
            game.run_logic( screen )
            game.display_frame( screen )

        pygame.display.flip( ) # 화면 업데이트
        clock.tick_busy_loop( FPS )

    pygame.quit( )

if __name__ == "__main__" : 
    main( )
