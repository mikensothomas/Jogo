import pygame as pg

class Timer_game:
    def __init__(self, tempo_inicial):
        self.tempo = tempo_inicial
        self.last_time = pg.time.get_ticks()
    
    def update(self):
        current_time = pg.time.get_ticks()

        if current_time - self.last_time > 1000:
            self.last_time = current_time
            self.tempo -= 1
            return True
        return False