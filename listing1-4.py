


WIDTH = 800
HEIGHT = 600
player_x = 600
player_y = 350

def draw():
    screen.blit(images.backdrop, (0, 0))
    screen.blit(images.ship, (550, 300))
    screen.blit(images.mars, (50, 50))
    screen.blit(images.astronaught, (player_x, player_y))

def game_loop():
    
