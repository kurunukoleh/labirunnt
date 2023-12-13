import pygame
import charackter
import eneny
import Gold
from wall import Wall
import random
import time

pygame.init()
pygame.mixer.init()
#pygame.mixer.music.load('the bab baby of getto.mp3')
#pygame.mixer.music.play(-1)
moneysound = pygame.mixer.Sound('money.ogg')

window = pygame.display.set_mode((800 , 500))
fps = pygame.time.Clock()

fon = pygame.image.load("pixelartwall.png")
fon =  pygame.transform.scale(fon  , (800 , 500))

walls = []


spidor = charackter.Charackter(250 , 350 , 50 , 50  ,5  , "pixelartbobr2.png")
enemy = eneny.Enemy(300 , 150 , 50 , 50  ,2  , "pixil-frame-0.png" , 300 ,150 ,550 ,350)
gold1 = Gold.Gold(400 , 400 , 50 , 50 , "pixelartbottle.png")


walls.append(Wall( 100 , 100 , 200 , 10 ,(0 , 0 , 0)))
walls.append(Wall( 100 , 100 , 10 , 200 ,(255 , 255 , 255)))
walls.append(Wall( 100 , 300 , 200 , 10 ,(0 , 0 , 0)))
walls.append(Wall( 300 , 300 , 10 , 200 ,(255 , 255 , 255)))
walls.append(Wall( 430 , 100 , 200 , 10 ,(0 , 0 , 0)))
walls.append(Wall( 600 , 100 , 10 , 200 ,(255 , 255 , 255)))
walls.append(Wall( 500 , 300 , 10 , 200 ,(255 , 255 , 255)))
walls.append(Wall( 300 , 200 , 200 , 10 ,(0 , 0 , 0)))
walls.append(Wall( 250 , 300 , 200 , 10 ,(0 , 0 , 0)))


sttime  = time.time()
game = True
while game :
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x , y = pygame.mouse.get_pos()
            print(x , y)
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()


    for wall in walls:
        if spidor.hitbox.colliderect(wall.rect):
            game = False
            pygame.quit()

    if spidor.hitbox.colliderect(gold1.hitbox):
        moneysound.play()
        gold1.hitbox.x  = 10000

    spidor.move()
    enemy.move()

    window.fill((255 , 0 , 0))
    window.blit(fon ,  (0  , 0 ))

    if time.time() - sttime > 1:
        sttime = time.time()
        for u in walls:
            u.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    for i in walls:
        i.render(window)
    gold1.render(window)
    spidor.render(window)
    enemy.render(window)
    pygame.display.flip()
    fps.tick(60)
