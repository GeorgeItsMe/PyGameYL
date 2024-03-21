import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, hero, image_path, transparent_color=None):
        super().__init__()
        self.screen = screen
        self.hero = hero
        self.image = pygame.image.load(image_path).convert_alpha()

        self.rect = self.image.get_rect()
        self.speed = 1  # Устанавливаем скорость врагов
        self.spawn()  # Перемещаем врага вне экрана при инициализации

    def spawn(self):
        side = random.randint(1, 4)  # Определяем случайную сторону спавна
        screen_width, screen_height = self.screen.get_size()
        spawn_margin = 50  # Отступ от границ экрана
        if side == 1:  # Спавн сверху
            self.rect.x = random.randint(spawn_margin, screen_width - self.rect.width - spawn_margin)
            self.rect.y = -self.rect.height

        elif side == 3 or side == 2:  # Спавн слева
            self.rect.x = -self.rect.width
            self.rect.y = random.randint(spawn_margin, screen_height - self.rect.height - spawn_margin)
        elif side == 4:  # Спавн справа
            self.rect.x = screen_width
            self.rect.y = random.randint(spawn_margin, screen_height - self.rect.height - spawn_margin)

    def update(self):
        # Перемещаем врагов к герою
        dx = self.hero.rect.centerx - self.rect.centerx
        dy = self.hero.rect.centery - self.rect.centery
        distance = max(1, (dx ** 2 + dy ** 2) ** 0.5)  # Расстояние между врагом и героем
        self.rect.x += self.speed * dx / distance
        self.rect.y += self.speed * dy / distance
        if distance < 5:  # если расстояние меньше 5 враг удаляется
            self.kill()

    def draw(self):
        self.screen.blit(self.image, self.rect)
