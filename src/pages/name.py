import pygame as pg
from src.color.cores import colors

class PlayerName:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.name = ""

    def get_name(self):
        writing = True

        while writing:
            self.screen.fill(colors['preto'])

            text = self.font.render("Digite seu nome:", True, colors['Branco'])
            self.screen.blit(text, (180, 300))

            name_txt = self.font.render(self.name, True, colors['Azul'])
            self.screen.blit(name_txt, (200, 350))

            pg.display.update()

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

                if event.type == pg.KEYDOWN:

                    if event.key == pg.K_RETURN and self.name != "":
                        writing = False

                    elif event.key == pg.K_BACKSPACE:
                        self.name = self.name[:-1]

                    else:
                        self.name += event.unicode

        return self.name