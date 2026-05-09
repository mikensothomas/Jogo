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
    image_y,
    ray,
    alpha,
    fade_speed,
    fade_direction,
    gatinho_x,
    gatinho_y,
    vel_x,
    vel_y
)
from src.pages.ball import BallGame
from src.pages.bullet import BulletGame
from src.pages.timer import Timer_game
from src.pages.name import PlayerName
from src.pages.level import Level

pg.init()
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
base_dir = os.path.dirname(__file__)

# Arma
image_file = os.path.join(base_dir,'..', 'assets', 'imagem2.png')
image = pg.image.load(image_file)
image_size = pg.transform.smoothscale(image, (image_x, image_y))
rotation_image = pg.transform.rotate(image_size, angle)
current_image = rotation_image
half_width = current_image.get_width() // 2

# Sons
sound_shoot = os.path.join(base_dir, '..', 'sounds', 'explosion.wav')
sound_file_move = os.path.join(base_dir, '..', 'sounds', 'select2.wav')
music_fille = os.path.join(base_dir, '..', 'sounds', 'jazz_march_27.mp3')
sound_fille_Collision = os.path.join(base_dir, '..', 'sounds', 'bomb.wav')

# Imagens da primeira tela
bg_image_path = os.path.join(base_dir, '..', 'assets', 'background.png')
load_bg_image = pg.image.load(bg_image_path)
bg_imagem = pg.transform.scale(load_bg_image, (width, height))

# Imagens da segunda tela
bg_image_path2 = os.path.join(base_dir, '..', 'assets', 'background_image.jpg')
load_bg2_image_load = pg.image.load(bg_image_path2)
load_bg2_image = pg.transform.scale(load_bg2_image_load, (width, height))

# Imagem de historico
gatinho_image = os.path.join(base_dir, '..', 'assets', 'gatinho.png')
gatinho_image_load = pg.image.load(gatinho_image)
gatinho_image_load_size = pg.transform.scale(gatinho_image_load, (550, 470))

gatinho_image_pngtree = os.path.join(base_dir, '..', 'assets', 'pngtree.png')
gatinho_image_load_pngtree = pg.image.load(gatinho_image_pngtree)
gatinho_image_load_size_pngtree = pg.transform.scale(gatinho_image_load_pngtree, (550, 470))

# imagens da terceira tela
bg_image_path3 = os.path.join(base_dir, '..', 'assets', 'background_image_3.jpg')
load_bg3_image_load = pg.image.load(bg_image_path3)
load_bg3_image = pg.transform.scale(load_bg3_image_load, (width, height))

pg.mixer.init()
pg.font.init()
move_sound = pg.mixer.Sound(sound_file_move)
shoot_sound = pg.mixer.Sound(sound_shoot)
collision_sound = pg.mixer.Sound(sound_fille_Collision)
pg.mixer.music.load(music_fille)
pg.mixer.music.play(-1)
last_time_gatinho = pg.time.get_ticks()
balls = []
bullets  = []
score = 0
ball_game_count = 0
count_ball = 0
paused = False
started = False
finished = False
continueGame = False
end_game = False
show_return = False
bullet_move_count = 0
historico = False
nivel_atual = 1
tick = False

font = pg.font.SysFont("Arial", 60)
font_menu = pg.font.SysFont("Arial", 25)
font_score = pg.font.SysFont("Arial", 30)
paused_game = font.render("JOGO PAUSADO", True, colors['Amarelo'])
pg.display.set_caption('REBELIÃO DAS BOLINHAS')

start = font_menu.render("I: Iniciar", True, colors['Verde'])
pause = font_menu.render("P: Pausar", True, colors['Amarelo'])
finish = font_menu.render("T: Terminar", True, colors['Vermelho'])
continue_game = font_menu.render("C: Continuar", True, colors['Laranja'])

timer1 = Timer_game(20)
timer2 = Timer_game(20)
timer3 = Timer_game(20)
player = PlayerName(screen, font)

