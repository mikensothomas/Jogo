import pygame as pg
from src.color.cores import colors

class ScreenGame:

    def __init__(self, screen):

        self.screen = screen
        pg.font.init()

        self.font_title = pg.font.SysFont("Arial", 60)
        self.font_menu = pg.font.SysFont("Arial", 25)
        self.font_score = pg.font.SysFont("Arial", 30)
        self.font = pg.font.SysFont("Arial", 30)

    def draw_title(self, nivel, alpha):

        title = self.font_title.render(f"REBELIÃO DAS BOLINHAS NÍVEL {nivel}",True,colors['Laranja'])
        title.set_alpha(alpha)
        self.screen.blit(title, (250, 50))

    def draw_menu(self):

        start = self.font_menu.render("I: Iniciar",True,colors['Verde'])
        pause = self.font_menu.render("P: Pausar",True,colors['Amarelo'])
        finish = self.font_menu.render("T: Terminar",True,colors['Vermelho'])
        continue_game = self.font_menu.render("C: Continuar",True,colors['Laranja'])

        self.screen.blit(start, (10, 10))
        self.screen.blit(pause, (90, 10))
        self.screen.blit(finish, (190, 10))
        self.screen.blit(continue_game, (300, 10))


    def draw_score(self, score):

        pontuation = self.font_score.render(f"Pontuação: {score}",True,colors['Laranja'])
        self.screen.blit(pontuation, (950, 550))

    def draw_hits(self, count_ball, ball_game_count):

        count = self.font_score.render(f"Acertou: {count_ball} em {ball_game_count}",True,colors['Laranja'])
        self.screen.blit(count, (950, 650))

    def draw_shots(self, bullet_move_count):

        shots_text = self.font_score.render(f"Tiros: {bullet_move_count}",True,colors['Vermelho'])
        self.screen.blit(shots_text, (10, 75))

    def draw_timer(self, tempo):

        time_text = self.font_score.render(f"Tempo: {tempo}",True,colors['Laranja'])
        self.screen.blit(time_text, (10, 40))

    def draw_pause(self):

        paused_game = self.font_title.render("JOGO PAUSADO",True,colors['Amarelo'])
        self.screen.blit(paused_game, (360, 300))

    def draw_historic(self, player_name, score, hits, total_balls):

        historic_game_ball = self.font_score.render(f"Em: {total_balls} bolinhas você acertou: {hits}",True,colors['Laranja'])
        historic_game_score = self.font_score.render(f"Você ganhou: {score} pontos",True,colors['Laranja'])
        name_surface = self.font_score.render(f"Nome: {player_name}",True,colors['Laranja'])

        self.screen.blit(historic_game_score, (360, 100))
        self.screen.blit(historic_game_ball, (360, 200))
        self.screen.blit(name_surface, (360, 300))

    def draw_win(self):

        coungratulation = self.font_score.render("Parabéns, você ganhou o jogo",True,colors['Laranja'])
        self.screen.blit(coungratulation, (360, 400))

    def draw_lose(self):

        not_coungratulation = self.font_score.render("Você perdeu a partida",True,colors['Vermelho'])
        self.screen.blit(not_coungratulation, (360, 400))

    def draw_final_buttons(self):

        return_to_start = self.font_score.render("V: Voltar ao início",True,colors['Laranja'])
        close_window = self.font_score.render("F: Fechar o jogo",True,colors['Vermelho'])

        self.screen.blit(return_to_start, (10, 10))
        self.screen.blit(close_window, (220, 10))
    
    def draw_player_name(self, name):
        text = self.font.render(f"Nome: {name}", True, colors['Laranja'])
        self.screen.blit(text, (360, 300))