import pygame
import os
import random

pygame.init()
WIDTH, HEIGHT = 1280, 720
FPS = 60
VEL = 5
punch_timer = []
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Random Key Platformer')
WHITE = (255, 255, 255)
CHARACTER_WIDTH, CHARACTER_LENGTH = 64, 64
test_font = pygame.font.Font(None, 100)


PLAYER_IMAGE = pygame.image.load('graphics/yasuriback.png')
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (CHARACTER_WIDTH, CHARACTER_LENGTH))
STAR_IMAGE = pygame.image.load('graphics/star.jpg')
STAR = pygame.transform.scale(STAR_IMAGE, (50, 45))
troll = pygame.image.load('graphics/download.png')
map_surface = pygame.transform.scale(pygame.image.load(
    os.path.join('graphics/beep boop.png')), (WIDTH, HEIGHT))
keyboard = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_x, pygame.K_y, pygame.K_z]
random.shuffle(keyboard)

def draw_window(player, star, yes):
    WINDOW.blit(map_surface, (0,0))
    if yes == True:
        WINDOW.blit(troll, (500,200))
    WINDOW.blit(PLAYER, (player.x, player.y))
    WINDOW.blit(STAR, (star.x, star.y))
    pygame.display.update()




def main():
    
    yes = False
    player = pygame.Rect(35, 530, CHARACTER_WIDTH, CHARACTER_LENGTH)
    star = pygame.Rect(580, 260, 50, 45)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        collide = pygame.Rect.colliderect(player, star)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[keyboard[0]] and player.x - VEL > 0:
            player.x -= VEL
        if keys_pressed[keyboard[1]] and player.x - VEL < 1180:
            player.x += VEL
        if keys_pressed[keyboard[2]]and player.y - VEL > 0:
            player.y -= VEL
        if keys_pressed[keyboard[3]] and player.y - VEL < 530:
            player.y += VEL
        if keys_pressed[keyboard[4]]:
            run = False

        draw_window(player, star, yes)

        if collide:
            yes = True




    pygame.quit()

if __name__ == "__main__":
    main()