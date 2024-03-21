import pygame
import sys
import math
import random
from hero import Hero
from enemy import Enemy
from bullet import Bullet

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Space Defend')


    # Загрузка звукового эффекта стрельбы
    shoot_sound = pygame.mixer.Sound('sounds/fire.mp3')

    hero = Hero(screen)
    enemies = pygame.sprite.Group()  # Группа для хранения врагов
    bullets = []  # Создаем список для хранения пуль
    enemy_spawn_delay = 0
    enemy_spawn_interval = 500  # Интервал спавна врагов (в миллисекундах)
    killed_enemies = 0  # Переменная для хранения счетчика убитых врагов
    enemy_not_killed = 0
    clock = pygame.time.Clock()
    background = pygame.image.load('image/backroung.jpg').convert()
    background_rect = background.get_rect()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - hero.rect.centerx
                dy = mouse_y - hero.rect.centery
                angle = math.atan2(dy, dx)
                new_bullet = Bullet(screen, hero, angle)
                bullets.append(new_bullet)

                # Воспроизведение звука стрельбы
                shoot_sound.play()

        screen.blit(background, background_rect)

        # Обновляем и отрисовываем все пули в списке
        for bullet in bullets:
            bullet.update()
            bullet.draw()

        # Обновляем и отрисовываем всех врагов в группе
        for enemy in enemies:
            enemy.update()
            enemy.draw()

        # Проверка столкновения пуль с врагами
        for bullet in bullets:
            for enemy in enemies:
                if bullet.rect.colliderect(enemy.rect):  # Проверяем столкновение пули с врагом
                    bullets.remove(bullet)  # Удаляем пулю
                    enemies.remove(enemy)  # Удаляем врага
                    killed_enemies += 1  # Увеличиваем счетчик убитых врагов

        # Поворот героя в направлении курсора мыши
        hero.rotate_towards_mouse()
        hero.output()  # Отображение героя

        # Обновление спавна врагов
        enemy_spawn_delay += clock.tick()
        if enemy_spawn_delay >= enemy_spawn_interval:
            new_enemy = Enemy(screen, hero, 'image/FinalEnemy (1).png')
            enemies.add(new_enemy)
            enemy_spawn_delay = 0
            enemy_not_killed += 1
        # Отображение счетчика убитых врагов на экране
        font = pygame.font.Font(None, 36)
        text = font.render(f"Убито врагов: {killed_enemies}/{enemy_not_killed}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()

run()
