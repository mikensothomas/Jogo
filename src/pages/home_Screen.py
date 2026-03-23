# https://pt.console-linux.com/?p=28699
import pygame as pg
import os
from src.color.cores import colors

pg.init()
largura = 1200
altura = 720
tela = pg.display.set_mode((largura, altura))
clock = pg.time.Clock()
rodando = True
base_dir = os.path.dirname(__file__)
image_path = os.path.join('..', 'assets', 'imagem2.png')
image = pg.image.load(image_path)
image_tamanho = pg.transform.smoothscale(image, (200, 100))
imagem_vertical = pg.transform.rotate(image_tamanho, 60)
imagem_atual = imagem_vertical
largura_img = imagem_atual.get_width()
x = 20
y = 500
velocidade = 20

while rodando:
    
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            rodando = False

    tecla = pg.key.get_pressed()

    if tecla[pg.K_RIGHT]:
        imagem_atual = imagem_vertical
        x += velocidade
    if tecla[pg.K_LEFT]:
        imagem_atual = pg.transform.flip(imagem_vertical, True, False)
        x -= velocidade

    if x < 0:
        x = 0

    if x > largura - largura_img:
        x = largura - largura_img


    tela.fill(colors['VerdeClaro'])
    tela.blit(imagem_atual, (x, y))

    pg.display.flip()

    clock.tick(15)

pg.quit()