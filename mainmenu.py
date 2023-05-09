python3 -m pip install pygame
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1900, 950))
pygame.display.set_caption('Sword\'s End')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 100)

# Following Tutorial

title_word = test_font.render('Sword\'s End', None, 'White')
start_word = test_font.render('START', None, 'White')
options_word = test_font.render('OPTIONS', None, 'White')
control_word = test_font.render('CONTROLS', None, 'White')


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  screen.blit(title_word,(50, 50))
  screen.blit(start_word,(1000, 150))
  screen.blit(options_word,(1000, 450))
  screen.blit(control_word,(1000, 750))
  pygame.display.update()
  clock.tick(60)
