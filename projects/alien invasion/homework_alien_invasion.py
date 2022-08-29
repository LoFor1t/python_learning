import sys

import pygame

from homework_settings import Settings
from homework_ship import Ship


class AlienInvasion:
    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.sheep = Ship(self)

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и событий мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.sheep.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
