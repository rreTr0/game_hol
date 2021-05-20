import pygame

W, H = 500, 500
SIZE = (W, H)

sc = pygame.display.set_mode(SIZE)

img = pygame.image.load("комар.png")

true = True


while true:
    sc.fill ((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            pygame.quit()


    sc.blit(img,(W // 10, H // 10))
    pygame.display.update()