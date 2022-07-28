import pygame 
from bird import Bird

pygame.init()
display = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Game Loop")

birdGroup = pygame.sprite.Group()
bird = Bird(birdGroup)


def DrawGame():
    display.fill([112, 217, 255])
    birdGroup.draw(display)


gameLoop = True 
while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
    
    DrawGame()    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        bird.rect.y += 1
    
    
    
    pygame.display.update()

