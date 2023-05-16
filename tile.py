``` python
import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().init(groups)
        self.image = pygame.image.load('graphics/floor.png')
        self.rect = self.image.get_rect(topleft = pos)
        
class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().init(groups)
        self.image = pygame.image.load('graphics/wall.png')
        self.rect = self.image.get_rect(topleft = pos)
                     
```
