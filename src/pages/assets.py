import pygame as pg
import os

class Assets:
    def __init__(self, base_dir, width, height, image_x, image_y, angle):

        self.base_dir = base_dir
        self.width = width
        self.height = height

        # ================= IMAGEM ARMA =================
        image_file = os.path.join(base_dir, '..', 'assets', 'imagem2.png')
        image = pg.image.load(image_file)

        self.weapon_image = pg.transform.smoothscale(image, (image_x, image_y))
        self.weapon_image = pg.transform.rotate(self.weapon_image, angle)

        self.half_width = self.weapon_image.get_width() // 2

        # ================= SONS =================
        self.sound_shoot = pg.mixer.Sound(os.path.join(base_dir, '..', 'sounds', 'explosion.wav'))
        self.sound_move = pg.mixer.Sound(os.path.join(base_dir, '..', 'sounds', 'select2.wav'))
        self.sound_collision = pg.mixer.Sound(os.path.join(base_dir, '..', 'sounds', 'bomb.wav'))

        self.music = os.path.join(base_dir, '..', 'sounds', 'jazz_march_27.mp3')

        # ================= BACKGROUNDS =================
        self.bg1 = self.load_image('background.png')
        self.bg2 = self.load_image('background_image.jpg')
        self.bg3 = self.load_image('background_image_3.jpg')

        # ================= HISTÓRICO =================
        self.gatinho = self.load_image('gatinho.png', (550, 470))
        self.pngtree = self.load_image('pngtree.png', (550, 470))

    def load_image(self, filename, size=None):
        path = os.path.join(self.base_dir, '..', 'assets', filename)
        img = pg.image.load(path)

        if size:
            img = pg.transform.scale(img, size)

        return img