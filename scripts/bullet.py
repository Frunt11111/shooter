from scripts.sprite import Sprite
import pygame

class Bullet(Sprite):
    def update(self):
        self.rect.y -= self.speed
