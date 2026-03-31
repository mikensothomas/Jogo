import pygame as pg
import os
from src.color.cores import colors
import math
import random
from src.settings.setting import (
    angle, 
    position_x, 
    position_y, 
    width, 
    height, 
    bullet_speed,
    speed, 
    speed_balls, 
    image_x, 
    interval, 
    image_y,
    ray,
    alpha,
    fade_speed,
    fade_direction
)
from src.pages.ball import BallGame
from src.pages.bullet import BulletGame

pg.init()
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
base_dir = os.path.dirname(__file__)
image_file = os.path.join(base_dir,'..', 'assets', 'imagem2.png')
image = pg.image.load(image_file)
image_size = pg.transform.smoothscale(image, (image_x, image_y))
rotation_image = pg.transform.rotate(image_size, angle)
current_image = rotation_image
width_img = current_image.get_width()
bg_image_path = os.path.join(base_dir, '..', 'assets', 'background.png')
load_bg_image = pg.image.load(bg_image_path)
bg_imagem = pg.transform.scale(load_bg_image, (width, height))
sound_shoot = os.path.join(base_dir, '..', 'sounds', 'explosion.wav')
sound_file_move = os.path.join(base_dir, '..', 'sounds', 'select2.wav')
music_fille = os.path.join(base_dir, '..', 'sounds', 'jazz_march_27.mp3')
sound_fille_Collision = os.path.join(base_dir, '..', 'sounds', 'bomb.wav')

pg.mixer.init()
pg.font.init()
move_sound = pg.mixer.Sound(sound_file_move)
shoot_sound = pg.mixer.Sound(sound_shoot)
collision_sound = pg.mixer.Sound(sound_fille_Collision)
pg.mixer.music.load(music_fille)
pg.mixer.music.play(-1)
last_time = pg.time.get_ticks()
balls = []
bullets  = []
score = 0
ball_game_count = 0
count_ball = 0
paused = False
started = False
finished = False
continueGame = False

font = pg.font.SysFont("Arial", 60)
font_menu = pg.font.SysFont("Arial", 25)
font_score = pg.font.SysFont("Arial", 30)
title = font.render("REBELIÃO DAS BOLINHAS", True, colors['Laranja'])
paused_game = font.render("JOGO PAUSADO", True, colors['Amarelo'])
pg.display.set_caption('REBELIÃO DAS BOLINHAS')

start = font_menu.render("I: Iniciar", True, colors['Verde'])
pause = font_menu.render("P: Pausar", True, colors['Amarelo'])
finish = font_menu.render("T: Terminar", True, colors['Vermelho'])
continue_game = font_menu.render("C: Continuar", True, colors['Laranja'])

running = True

while running:

    current_time = pg.time.get_ticks()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                bullet_x = position_x + 100
                bullet_y = position_y

                if current_image == rotation_image:
                    angle = 60
                else:
                    angle = 120

                rad = math.radians(angle)

                dx = bullet_speed * math.cos(rad)
                dy = -bullet_speed * math.sin(rad)

                bullets.append(BulletGame(screen, colors['Vermelho'], position_x + 100, position_y, dx, dy, ray))

                if not paused and started:
                    shoot_sound.play(maxtime=50)

            if event.key == pg.K_p:
                paused = True
            if event.key == pg.K_i:
                started = True
            if event.key == pg.K_c:
                if paused == True:
                    paused = False
            if event.key == pg.K_t:
                running = False

    keyboard = pg.key.get_pressed()
    pontuation = font_score.render(f"Pontuação: {score} ", True, colors['Laranja'])
    count = font_score.render(f"Acertou: {count_ball} em {ball_game_count} ", True, colors['Laranja'])

    if not paused:
        if started:
            if keyboard[pg.K_RIGHT]:
                current_image = rotation_image
                position_x += speed
                move_sound.play(maxtime=50)
            if keyboard[pg.K_LEFT]:
                current_image = pg.transform.flip(rotation_image, True, False)
                position_x -= speed
                move_sound.play(maxtime=50)

    if position_x < 0:
        position_x = 0

    if position_x > width - width_img:
        position_x = width - width_img

    screen.blit(bg_imagem, (0, 0))

    screen.blit(current_image, (position_x, position_y))

    if not paused:
        alpha += fade_speed * fade_direction
        if alpha > 255:
            alpha = 255
            fade_direction = -1
        elif alpha <= 0:
            alpha = 0
            fade_direction = 1
        
    title.set_alpha(alpha)

    if paused:
        screen.blit(paused_game, (360, 300))
        screen.blit(continue_game, (300, 10))
        
    screen.blit(title, (250, 50))
    screen.blit(pontuation, (950, 550))
    screen.blit(count, (950, 650))
    screen.blit(start, (10, 10))
    screen.blit(pause, (90, 10))
    screen.blit(finish, (190, 10))
    
    if not paused:
        if started:
            if current_time - last_time > interval:
                balls.append(BallGame(screen, colors['RosaClaro'], (width, random.randint(0, height-350)), 8))
                last_time = current_time
                ball_game_count += 1

            for ball in balls:
                ball.move_balls(speed_balls)
                ball.draw_balls()

            for bullet in bullets[:]:
                bullet.move_bullet()
                bullet.draw_bullet()

                if bullet.is_off_screen(width, height):
                    bullets.remove(bullet)

            for bullet in bullets[:]:
                for ball in balls[:]:
                    if bullet.collide(ball):
                        balls.remove(ball)
                        count_ball += 1
                        bullets.remove(bullet)
                        score += 10
                        collision_sound.play()
                        break
                
    pg.display.flip()

    clock.tick(15)

pg.quit()