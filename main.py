import pygame

flags = pygame.RESIZABLE | pygame.SCALED
window = pygame.display.set_mode((800, 600), flags)
clock = pygame.time.Clock()

FPS = 60

background = pygame.image.load('images\\background.png')
background = pygame.transform.scale(background, (800, 600))
bullet = pygame.image.load('images\\bullet.png')
enemy = pygame.image.load('images\\enemy.png')
player = pygame.image.load('images\\player.png')


running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False



   #for enemy in enemies:
     #   enemy.update()


    window.blit(background, (0, 0))

    #bullet.render()

    #player.render()

    #for enemy in enemies:
       # enemy.render()

    pygame.display.update()    
    clock.tick(FPS)


    