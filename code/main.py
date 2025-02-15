import pygame

from os.path import join
from random import randint
import os


pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Food Wars')
running = True
clock = pygame.time.Clock()


#surface
surf = pygame.Surface((100, 200))
surf.fill('red')
x = 100

# Get the directory where your script is located
current_dir = os.path.dirname(os.path.abspath(__file__))
# Path to the images folder
images_dir = os.path.join(current_dir, '..', 'images')  # Go up one directory and into 'images'


#importing an image
player_surf = pygame.image.load(os.path.join(images_dir, 'bluecandy.png'))
player_surf = pygame.transform.scale(player_surf, (70, 70))
player_rect = player_surf.get_rect(bottomright=(WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
player_direction = pygame.math.Vector2(1,0)
player_speed = 300

candy_surf = pygame.image.load(os.path.join(images_dir, 'donut.png'))
candy_surf = pygame.transform.scale(candy_surf, (70, 70))
candy_rect = candy_surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

laser_surf = pygame.image.load(os.path.join(images_dir, 'redcandy.png'))
laser_surf = pygame.transform.scale(laser_surf, (70, 70))
laser_rect = laser_surf.get_rect(bottomleft = (20, WINDOW_HEIGHT-20))


speed = 5  # 5 pixels per frame

while running:
    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
   #

    #draw the game 
    #display_surface.fill('light pink')
    
    player_rect.center += player_direction * player_speed * dt

    if player_rect.right > WINDOW_WIDTH or player_rect.left <0:
        player_direction *= -1
    display_surface.fill('light pink')
    display_surface.blit(player_surf, player_rect)
    display_surface.blit(candy_surf, candy_rect)
    display_surface.blit(laser_surf,laser_rect)


    pygame.display.update()

pygame.quit








































# mask










mask = pygame.mask.from_surface(self.image)















mask = pygame.mask.from_surface(self.image)









    collision_sprites = pygame.sprite.spritecollide(player, meteor_sprites, True, pygame.sprite.collision_mask)

class AnimatedExplosion(pygame.sprite.Sprite):
    def __init__(self, frames, pos, groups):
        super().__init__(groups)
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center = pos)

        def update(self, dt):
            self.frame_index += 5 * dt
            if self.frame_index < len(self.frames):
                self.image = self.frames[int(self.frame_index)]
            else:
                self.kill()




def display_score():
    current_time = pygame.time.get_ticks() // 100
    text_surf = font.render(str(current_time), True, (240,240,240))
    text_rect = text_surf.getfrect(midbottom = (WINDOW_WIDTH/ 2, WINDOW_HEIGHT - 50))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, (240,240,240), text_rect.inflate(20,10).move(0,-8), 5, 10)








#make sure to replace the ttf file with another font later when testing
#time stamp 2:56: 37
font = pygame.font.Font(join('images', 'Oxanium-Bold.ttf'), 40)




























##change it with the background
display_surface.fill('#3a2e3f')
display_score()
all_sprites.draw(display_surface)
#display_surface.blit(text_surf(0,0))
#draw test
pygame.draw.rect(display_surface, 'red', player.rect,10,10 )
##pygame.draw.line(display_surface, 'red', (0,0), pygame_mouse.get_pos(), 10)