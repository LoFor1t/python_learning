class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализируем настройки игры."""
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 250)

        # Настройки корабля.
        self.ship_speed = 1.5

        # Настройки снарядов
        self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
