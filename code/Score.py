import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, K_RETURN, KEYDOWN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import C_YELLOW, SCORE_POS, MENU_OPTION, C_WHITE, WIN_WIDTH
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.menu_option = 0

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', C_WHITE, SCORE_POS['Title'])
            text = 'Enter player 1 name (4 characters): '
            score = player_score[0]
            if game_mode == MENU_OPTION[0]:
                text = 'Enter player 1 name (4 characters): '
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team name (4 characters): '
            if game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Enter player 1 name (4 characters): '
                else:
                    score = player_score[1]
                    text = 'Enter player 2 name (4 characters): '
            self.score_text(15, text, C_YELLOW, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(13, name, C_YELLOW, SCORE_POS['Name'])
            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(40, 'TOP 3 SCORE', C_YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NAME     SCORE           DATE      ', C_YELLOW, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score:05d}     {date}', C_YELLOW,
                            SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)

        # Renderiza o texto normalmente
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        # Cria uma caixa com padding ao redor do texto
        padding_x = 20
        padding_y = 10
        box_width = text_rect.width + padding_x * 2
        box_height = text_rect.height + padding_y * 2
        box_x = text_rect.centerx - box_width // 2
        box_y = text_rect.centery - box_height // 2

        # Cria a superfície da caixa (com transparência e borda arredondada)
        box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        pygame.draw.rect(box_surface, (30, 30, 30, 180), box_surface.get_rect(), border_radius=12)

        # Desenha a caixa e depois o texto sobre ela
        self.window.blit(box_surface, (box_x, box_y))
        self.window.blit(text_surf, text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
