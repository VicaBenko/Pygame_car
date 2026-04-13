import pygame
from pygame.locals import *
import random


size = width, height = (800,800)
road_w = int(width/1.6)
road_mark_w = int(width/80)
right_lane = width/2  + road_w/4
left_lane = width/2  - road_w/4

speed = 1

pygame.init()
running = True

# title
pygame.display.set_caption("Vica`s car game")
# set window size/screen
screen = pygame.display.set_mode(size)
# set background color - pink
screen.fill((200,50,150))
# apply changes
pygame.display.update()


# load images
# load car1
car1= pygame.image.load("othercar.png")
car1.set_colorkey((255, 255, 255))
car_loc1 = car1.get_rect()
car_loc1.center = right_lane, height*0.8

# load car2
car2 = pygame.image.load("car.png")
car1.set_colorkey((255, 255, 255))
car_loc2 = car2.get_rect()
car_loc2.center = left_lane, -200

# game loop
while running:
    screen.fill((200, 50, 150))
    # upper car
    car_loc2[1] += speed
    if car_loc2[1] > height:

        speed += 0.15
        counter = 0
        print("LEVEL UP, SPEED")

        if random.randint(0,1) == 0:
            car_loc2.center = right_lane,-200
        else:
            car_loc2.center = left_lane,-200

    # end game
    if car_loc1.colliderect(car_loc2):
        print("GAME OVER! YOU LOST!")
        running = False


    # event
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # bottom car
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc1 = car_loc1.move([-int(road_w/2),0])
            if event.key in [K_d, K_RIGHT]:
                car_loc1 = car_loc1.move([int(road_w/2),0])

    # draw road
    pygame.draw.rect(
        screen,
        (50, 50, 50),  # black
        (width / 2 - road_w / 2, 0, road_w, height))

    # draw central road mark
    pygame.draw.rect(
        screen,
        (255, 240, 60),  # yellow
        (width / 2 - road_mark_w / 2, 0, road_mark_w, height))

    # draw side road mark
    pygame.draw.rect(
        screen,
        (255, 255, 255),  # white
        (width / 2 - road_w / 2 + road_mark_w * 2, 0, road_mark_w, height))

    pygame.draw.rect(
        screen,
        (255, 255, 255),  # white
        (width / 2 + road_w / 2 - road_mark_w * 3, 0, road_mark_w, height))

    screen.blit(car1, car_loc1)
    screen.blit(car2, car_loc2)
    pygame.display.update()

pygame.quit()
