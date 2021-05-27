import pygame
from random import randint

pygame.init()
W = 700
H = 700
sc = pygame.display.set_mode((W, H))
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 200, 200)
black = (0, 0, 0)

class Bug():
    """ Жук :) """
    health = 3
    attack = 4
    imghollow = pygame.image.load('жучок.png')
    imghollow = pygame.transform.scale(imghollow, (150, 150))
    x = W // 2
    y = int(H * 0.75)
    keys = pygame.key.get_pressed()
    is_jump = False
    jump_counter_base = 25
    jump_counter = jump_counter_base
        
    def draw(self):
        sc.blit(self.imghollow,(self.x, self.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.is_jump = True
        
        if self.is_jump is True and self.jump_counter >= -self.jump_counter_base:
            self.y -= self.jump_counter
            self.jump_counter -= 1
        else:
            self.is_jump = False
            self.jump_counter = self.jump_counter_base

    def check_podst(self, list_podsts):
        is_platf = False
        for podst in list_podsts:
            if podst[0] < self.x < podst[0] + 100:
                if podst[1] < self.y + 150 < podst[1] + 5:
                    self.is_jump = False
                    self.jump_counter = self.jump_counter_base
                    is_platf = True
        if is_platf is False and self.y > int(H * 0.75):
            self.y += 1


class Map():
    """ КАРТА """
    imgmap = pygame.image.load('map.png')
    imgmap = pygame.transform.scale(imgmap, (W, H))
    
    podst_img = pygame.image.load('podstavka.png')
    podst_img = pygame.transform.scale(podst_img, (100, 50))
    
    coords_podsts = []
    for i in range(3):
        coords_podsts.append((randint(0, int(W * 0.9)),\
            randint(0, int(H * 0.8))))


    def draw(self):
        sc.blit(self.imgmap, (0, 0))
        for podst in self.coords_podsts:
            sc.blit(self.podst_img, podst)


bug = Bug()
background = Map()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    bug.move()
    bug.jump()
    bug.check_podst(background.coords_podsts)

    sc.fill(GREEN)
    background.draw()
    bug.draw()
    pygame.display.update()

    pygame.time.delay(10)