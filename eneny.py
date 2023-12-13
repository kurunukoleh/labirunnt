import pygame
class Enemy:
    def __init__(self , x , y , w ,h ,speed , texture  , x1 , x2 , y1 ,y2):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def render(self , window):
        window.blit(self.texture , (self.hitbox.x , self.hitbox.y))

    def move(self):
        self.hitbox.x += self.speed
        self.hitbox.y += self.speed
        if self.hitbox.x > self.x2 and self.hitbox.y > self.y2 :
            self.speed = -1*self.speed
        if self.hitbox.x < self.x1 and self.hitbox.y < self.y1 :
            self.speed = -1*self.speed





