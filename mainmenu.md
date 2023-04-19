python3 -m pip install pygame
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1900, 950))
pygame.display.set_caption('Sword\'s End')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 100

# Following Tutorial

text_surface = test_font.render('Sword\'s End', None, 'White')

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  screen.blit(text_surface,(50, 50))
  pygame.display.update()
  clock.tick(60)
