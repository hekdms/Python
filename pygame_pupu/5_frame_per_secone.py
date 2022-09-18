import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥 피하기")

clock = pygame.time.Clock()

background = pygame.image.load("C:\\Users\\h6263\\Desktop\\스터디\\파이썬\\pygame_pupu\\background.png")

character = pygame.image.load("C:\\Users\\h6263\\Desktop\\스터디\\파이썬\\pygame_pupu\\character1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

to_x = 0

character_speed = 0.4

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

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()