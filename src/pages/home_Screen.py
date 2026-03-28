import pygame as pg
import os
from src.color.cores import colors
import math
from src.settings.setting import angle, bullet_x, bullet_y, dx, dy, width, height, bullet_speed, x, y, speed, position_x, position_y, speed_balls, image_x, interval, image_y
import random

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
pg.mixer.init()
move_sound = pg.mixer.Sound(sound_file_move)
shoot_sound = pg.mixer.Sound(sound_shoot)
pg.mixer.music.load(music_fille)
pg.mixer.music.play(-1)
shooting = False
last_time = pg.time.get_ticks()
balls = []

def little_balls(screen, color, position, ray):
    pg.draw.circle(screen, color, position, ray)

running = True

while running:

    current_time = pg.time.get_ticks()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                bullet_x = x + 100
                bullet_y = y

                if current_image == rotation_image:
                    angle = 60
                else:
                    angle = 120

                rad = math.radians(angle)

                dx = bullet_speed * math.cos(rad)
                dy = -bullet_speed * math.sin(rad)

                shooting = True
                shoot_sound.play(maxtime=50)

    keyboard = pg.key.get_pressed()

    if keyboard[pg.K_RIGHT]:
        current_image = rotation_image
        x += speed
        move_sound.play(maxtime=50)
    if keyboard[pg.K_LEFT]:
        current_image = pg.transform.flip(rotation_image, True, False)
        x -= speed
        move_sound.play(maxtime=50)

    if x < 0:
        x = 0

    if x > width - width_img:
        x = width - width_img


    screen.blit(bg_imagem, (0, 0))

    screen.blit(current_image, (x, y))

    if current_time - last_time > interval:
        balls.append([width, random.randint(0, height-350)])
        last_time = current_time
    
    for ball in balls:
        ball[0] -= speed_balls

    for ball in balls:
        little_balls(screen, colors['RosaClaro'], (int(ball[0]), int(ball[1])), 8)

    if shooting:
        bullet_x += dx
        bullet_y += dy
        pg.draw.circle(screen, colors['Vermelho'], (int(bullet_x), int(bullet_y)), 8)

        if bullet_x > width or bullet_y < 0:
            shooting = False

    pg.display.flip()

    clock.tick(15)

pg.quit()