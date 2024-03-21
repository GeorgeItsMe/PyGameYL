import pygame
import math

class Bullet:
    def __init__(self, screen, hero, angle):
        self.screen = screen
        self.hero = hero

        # Загрузка изображения пули
        self.image = pygame.image.load('image/turret_BULLET (1).png').convert_alpha()

        # Получение прямоугольника, описывающего положение пули
        self.rect = self.image.get_rect()

        # Начальное положение пули в центре героя
        self.rect.centerx = hero.rect.centerx
        self.rect.centery = hero.rect.centery

        # Установка начальной скорости пули
        self.speed = 10

        # Установка начального направления пули
        self.angle = angle

    def update(self):
        # Обновление положения пули в соответствии с направлением
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)

    def draw(self):
        # Отрисовка пули на экране
        self.screen.blit(self.image, self.rect)