level1 = Level(1, 20, 1, bg_imagem)
level2 = Level(2, 20, 2, load_bg2_image)
level3 = Level(3, 20, 3, load_bg3_image)

levels = { 1: level1, 2: level2, 3: level3 }

def handle_global_input(event):
    global paused, started, end_game, running, historico

    if event.key == pg.K_p:
        paused = True
    elif event.key == pg.K_i:
        started = True
    elif event.key == pg.K_c and paused:
        paused = False
    elif event.key == pg.K_t:
        end_game = True
        historico = True
    elif event.key == pg.K_f:
        running = False


running = True
get_player_name = player.get_name()

while running:

    current_level = levels.get(nivel_atual)
    if current_level:
        title = font.render(f"REBELIÃO DAS BOLINHAS NÍVEL {current_level.numero}",True,colors['Laranja'])
        time_text = font_score.render(f"Tempo: {current_level.timer.tempo}",True,colors['Laranja'])

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:

            handle_global_input(event)

            if not paused and started:
                if event.key == pg.K_SPACE:

                    gun_tip_offset_1 = (-20, 20)
                    gun_tip_offset_2 = (-10, -70)

                    offset_x, offset_y = gun_tip_offset_1
                    rad = math.radians(angle)
                    center_x = position_x
                    center_y = position_y

                    rotated_x = offset_x * math.cos(rad) - offset_y * math.sin(rad)
                    rotated_y = offset_x * math.sin(rad) + offset_y * math.cos(rad)

                    bullet_x = center_x + rotated_x
                    bullet_y = center_y + rotated_y

                    dx = bullet_speed * math.cos(rad)
                    dy = -bullet_speed * math.sin(rad)

                    bullets.append(BulletGame(screen, colors['Vermelho'], bullet_x, bullet_y, dx, dy, ray))
                    bullet_move_count += 1

                    if not paused and started:
                        shoot_sound.play(maxtime=50)
    keyboard = pg.key.get_pressed()

    if not paused:
        alpha += fade_speed * fade_direction
        if alpha > 255:
            alpha = 255
            fade_direction = -1
        elif alpha <= 0:
            alpha = 0
            fade_direction = 1
            
    title.set_alpha(alpha)

    pontuation = font_score.render(f"Pontuação: {score}", True, colors['Laranja'])
    count = font_score.render(f"Acertou: {count_ball} em {ball_game_count}", True, colors['Laranja'])
    shots_text = font_score.render(f"Tiros: {bullet_move_count}", True, colors['Vermelho'])
    historic_game_ball = font_score.render(f"Em: {ball_game_count} bolinhas você acertou: {count_ball}", True, colors['Laranja'])
    historic_game_score = font_score.render(f"Você ganhou: {score} pontos", True, colors['Laranja'])
    coungratulation = font_score.render("Parabéns, você Ganhou o jogo", True, colors['Laranja'])
    not_coungratulation = font_score.render("Você perdeu a partida", True, colors['Vermelho'])
    return_to_start = font_score.render("V: Voltar ao início", True, colors['Laranja'])
    close_window = font_score.render("F: Fechar o jogo", True, colors['Vermelho'])
    rect = current_image.get_rect(center=(position_x, position_y))

    if not started:
        screen.blit(bg_imagem, (0, 0))
        screen.blit(title, (250, 50))
        screen.blit(start, (10, 10))
        screen.blit(finish, (100, 10))
    if current_level and started:

        current_level.draw_background(screen)
        
        if not paused:
            tick = current_level.update()

        screen.blit(current_image, rect)
        screen.blit(title, (250, 50))
        screen.blit(time_text, (10, 40))
        screen.blit(pontuation, (950, 550))
        screen.blit(count, (950, 650))
        screen.blit(start, (10, 10))
        screen.blit(shots_text, (10, 75))
        screen.blit(pause, (90, 10))
        screen.blit(finish, (190, 10))

        if paused:
            screen.blit(paused_game, (360, 300))
            screen.blit(continue_game, (300, 10))

        if tick:
            current_level.spawn_balls(balls, screen, width, height)
            ball_game_count += current_level.bolas_spawn

        for ball in balls:
            
            if not paused:
                ball.move_balls(speed_balls)

            ball.draw_balls()

        for bullet in bullets[:]:
            
            if not paused:
                bullet.move_bullet()
                
            bullet.draw_bullet()

            if bullet.is_off_screen(width, height):
                bullets.remove(bullet)
                
        if position_x - half_width < 0:
            position_x = half_width

        if position_x + half_width > width:
            position_x = width - half_width

        if not paused and started:
            if keyboard[pg.K_RIGHT]:
                position_x += speed
                move_sound.play(maxtime=50)

            if keyboard[pg.K_LEFT]:
                position_x -= speed
                move_sound.play(maxtime=50) 

        if not paused and started:
            if keyboard[pg.K_RIGHT]:
                position_x += speed
                move_sound.play(maxtime=50)

            if keyboard[pg.K_LEFT]:
                position_x -= speed
                move_sound.play(maxtime=50)

            for bullet in bullets[:]:
                for ball in balls[:]:

                    if bullet.collide(ball):

                        balls.remove(ball)
                        bullets.remove(bullet)

                        count_ball += 1
                        score += 10

                        collision_sound.play()

                        break
        if current_level and current_level.timer.tempo == 0:

            if count_ball >= (ball_game_count * 0.7):

                nivel_atual += 1

            else:
                historico = True
