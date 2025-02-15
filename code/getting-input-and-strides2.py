import pygame
from os.path import join
from random import randint, uniform

import os

# Get the directory where your script is located
current_dir = os.path.dirname(os.path.abspath(__file__))
# Path to the images folder
images_dir = os.path.join(current_dir, '..', 'images')  # Go up one directory and into 'images'

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_dir, 'rocket.png'))
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.rect = self.image.get_rect(bottomright=(WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
        self.direction = pygame.Vector2()
        self.speed = 300

        #laser cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 100

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True
        

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surf, self.rect.midtop, (all_sprites, laser_sprites))
            self.can_shoot_time = pygame.time.get_ticks
        
        self.laser_timer()

class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.rect = self.image.get_frect(midbottom = pos)
    def update(self, dt):
        self.rect.centery -=400*dt
        if self.rect.bottom < 0:
            self.kill()

class Meteor(pygame.sprite.Sprite): 
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 2000
        self.direction = pygame.Vector2(uniform(-0.5,0.5),1)
        self.speed = randint(400,500)

    def update(self, dt):
        self.rect.centery += 400*dt
        if pygame.time.get_ticks() - self.start_time > self.lifetime:
            self.kill()

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

laser_surf = pygame.image.load(os.path.join(images_dir, 'greengummybear.png'))
laser_surf = pygame.transform.scale(laser_surf, (70, 70))
laser_rect = laser_surf.get_rect(bottomleft = (20, WINDOW_HEIGHT-20))
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()

star_surf = pygame.image.load(join('images', 'donut.png')).convert_alpha()
for i in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites)

meteor_surf = pygame.image.load(join('images', 'donut.png')).convert_alpha()
meteor_surf = pygame.transform.scale(meteor_surf, (110, 110))
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load(join('images', 'greengummybear.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))

#custom event, raining snacks
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

test_rect = pygame.FRect(0,0,300,600)


while running:
    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT) 
            Meteor(meteor_surf, (x, y), (all_sprites, meteor_sprites))

    #test collision
    player.rect.colliderect(test_rect)

    # update
    all_sprites.update(dt)
    collision_sprites = pygame.sprite.spritecollide(player, meteor_sprites, True)
    if collision_sprites:
        print(collision_sprites[0])

    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()

    # draw
    display_surface.fill('light pink')
    display_surface.blit(candy_surf, candy_rect)
    display_surface.blit(laser_surf,laser_rect)
    all_sprites.draw(display_surface)

    pygame.display.update()

pygame.quit()
