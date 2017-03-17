import sys
import pygame


def check_events():
    """Обрабатывает нажатия клавиш и события мыши."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
