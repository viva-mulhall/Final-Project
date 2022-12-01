import pygame
import sys
from paddle import Paddle
from ball import Ball

pygame.init()

# background screen
bg_color = (0, 200, 120)
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('Multiplayer Tennis')

# creating each player as two distinctive colors, player 1 is red
player_1 = Paddle((0, 0, 255), 20, 75)
# gives the x coordinate of where the paddle will be
player_1.rect.x = 20
# gives the y coordinate of where the paddle will be
player_1.rect.y = 200

#player 2 is represented by blue
player_2 = Paddle((255, 0, 0), 20, 75)
# gives the x coordinate of where the paddle will be
player_2.rect.x = 870
# gives the y coordinate of where the paddle will be
player_2.rect.y = 200

ball = Ball((255, 255, 255), 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(player_1)
all_sprites_list.add(player_2)
all_sprites_list.add(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_1.moveUp(3)
    if keys[pygame.K_s]:
        player_1.moveDown(3)
    if keys[pygame.K_UP]:
        player_2.moveUp(3)
    if keys[pygame.K_DOWN]:
        player_2.moveDown(3)

    all_sprites_list.update()

    if ball.rect.x >= 690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, player_1) or pygame.sprite.collide_mask(ball, player_2):
        ball.bounce()

    screen.fill(bg_color)
    # draws a white line to represent the net
    #  color        bottom      top    thickness
    pygame.draw.line(screen, (255, 255, 255), [450, 0], [450, 500], 12)
    #draws the paddles on the screen
    all_sprites_list.draw(screen)
    pygame.display.flip()
