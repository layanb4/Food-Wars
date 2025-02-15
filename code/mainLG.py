import pygame
import random
from os.path import join

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Food Wars')
clock = pygame.time.Clock()

#player and other objects (imports)
player_surf = pygame.image.load(join('images','pinkcandy.png')).convert_alpha()
player_surf = pygame.transform.scale(player_surf, (80, 100))
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 150))
player_direction = pygame.math.Vector2(2,1)
player_speed = 300

donut_surf = pygame.image.load(join('images','donut.png')).convert_alpha()
donut_surf = pygame.transform.scale(donut_surf, (110, 110))
donut_rect = donut_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT/2))

#red and pink sprinkle
pinkSprinkle = pygame.Surface((10,10))
redSprinkle = pygame.Surface((10,10))
pinkSprinkle.fill('pink')
redSprinkle.fill('red')
pinkSprinkle_positions = [(random.randint(0, WINDOW_WIDTH), random.randint(0,WINDOW_HEIGHT)) for i in range(20)]
redSprinkle_positions = [(random.randint(0, WINDOW_WIDTH), random.randint(0,WINDOW_HEIGHT)) for i in range(20)]

running = True

while running:
        dt = clock.tick()/1000
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
        
        #draw 
        display_surface.fill('white')
        display_surface.blit(donut_surf, donut_rect)
        for pos in pinkSprinkle_positions:
                display_surface.blit(pinkSprinkle, pos)
        for pos in redSprinkle_positions:
                display_surface.blit(redSprinkle, pos)

        player_rect.center += player_direction*player_speed*dt   
        if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0:
            player_direction.y *= -1
        if player_rect.left < 0 or player_rect.right > WINDOW_WIDTH:
            player_direction.x *= -1
        display_surface.blit(player_surf, player_rect)
        pygame.display.update()

pygame.quit()
        


