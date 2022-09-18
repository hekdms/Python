import random
from turtle import color
import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥 피하기")

clock = pygame.time.Clock()

background = pygame.image.load("C:\\Users\\h6263\\Desktop\\스터디\\파이썬\\pygame_pupu\\background.jpg")

character = pygame.image.load("C:\\Users\\h6263\\Desktop\\스터디\\파이썬\\pygame_pupu\\character1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height
character_speed = 0.4

to_x = 0

enemy = pygame.image.load("C:\\Users\\h6263\\Desktop\\스터디\\파이썬\\pygame_pupu\\enemy1.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - character_width)
enemy_y_pos = 0
enemy_speed = 15

# 폰트 및 타이머
game_font = pygame.font.Font(None, 70)

total_time = 10

start_ticks = pygame.time.get_ticks()

running = True
while running :
    dt = clock.tick(30)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT :
                to_x += character_speed

        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0

    character_x_pos += to_x * dt

    enemy_y_pos += enemy_speed

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    if enemy_y_pos > screen_height :
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect) :
        print("충돌했어요")
        running = False

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (0, 0, 0))

    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0 :
        print("시간 종료")
        running = False


    pygame.display.update()

pygame.time.delay(1000)

pygame.quit()