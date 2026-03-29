import pygame as pg

class BulletGame:
    def __init__(self, screen, color, position_x, position_y, speed_bullet_x,speed_bullet_y, ray):
        self.screen = screen
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.speed_bullet_x = speed_bullet_x
        self.speed_bullet_y = speed_bullet_y
        self.ray = ray
    
    def draw_bullet(self):
        pg.draw.circle(self.screen, self.color, (int(self.position_x), int(self.position_y)), self.ray)

    def move_bullet(self):
        self.position_x += self.speed_bullet_x
        self.position_y += self.speed_bullet_y
    
    def is_off_screen(self, width, height):
        return self.position_x > width or self.position_y < 0 or self.position_y > height

    def collide(self, ball):
        dx = self.position_x - ball.position[0]
        dy = self.position_y - ball.position[1]
        distance = (dx**2 + dy**2) ** 0.5

        return distance < (self.ray + ball.ray + 5)