# ===============================================================================================================================================
    if nivel_atual == 4 or historico:
        paused = True

        largura_gatinho = gatinho_image_load_size.get_width()
        altura_gatinho = gatinho_image_load_size.get_height()

        pngtree_largura_gatinho = gatinho_image_load_size_pngtree.get_width()
        pngtree_altura_gatinho = gatinho_image_load_size_pngtree.get_height()

        current_image_gatinho = pg.time.get_ticks()
        screen.blit(bg_imagem, (0, 0))
        name_surface = font_score.render(f"Nome: {get_player_name}", True, colors['Laranja'])
        screen.blit(name_surface, (360, 300))
        screen.blit(historic_game_ball, (360, 200))
        screen.blit(historic_game_score, (360, 100))
        if show_return:
            screen.blit(return_to_start, (10, 10))
        screen.blit(close_window, (220, 10))

        if count_ball >= (ball_game_count * 0.7):
            screen.blit(coungratulation, (360, 400))
            screen.blit(gatinho_image_load_size, (gatinho_x, gatinho_y))

            if current_image_gatinho - last_time_gatinho > 500:
                gatinho_x += vel_x
                gatinho_y += vel_y

                last_time_gatinho = current_image_gatinho

                if gatinho_x <= 0:
                    gatinho_x = 0
                    vel_x *= -1

                elif gatinho_x >= width - largura_gatinho:
                    gatinho_x = width - largura_gatinho
                    vel_x *= -1

                if gatinho_y <= 0:
                    gatinho_y = 0
                    vel_y *= -1

                elif gatinho_y >= height - altura_gatinho:
                    gatinho_y = height - altura_gatinho
                    vel_y *= -1
            
        else:
            screen.blit(not_coungratulation, (360, 400))
            screen.blit(gatinho_image_load_size_pngtree, (gatinho_x, gatinho_y))

            if current_image_gatinho - last_time_gatinho > 500:
                gatinho_x += vel_x
                gatinho_y += vel_y

                last_time_gatinho = current_image_gatinho

                if gatinho_x <= 0:
                    gatinho_x = 0
                    vel_x *= -1

                elif gatinho_x >= width - pngtree_largura_gatinho:
                    gatinho_x = width - pngtree_largura_gatinho
                    vel_x *= -1

                if gatinho_y <= 0:
                    gatinho_y = 0
                    vel_y *= -1

                elif gatinho_y >= height - pngtree_altura_gatinho:
                    gatinho_y = height - pngtree_altura_gatinho
                    vel_y *= -1
    pg.display.flip()

    clock.tick(15)

pg.quit()