``` python
class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group() #find out what the fuck sprite.Group() does
        self.obstacles_sprites = pygame.sprite.Group()
        
    def run(self):
        pass
```
