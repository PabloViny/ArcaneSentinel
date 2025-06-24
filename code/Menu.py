import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_GREEN, MENU_OPTION, C_WHITE


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:

            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Arcane Sentinel", C_GREEN, ((WIN_WIDTH / 2) + 5, 70))

            self.draw_menu_box(MENU_OPTION, 20, (WIN_WIDTH / 2), 145)
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.box_surface(text_rect, text_surf)
        self.window.blit(source=text_surf, dest=text_rect)

    # Create a box to insert the title of the game
    def box_surface(self, text_rect: Rect, text: Surface, valid=False):
        padding = 20
        box_width = text_rect.width + padding * 2
        box_height = text_rect.height + padding * 2
        box_x = text_rect.x - padding
        box_y = text_rect.y - padding

        shadow_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        pygame.draw.rect(shadow_surface, (0, 0, 0, 100), shadow_surface.get_rect(), border_radius=12)
        self.window.blit(shadow_surface, (box_x + 4, box_y + 4))

        box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        pygame.draw.rect(box_surface, (30, 30, 30, 180), box_surface.get_rect(), border_radius=12)
        self.window.blit(box_surface, (box_x, box_y))
        self.window.blit(text, text_rect)

    # Create a box to insert menu
    def draw_menu_box(self, options: list[str], font_size: int, center_x: int, top_y: int):
        font = pygame.font.SysFont("Lucida Sans Typewriter", font_size)

        # Renders the options to measure
        text_surfs = []
        max_width = 0
        total_height = 0
        line_spacing = 5

        for option in options:
            surf = font.render(option, True, C_WHITE).convert_alpha()
            text_surfs.append(surf)
            max_width = max(max_width, surf.get_width())
            total_height += surf.get_height() + line_spacing

        total_height -= line_spacing  # Remove extra spacing from the last line

        # Creates and draws the box that surrounds the option
        padding = 10
        box_width = max_width + padding * 2
        box_height = total_height + padding * 2
        box_x = center_x - box_width / 2
        box_y = top_y

        # Creating main box
        box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        pygame.draw.rect(box_surface, (30, 30, 30, 180), box_surface.get_rect(), border_radius=12)
        self.window.blit(box_surface, (box_x, box_y))

        # Draw the options inside the box
        current_y = box_y + padding
        for surf in text_surfs:
            rect = surf.get_rect(centerx=center_x, top=current_y)
            self.window.blit(surf, rect)
            current_y += surf.get_height() + line_spacing
