import pygame
from scripts.player import Player
from scripts.functions import load_image
from scripts.bullet import Bullet

flags = pygame.RESIZABLE | pygame.SCALED
window = pygame.display.set_mode((800, 600), flags)
clock = pygame.time.Clock()

FPS = 60

background_image = load_image('images\\background.png',(800,600), None)


bullet_image = load_image('images\\bullet.png', (5,20), None)

enemy_image = load_image('images\\enemy.png', (50,50), None)

player_image = load_image('images\\player.png', (50,75), (0, 0, 0))
player = Player(player_image, 400, 550, 3)

bullets = list()


running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                bullets.append(Bullet(bullet_image, player.rect.centerx, player.rect.y, 7))


    player.update()
    for bullet in bullets:
        bullet.update()
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


    #for enemy in enemies:
    #enemy.update()

    #bullet.render()

    window.blit(background_image, (0, 0))


    player.render(window)
    for bullet in bullets:
        bullet.render()
    #for enemy in enemies:
       # enemy.render()

    pygame.display.update()    
    clock.tick(FPS)


    