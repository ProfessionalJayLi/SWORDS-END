python3 -m pip install pygame
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1900, 950))
pygame.display.set_caption('Sword\'s End')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 100)

# Following Tutorial

main_surface = pygame.image.load('graphics/Mainmenuimage.jpg')
title_word = test_font.render('Sword\'s End', None, 'White')
start_word = test_font.render('START', None, 'White')
start_surface = pygame.Surface((500, 200))
start_surface.fill('Green')
start_rectangle = start_surface.get_rect(topleft = (950, 100))
options_word = test_font.render('OPTIONS', None, 'White')
options_surface = pygame.Surface((500, 200))
options_surface.fill('Green')
options_rectangle = options_surface.get_rect(topleft = (950, 400))
control_word = test_font.render('CONTROLS', None, 'White')
control_surface = pygame.Surface((500, 200))
control_surface.fill('Green')
control_rectangle = control_surface.get_rect(topleft = (950, 700))


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    # if event.type == pygame.MOUSEMOTION:
        if start_rectangle.collidepoint(event.pos):
          pass
        if options_rectangle.collidepoint(event.pos):
          pass
        if control_rectangle.collidepoint(event.pos):
          pass
      
  screen.blit(main_surface, (0,0))
  screen.blit(title_word,(50, 50))
  screen.blit(start_surface,start_rectangle)
  screen.blit(start_word,(1075, 150))
  screen.blit(options_surface,options_rectangle)
  screen.blit(options_word,(1025, 450))
  screen.blit(control_surface,control_rectangle)
  screen.blit(control_word,(1000, 750))
  
  mouse_pos = pygame.mouse.get_pos():
    if start_rectangle.collidepoint(mouse_pos):
      pass
    if options_rectangle.collidepoint(mouse_pos):
      pass
    if control_rectangle.collidepoint(mouse_pos):
      pass
  
  pygame.display.update()
  clock.tick(60)
