import pygame as pg
import os
from src.color.cores import colors
import math

pg.init()
largura = 1200
altura = 720
tela = pg.display.set_mode((largura, altura))
clock = pg.time.Clock()
rodando = True
base_dir = os.path.dirname(__file__)
image_path = os.path.join(base_dir,'..', 'assets', 'imagem2.png')
image = pg.image.load(image_path)
image_tamanho = pg.transform.smoothscale(image, (200, 100))
imagem_vertical = pg.transform.rotate(image_tamanho, 60)
imagem_atual = imagem_vertical
largura_img = imagem_atual.get_width()
bg_image = os.path.join(base_dir, '..', 'assets', 'background.png')
bacground = pg.image.load(bg_image)
pg.mixer.init()
imagem_bg = pg.transform.scale(bacground, (largura, altura))
sound_path  = os.path.join(base_dir, '..', 'sounds', 'explosion.wav')
desloca = os.path.join(base_dir, '..', 'sounds', 'select2.wav')
desloca_sound = pg.mixer.Sound(desloca )
sound = pg.mixer.Sound(sound_path )
atirando = False
angulo = 60
rad = math.radians(angulo)
dx = 0
dy = 0
velocidade_bala = 80

x = 20
y = 500
bala_x = 100
bala_y = 100
velocidade = 20

while rodando:
    
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            rodando = False

        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_SPACE:
                bala_x = x + 100
                bala_y = y

                if imagem_atual == imagem_vertical:
                    angulo = 60
                else:
                    angulo = 120

                rad = math.radians(angulo)

                dx = velocidade_bala * math.cos(rad)
                dy = -velocidade_bala * math.sin(rad)

                atirando = True
                sound.play(maxtime=50)

    tecla = pg.key.get_pressed()

    if tecla[pg.K_RIGHT]:
        imagem_atual = imagem_vertical
        x += velocidade
        desloca_sound.play(maxtime=50)
    if tecla[pg.K_LEFT]:
        imagem_atual = pg.transform.flip(imagem_vertical, True, False)
        x -= velocidade
        desloca_sound.play(maxtime=50)

    if x < 0:
        x = 0

    if x > largura - largura_img:
        x = largura - largura_img


    tela.blit(imagem_bg, (0, 0))

    tela.blit(imagem_atual, (x, y))

    if atirando:
        bala_x += dx
        bala_y += dy
        pg.draw.circle(tela, colors['Vermelho'], (int(bala_x), int(bala_y)), 8)

        if bala_x > largura or bala_y < 0:
            atirando = False

    pg.display.flip()

    clock.tick(15)

pg.quit()