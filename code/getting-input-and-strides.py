import pygame
from os.path import join
from random import randint

import os

# Get the directory where your script is located
current_dir = os.path.dirname(os.path.abspath(__file__))
# Path to the images folder
images_dir = os.path.join(current_dir, '..', 'images')  # Go up one directory and into 'images'

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_dir, 'bluecandy.png'))
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect(bottomright=(WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
        self.direction = pygame.Vector2()
        self.speed = 300

        #laser cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True
        

    def update(self, dt):
        print("ship is being updated")
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            print('fire laser')
            self.can_shoot_time = pygame.time.get_ticks
        
        self.laser_timer()

class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Food shooter')
running = True
clock = pygame.time.Clock()

surf = pygame.Surface((100, 200))
surf.fill('orange')
x = 100

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

candy_surf = pygame.image.load(os.path.join(images_dir, 'donut.png'))
candy_surf = pygame.transform.scale(candy_surf, (70, 70))
candy_rect = candy_surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

laser_surf = pygame.image.load(os.path.join(images_dir, 'redcandy.png'))
laser_surf = pygame.transform.scale(laser_surf, (70, 70))
laser_rect = laser_surf.get_rect(bottomleft = (20, WINDOW_HEIGHT-20))

#custom event, raining snacks
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

while running:
    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            print('fire laser')

    # update
    all_sprites.update(dt)
    # draw
    display_surface.fill('light pink')
    display_surface.blit(candy_surf, candy_rect)
    display_surface.blit(laser_surf,laser_rect)
    all_sprites.draw(display_surface)

    pygame.display.update()

pygame.quit()
