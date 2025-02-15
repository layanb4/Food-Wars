import pygame


















































































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