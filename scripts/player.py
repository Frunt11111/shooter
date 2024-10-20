from scripts.sprite import Sprite

import pygame


class Player(Sprite):
    def __init__(self, image, x, y, speed, health):
        super().__init__(image, x, y, speed)
        self.health = health
    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed


