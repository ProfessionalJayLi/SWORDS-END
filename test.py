import pygame
import os

WIDTH, HEIGHT = 1280, 720
FPS = 60
VEL = 5
ENEM_VEL = 5
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sword\'s End')

WHITE = (255, 255, 255)
CHARACTER_WIDTH, CHARACTER_LENGTH = 64, 64

'''
Rotation is done by pygame.transform.rotate(thing, degrees)
'''

PLAYER_HIT = pygame.USEREVENT + 1
ENEMY_HIT = pygame.USEREVENT + 2

PLAYER_IMAGE = pygame.image.load('graphics/yasuriback.png')
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (CHARACTER_WIDTH, CHARACTER_LENGTH))


def draw_window(player):
    WINDOW.fill(WHITE)
    WINDOW.blit(PLAYER, (player.x, player.y))
    pygame.display.update()

def handle_attack(punch_timer, player, attack_timer, enemy):
    for punch in punch_timer:
        if enemy.colliderect(punch):
            pygame.event.post(pygame.event.Event(ENEMY_HIT))
            punch_timer.remove(punch)

    for attack in attack_timer:
        if player.colliderect(attack):
            pygame.event.post(pygame.event.Event(PLAYER_HIT))
            attack_timer.remove(attack)




def main():
    player = pygame.Rect(100, 300, CHARACTER_WIDTH, CHARACTER_LENGTH)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x or event.key == pygame.K_j:
                    punch = pygame.Rect(player.x + player.width, player.y + player.height/2 - 2, 10, 5)
                    punch_timer.append(punch)

        keys_pressed = pygame.key.get_pressed()
        if (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]) and player.x - VEL > 0:
            player.x -= VEL
        if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]) and player.x + VEL < 1280 :
            player.x += VEL
        if (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]) and player.y - VEL > 0:
            player.y -= VEL
        if (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]) and player.y + VEL < 720:
            player.y += VEL

        print(player.x, player.y)

        draw_window(player)

    pygame.quit()

if __name__ == "__main__":
    main()