import pygame

pygame.init()
class Player():
    """ Жук :) """
    health = 3
    attack = 4
    imghollow = pygame.image.load(r'\\erudite.local\Users$\Docs\prc7\Рабочий стол\images/жучок.png')
    imghollow = pygame.transform.scale(imghollow, (200, 200))
    xbug = 500
    ybug = 660
    keys = pygame.key.get_pressed()
        
    def draw(self):
        sc.blit(self.imghollow,(self.xbug, self.ybug))
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.xbug -= 5
        if keys[pygame.K_RIGHT]:
            self.xbug += 5
        pygame.display.update()

class Map():
    """ КАРТА """
    imgmap = pygame.image.load(r'C:\Users\prc7\Downloads/map.png')
    imgmap = pygame.transform.scale(imgmap, (1000, 1000))
    def draw():
        sc.blit(self.imgmap, (0, 0))

W = 1000
H = 1000
sc = pygame.display.set_mode((W, H))
red = (0, 255, 0)
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
    sc.fill(red)
    bug.draw()
    bug.move()
    fon.draw()
    pygame.display.update()
