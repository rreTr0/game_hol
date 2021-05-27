
import pygame

pygame.init()

PINK = (255, 105, 180)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

W, H = 500, 500
SIZE = (W, H)

y = int(H * 0.8)
x = W // 2

is_jump = False
jump_counter = 20

sc = pygame.display.set_mode(SIZE)
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    sc.fill(GREEN)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        is_jump = True
    
    if is_jump is True and jump_counter >= -20:
        y -= jump_counter * 2
        jump_counter -= 2
    else:
        is_jump = False
        jump_counter = 20

    pygame.draw.circle(sc, PINK, (x, y), 50)
    pygame.display.update()
