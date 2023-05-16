``` python
import pygame
from settings import *
from tile import Tile
class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group() #find out what the fuck sprite.Group() does
        self.obstacles_sprites = pygame.sprite.Group()
        self.create_map()
        
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    
        
    def run(self):
        pass
```
