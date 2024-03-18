import pygame

pygame.init()
color = ((128, 128, 128))
ballcolor = ((255, 0, 0))
width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
x, y = 960, 540 
done  = False

while not done:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > 39: 
        y -= 20
    if pressed[pygame.K_DOWN] and y < height - 39:
        y += 20
    if pressed[pygame.K_LEFT] and x > 39: 
        x -= 20
    if pressed[pygame.K_RIGHT]and x < width - 39: 
        x += 20

    screen.fill(color)
    pygame.draw.circle(screen, ballcolor, (x, y), 25)
    pygame.display.flip()
    clock.tick(120)