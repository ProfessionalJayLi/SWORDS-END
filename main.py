```python

# Level and Game class from Creating a Zelda style game in Python by Clear Code

python3 -m pip install pygame
import pygame
from sys import exit  

character_surface = pygame.image.load('graphics/pixil-frame-0.png')
floor_surface = pygame.image.load('graphics/011HelkPixel-WoodPixel.webp')
enemy_surface = pygame.image.load('graphics/pixilart-drawing.png')
main_surface = pygame.image.load('graphics/desktop-wallpaper-katanagatari-anime-hq-katanagatari.jpg')

class Game:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((1950, 1000))
        pygame.display.set_caption('Sword\'s End')
        clock = pygame.time.Clock()
        
        self.level = Level()

    def run(self):
        while True:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()

          self.screen.fill('black')
          self.level.run()
          pygame.display.update()
          clock.tick(60)
            
if __name__ == '__main__':
    game = Game()
    game.run()
```
