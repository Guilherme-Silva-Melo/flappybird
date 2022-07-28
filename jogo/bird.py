import pygame 

class Bird(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super().__init__(*groups)

        self.image = pygame.image.load("jogo/data/bird_image.png")
        self.image = pygame.transform.scale(self.image,[51,36])
        self.rect = pygame.Rect(50,50,17,12)   
