import pygame as pg

class BallGame:

    def __init__(self, screen, color, position, ray):
        self.screen = screen
        self.color = color
        self.position = list(position)
        self.ray = ray

    def draw_balls(self):
        pg.draw.circle(self.screen, self.color, self.position, self.ray)
    
    def move_balls(self, speed):
        self.position = (self.position[0] - speed, self.position[1])