import pygame

pygame.init()
class Player():
    """ Жук :) """
    health = 3
    attack = 4
    imghollow = pygame.image.load('жучок.png')
    imghollow = pygame.transform.scale(imghollow, (200, 200))
    x = 500
    y = 660
    keys = pygame.key.get_pressed()
    is_jump = False
    jump_counter = 20
        
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
        
        if self.is_jump is True and self.jump_counter >= -20:
            self.y -= self.jump_counter * 2
            self.jump_counter -= 2
        else:
            self.is_jump = False
            self.jump_counter = 20



class Map():
    """ КАРТА """
    imgmap = pygame.image.load('map.png')
    imgmap = pygame.transform.scale(imgmap, (1000, 1000))
    img = pygame.image.load('podstavka.png')
    def drawmap(self):
        sc.blit(self.imgmap, (0, 0))

    
        

W = 1000
H = 1000
sc = pygame.display.set_mode((W, H))
red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)
black = (0, 0, 0)
bug = Player()
fon = Map()



while True:
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            pygame.quit()
            exit()
    
    bug.move()
    bug.jump()

    sc.fill(red)
    fon.draw()
    bug.draw()

    pygame.display.update()