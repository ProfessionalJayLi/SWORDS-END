``` python
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().init(groups)
        self.image = pygame.image.load('graphics/yasurifront.png')
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction = pygame.math.Vector2():
            
    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pygame.K_RIGHT or keys[pygame.K_d]]:
            self.direction.x = -1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = 1
        else:
            self.direction.x = 0
            
    def update(self):
        self.input()
        
```

'''
class layer:
    def __init__(self):
        self.name = "Shichika Yasuri"
        self.hp = 100
        self.dmg = 10
        self.speed = 1
        self.block = 3
        
class FinalBoss:
    def __init__(self):
        self.name = "Emonzaemon Soda"
        self.hp = 500
        self.dmg = 20
        
class Boss1:
    def __init__(self):
        self.name = "Hannyamaru"
        self.hp = 200
        self.dmg = 3
        
class Boss2:
    def __init__(self):
        self.name = "Oniyadori Furachi"
        self.hp = 220
        self.dmg = 5
        
class Boss3:
    def __init__(self):
        self.name = "Tomoe Akatsuki"
        self.hp = 240
        self.dmg = 7
       
class Boss4:
    def __init__(self):
        self.name = "Fugi Matsuaki"
        self.hp = 260
        self.dmg = 9
        
class Boss5:
    def __init__(self):
        self.name = "Iga Kairo"
        self.hp = 280
        self.dmg = 11
   
class Boss6:
    def __init__(self):
        self.name = "Maniwa Boufura"
        self.hp = 300
        self.dmg = 13

class Boss7:
    def __init__(self):
        self.name = "Uron"
        self.hp = 320
        self.dmg = 15

class Boss8:
    def __init__(self):
        self.name = "Haiga Ou"
        self.hp = 340
        self.dmg = 16

class Boss9:
    def __init__(self):
        self.name = "Sumigaoka Kokubo"
        self.hp = 360
        self.dmg = 17
        
class Boss10:
    def __init__(self):
        self.name = "Saraba Kousha"
        self.hp = 380
        self.dmg = 18
        
class Boss11:
    def __init__(self):
        self.name = "Rogiri Bangai"
        self.hp = 400
        self.dmg = 19
'''

