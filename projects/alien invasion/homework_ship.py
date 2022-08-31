import pygame


class Ship:
    """Класс для управления кораблём."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задаёт начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Загружает изображение корабля, и получает его коллизию в виде прямоугольника
        self.image = pygame.image.load('images/ship.bmp')
        self.rotate_image = pygame.transform.rotate(self.image, -90)
        self.rect = self.rotate_image.get_rect()

        # Каждый новый корабль появляется посередине снизу.
        self.rect.midleft = self.screen_rect.midleft

        # Сохранение вещественной координаты корабля.
        self.y = float(self.rect.y)

        # Флаги перемещения
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учётом флагов."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Обновление атрибута rect на основании self.x и self.y
        self.rect.y = self.y

    def blitme(self):
        """Рисует корабль на текущей позиции."""
        self.screen.blit(self.rotate_image, self.rect)
