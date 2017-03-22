import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # Создание экземпляра для хранения игровой статистики.
    stats = GameStats(ai_settings)

    # Создание корабля.
    ship = Ship(screen, ai_settings)
    # Создание группы для хранения пуль.
    bullets = Group()
    # Создание группы для хранения пришельцев.
    aliens = Group()

    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
