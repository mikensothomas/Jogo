import random
from src.pages.ball import BallGame
from src.pages.timer import Timer_game
from src.color.cores import colors

class Level:

    def __init__(self, numero, tempo, bolas_spawn, background):
        self.numero = numero
        self.timer = Timer_game(tempo)
        self.bolas_spawn = bolas_spawn
        self.background = background

    def update(self):
        return self.timer.update()

    def draw_background(self, screen):
        screen.blit(self.background, (0, 0))

    def spawn_balls(self, balls, screen, width, height):
        
        for _ in range(self.bolas_spawn):

            balls.append(
                BallGame(
                    screen,
                    colors['RosaClaro'],
                    (width, random.randint(0, height - 350)),
                    8
                )
            )