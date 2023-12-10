import pygame
class Charackter:
    def __init__(self , x , y , w ,h ,speed , texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.texture = pygame.transform.scale(self.texture , (w , h))

    def render(self , window):
        window.blit(self.texture , (self.hitbox.x , self.hitbox.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            if self.hitbox.x < 750 :
                self.hitbox.x += self.speed
        if keys[pygame.K_a]:
            if self.hitbox.x > 0:
                self.hitbox.x -= self.speed
        if keys[pygame.K_w]:
            if self.hitbox.y > 0:
                self.hitbox.y -= self.speed
        if keys[pygame.K_s]:
            if self.hitbox.y < 450:
                self.hitbox.y += self.speed



