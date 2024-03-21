import pygame
import math


class Hero:
    def __init__(self, screen):  # инициализация героя
        # Инициализация героя с передачей экрана для рисования
        self.screen = screen

        # Загрузка изображения героя
        self.original_image = pygame.image.load('image/turret_FACE_1.png')
        self.base_turret = pygame.image.load('image/turret_BASE.png')

        # Установка начального размера изображения
        self.width = 100
        self.height = 100

        # Масштабирование изображения героя
        self.image = pygame.transform.scale(self.original_image, (self.width, self.height))

        # Получение прямоугольника, описывающего положение изображения
        self.rect = self.image.get_rect()

        # Получение прямоугольника экрана
        self.screen_rect = screen.get_rect()

        # Установка начального положения героя в центре нижней части экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Установка начального положения базы турели таким же, как у героя
        self.rect_base = self.base_turret.get_rect()
        self.rect_base.centerx = self.rect.centerx
        self.rect_base.centery = self.rect.centery  # Центрирование базы турели по оси Y

    def output(self):
        # Вывод изображения базы турели на экран в его текущем положении
        self.screen.blit(self.base_turret, self.rect_base)

        # Вывод изображения героя на экран в его текущем положении
        self.screen.blit(self.image, self.rect)

    def rotate_towards_mouse(self):
        # Получение позиции курсора мыши
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Вычисление угла между героем и курсором мыши
        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery
        angle = math.degrees(math.atan2(dy, dx))

        # Поворот изображения героя
        self.image = pygame.transform.rotate(self.original_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)
