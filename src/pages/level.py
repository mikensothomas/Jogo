import pygame as pg
from src.pages.timer import Timer_game

class Level:
    def __init__(self, level_number, title, background, tempo_inicial, bolas_por_spawn):
        self.level_number = level_number
        self.title = title
        self.background = background
        self.timer = Timer_game(tempo_inicial)
        self.bolas_por_spawn = bolas_por_spawn