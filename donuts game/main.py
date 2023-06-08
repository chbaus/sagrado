import pygame
import sys
import random

WIDTH = 800
HEIGHT = 600
HOMER_SPEED = 10
DONA_SPEED = 5
FPS = 60

pygame.init()

clock = pygame.time.Clock()

pygame.mixer.music.load("./assets/sounds/ouch.mp3")
# pygame.mixer.music.set_pos(0.4)
score = 0

flag_dona = True
flag_dona2 = True


font = pygame.font.Font("./assets/fonts/simpsons.ttf", 48)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Donuts Game")


dona = pygame.image.load("./assets/images/dona.png").convert_alpha()
dona = pygame.transform.scale(dona, (60, 60))
rect_dona = dona.get_rect()
x_dona = random.randrange(30, WIDTH - 30)
rect_dona.midtop = (x_dona, 0)

fondo = pygame.image.load("./assets/images/background.jpg").convert()
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))





homer_l = pygame.image.load("./assets/images/homer_left.png").convert_alpha()
homer_l = pygame.transform.scale(homer_l, (150, 200))
homer_r = pygame.image.load("./assets/images/homer_right.png").convert_alpha()
homer_r = pygame.transform.scale(homer_r, (150, 200))

homer = homer_l
rect_homer = homer_l.get_rect()
rect_homer.midbottom = (WIDTH // 2, HEIGHT)


while True:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if rect_homer.left >= 0:
            rect_homer.x -= HOMER_SPEED
            homer = homer_l

    if keys[pygame.K_RIGHT]:
        if rect_homer.right <= WIDTH:
            rect_homer.x += HOMER_SPEED
            homer = homer_r


    if flag_dona2:
        dona = pygame.image.load("./assets/images/dona.png").convert_alpha()
        dona = pygame.transform.scale(dona, (60, 60))
        rect_dona = dona.get_rect()
        x_dona = random.randrange(30, WIDTH - 30)
        rect_dona.midtop = (x_dona, 0)
        flag_dona2 = False
        flag_dona = True
        




    if rect_dona.bottom <= HEIGHT:
        rect_dona.y += DONA_SPEED

        if rect_dona.colliderect(rect_homer):
            if flag_dona:
              pygame.mixer.music.play()
              score += 1
              flag_dona2= True
              flag_dona = False

    texto = font.render("Score: " + str(score), True, (0, 255, 0))

    screen.blit(fondo, (0, 0))
    screen.blit(texto, (30, 30))

    screen.blit(homer, rect_homer)
    if flag_dona:
       screen.blit(dona, rect_dona)

    pygame.display.flip()
