import pygame


class Ship:
    """Класс для управления кораблём."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задаёт начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля, и получает его коллизию в виде прямоугольника
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется посередине снизу.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует корабль на текущей позиции."""
        self.screen.blit(self.image, self.rect)
