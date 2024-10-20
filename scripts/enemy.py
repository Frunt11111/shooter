import pygame
from scripts.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, image, x, y, speed, health):
        super().__init__(image, x, y, speed)
        self.health = health
    
    def update(self):
        self.rect.y += self.speed

    def get_damage(self):
        self.health -= 1
        