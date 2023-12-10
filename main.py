import pygame
import charackter
import eneny
import Gold
from wall import Wall
import random

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('the bab baby of getto.mp3')
pygame.mixer.music.play(-1)

window = pygame.display.set_mode((800 , 500))
fps = pygame.time.Clock()

fon = pygame.image.load("pixelartwall.png")
fon =  pygame.transform.scale(fon  , (800 , 500))

walls = []

spidor = charackter.Charackter(250 , 350 , 50 , 50  ,5  , "pixelartbobr2.png")
enemy = eneny.Enemy(130 , 340 , 50 , 50  ,2  , "pixil-frame-0.png" , 100 ,200 ,300 ,300)
gold1 = Gold.Gold(400 , 250 , 50 , 50 , "pixelartbottle.png")

walls.append(Wall(random.randint(-200 , 600) , random.randint(0 , 490) , 200 , 10 ,(0 , 0 , 0)))
walls.append(Wall(random.randint(0 , 790) , random.randint(0 , 300) , 10 , 200 ,(255 , 255 , 255)))
walls.append(Wall(random.randint(-200 , 600) , random.randint(0 , 490) , 200 , 10 ,(0 , 0 , 0)))
walls.append(Wall(random.randint(0 , 790) , random.randint(0 , 300) , 10 , 200 ,(255 , 255 , 255)))



game = True
while game :
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x , y = pygame.mouse.get_pos()
            print(x , y)
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    spidor.move()
    enemy.move()

    window.fill((255 , 0 , 0))
    window.blit(fon ,  (0  , 0 ))
    for i in walls:
        i.render(window)
    gold1.render(window)
    spidor.render(window)
    enemy.render(window)
    pygame.display.flip()
    fps.tick(60)
