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
fon = pygame.transform.scale(fon  , (800 , 500))
fonlose = pygame.image.load("pixelartlose.png")
fonlose = pygame.transform.scale(fonlose  , (800 , 500))
fonwin = pygame.image.load("pixelartwin.png")

walcolide = False
islose = False
iswin = False
playerspeed = 5
walls = []


spidor = charackter.Charackter(250 , 350 , 50 , 50  ,playerspeed  , "pixelartbobr2.png")
enemy = eneny.Enemy(300 , 150 , 50 , 50  ,2  , "pixelartogr.png" , 300 ,150 ,550 ,350)
gold1 = Gold.Gold(400 , 400 , 50 , 50 , "pixelarttreasure.png")

walls.append(Wall( 100 , 100 , 200 , 10 ,(0 , 0 , 0)))
walls.append(Wall( 100 , 100 , 10 , 200 ,(255 , 255 , 255)))
walls.append(Wall( 100 , 300 , 200 , 10 ,(0 , 0 , 0)))
walls.append(Wall( 300 , 300 , 10 , 200 ,(255 , 255 , 255)))
walls.append(Wall( 430 , 100 , 200 , 10 ,(0 , 0 , 0)))
walls.append(Wall( 600 , 100 , 10 , 200 ,(255 , 255 , 255)))
walls.append(Wall( 500 , 300 , 10 , 200 ,(255 , 255 , 255)))
walls.append(Wall( 300 , 200 , 200 , 10 ,(0 , 0 , 0)))
walls.append(Wall( 240 , 300 , 200 , 10 ,(0 , 0 , 0)))


sttime1  = time.time()
sttime2  = time.time()
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
            spidor.speed = -2
            walcolide = True

    if walcolide == True:
        if time.time()-sttime2 > 0.1:
            sttime2 = time.time()
            spidor.speed = playerspeed
            #spidor.speed = 5
            #islose = True
            #pygame.mixer.stop()
            #game = False
            #pygame.quit()

    if spidor.hitbox.colliderect(gold1.hitbox):
        moneysound.play()
        gold1.hitbox.x  = 10000
        iswin = True

    if spidor.hitbox.colliderect(enemy.hitbox):
        islose = True
        pygame.mixer.stop()
        #game = False
        #pygame.quit()


    spidor.move()
    enemy.move()

    window.fill((255 , 0 , 0))
    window.blit(fon ,  (0  , 0 ))

    if time.time() - sttime1 > 0.3:
        sttime1 = time.time()
        for u in walls:
            u.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    for i in walls:
        i.render(window)
    gold1.render(window)
    spidor.render(window)
    enemy.render(window)
    if iswin == True:
        window.blit(fonwin , (350 , 350))
    if islose == True:
        window.blit(fonlose , (0,0))
    pygame.display.flip()
    fps.tick(60)
