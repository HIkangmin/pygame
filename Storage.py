import os
import sys

# 네이밍 규칙 ( 코딩 스텐다드 )
# 파일의 경로를 담고 있는 class와 변수의 이름은 대문자로 통일하며,
# 띄어쓰기나 소문자가 필요한경우 _ 를 사용합니다. 
# (파이썬에서 상수는 CONST_ 등으로 표기하지만, 편의를 위해 무시하고 있습니다.)
# 운석같은 특이케이스가 아니라면 해당 규칙을 따라 주시기 바랍니다.


# 문자열
class STRING :
    TITLE = 'Outlaw Gunner 3팀'
    CAPTION1 = ' 황야의 무법자 '
    CAPTION2 = 'SPACE => START'
    CAPTION3 = 'A W S D , L / R MOUSE '
    CAPTION4 = 'SHIFT - Rolling '
    CAPTION5 = 'SPACE - Orbital attack '
    CAPTION6 = 'RETURN - PAUSE '
    PAUSED = ' PAUSED '
    TOP1 = ' 처치한 적 : '
    SKIL_COUNT = 'Obital Strike : '


# 폰트 파일
class FONTS:
    NANUMGOTHIC = "assets/fonts/NanumGothic.ttf"

# 음악 파일
class SOUNDS:
    GRENADE_EXPL1 = "assets/sounds/EXPLO_VEH_DROPPOD_DIST.wav"
    GRENADE_EXPL2 = "assets/sounds/EXPLO_VEH_ENG_TURRET_DIST.wav"
    GRENADE_EXPL3 = "assets/sounds/EXPLO_VEH_FAC_TURRET_DIST.wav"
    GRENADE_EXPL4 = "assets/sounds/EXPLO_VEH_LIGHTNING_DIST.wav"
    GRENADE_EXPL5 = "assets/sounds/EXPLO_VEH_QUAD_DIST.wav"

    ORBITAL_STRIKE00 = "assets/sounds/Orbital_Strike/Explo_Orbital_Strike_Beam_Close_01.wav"  # 4초 동안 소리만 나다가
    ORBITAL_STRIKE01 = "assets/sounds/Orbital_Strike/Explo_Orbital_Strike_Close_01.wav"        # 15초간 적 섬멸 
    
    EXPLOSION01 = "assets/sounds/explosion01.wav"
    EXPLOSION02 = "assets/sounds/explosion02.wav"
    EXPLOSION03 = "assets/sounds/explosion03.wav"
    GAMEOVER = "assets/sounds/gameover.wav"
    MISSILE = "assets/sounds/missile.wav"
    MUSIC = "assets/sounds/music.wav"
    
    class NPC :
        MONSTERPAIN = "assets/sounds/npc/sound01/monsterpain.wav"
        ENEMYHURT = "assets/sounds/npc/sound02/enemyhurt.wav"
        ENEMYPAIN = "assets/sounds/npc/sound03/enemypain.wav"
        ENEMYSHOT = "assets/sounds/npc/sound03/enemyshot.wav"
        GUN = "assets/sounds/npc/sound03/gun.wav"
        PISTOL = "assets/sounds/npc/sound02/pistol.wav"
        TROWBOMB = "assets/sounds/npc/sound03/throwbomb.wav"
        BGM = "assets/sounds/npc/sound03/backgm.wav"
# 이미지 파일
class IMAGES:
    DEFALT_TEST = "assets/images/Python-logo.svg.png"
    ORBITAL_STRIKE00 = "assets/images/Orbital_Strike/0.png"
    ORBITAL_STRIKE01 = "assets/images/Orbital_Strike/1.png"
    ORBITAL_STRIKE02 = "assets/images/Orbital_Strike/2.png"
    ORBITAL_STRIKE03 = "assets/images/Orbital_Strike/3.png"
    ORBITAL_STRIKE04 = "assets/images/Orbital_Strike/4.png"

    BACKGROUND_NEW_02 = "assets/images/background_new_02.jpg"
    BACKGROUND2 = "assets/images/background2.jpg"
    CROSSHAIR = "assets/images/crosshair.png"
    EXPLOSION = "assets/images/explosion.png"
    FIGHTER = "assets/images/fighter.png"
    MAN01 = "assets/images/man01.png" # 23 * 61 
    MANR01 = "assets/images/manr-01.png"
    MANR02 = "assets/images/manr-02.png"
    MANR03 = "assets/images/manr-03.png"
    MANR04 = "assets/images/manr-04.png"
    MANR05 = "assets/images/manr-05.png"
    MANR06 = "assets/images/manr-06.png"
    MANR07 = "assets/images/manr-07.png"
    MANR08 = "assets/images/manr-08.png"
    MAXRESDEFAULT_NEW = "assets/images/maxresdefault_new.jpg"
    BULLET = "assets/images/bullet01.png"
    MISSILE = "assets/images/missile.png"
    GRENADE = "assets/images/grenade01.png"
    GRENADE_EXPLOSION = "assets/images/Explo01.png"

    ROLLING_IMAGE_1 = "assets/images/manr-01.png"
    ROLLING_IMAGE_2 = "assets/images/manr-02.png"
    ROLLING_IMAGE_3 = "assets/images/manr-03.png"
    ROLLING_IMAGE_4 = "assets/images/manr-04.png"
    ROLLING_IMAGE_5 = "assets/images/manr-05.png"
    ROLLING_IMAGE_6 = "assets/images/manr-06.png"
    ROLLING_IMAGE_7 = "assets/images/manr-07.png"
    ROLLING_IMAGE_8 = "assets/images/manr-08.png"

    CLOUD_01 = "assets/images/cloud01.png"

   
    class ROCKS:
        ROCK01 = "assets/images/rocks/rock01.png"
        ROCK02 = "assets/images/rocks/rock02.png"
        ROCK03 = "assets/images/rocks/rock03.png"
        ROCK04 = "assets/images/rocks/rock04.png"
        ROCK05 = "assets/images/rocks/rock05.png"
        ROCK06 = "assets/images/rocks/rock06.png"
        ROCK07 = "assets/images/rocks/rock07.png"
        ROCK08 = "assets/images/rocks/rock08.png"
        ROCK09 = "assets/images/rocks/rock09.png"
        ROCK10 = "assets/images/rocks/rock10.png"
        ROCK11 = "assets/images/rocks/rock11.png"
        ROCK12 = "assets/images/rocks/rock12.png"
        ROCK13 = "assets/images/rocks/rock13.png"
        ROCK14 = "assets/images/rocks/rock14.png"
        ROCK15 = "assets/images/rocks/rock15.png"
        ROCK16 = "assets/images/rocks/rock16.png"
        ROCK17 = "assets/images/rocks/rock17.png"
        ROCK18 = "assets/images/rocks/rock18.png"
        ROCK19 = "assets/images/rocks/rock19.png"
        ROCK20 = "assets/images/rocks/rock20.png"
        ROCK21 = "assets/images/rocks/rock21.png"
        ROCK22 = "assets/images/rocks/rock22.png"
        ROCK23 = "assets/images/rocks/rock23.png"
        ROCK24 = "assets/images/rocks/rock24.png"
        ROCK25 = "assets/images/rocks/rock25.png"
        ROCK26 = "assets/images/rocks/rock26.png"
        ROCK27 = "assets/images/rocks/rock27.png"
        ROCK28 = "assets/images/rocks/rock28.png"
        ROCK29 = "assets/images/rocks/rock29.png"
        ROCK30 = "assets/images/rocks/rock30.png"
        
    class NPC :
        ENEMYBULLET = "assets/images/npc/enemybullet.png"

# 게임 리소스 경로
def path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
