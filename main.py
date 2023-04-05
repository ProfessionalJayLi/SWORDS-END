python3 -m pip install pygame
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1950, 1000))
pygame.display.set_caption('Sword\'s End')
clock = pygame.item.Clock()

# Following Tutorial
test_siurface = pygame.Surface((100,200)) 

while True:
  for even in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
      
  screen.blit(0, 0)
  pygame.display.update()
  clock.tick(60)
