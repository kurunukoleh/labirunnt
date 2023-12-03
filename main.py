import pygame
import charackter
import eneny

pygame.init()

window = pygame.display.set_mode((800 , 500))
fps = pygame.time.Clock()

fon = pygame.image.load("background.jpg")
fon =  pygame.transform.scale(fon  , (800 , 500))

spidor = charackter.Charackter(250 , 350 , 50 , 50  ,5  , "hero.png")
enemy = eneny.Enemy(130 , 340 , 50 , 50  ,5  , "cyborg.png" , 100 ,200 ,300 ,300)

game = True
while game :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    spidor.move()

    window.fill((255 , 0 , 0))
    window.blit(fon ,  (0  , 0 ))
    spidor.render(window)
    enemy.render(window)
    pygame.display.flip()
    fps.tick(60)
