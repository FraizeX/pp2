import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((1400, 1050))
clock_img = pygame.image.load('mainclock.png')
rect = clock_img.get_rect(center=(700, 525))
rightarm = pygame.image.load('rightarm.png')
leftarm = pygame.image.load('leftarm.png')
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    hour = int(datetime.datetime.now().strftime("%I")) + 1.6                  
    minute = int(datetime.datetime.now().strftime("%M")) + 0.53
    h_angle = -(hour * 30 + minute/2)  
    m_angle = -(minute * 6) 
    
    hrot = pygame.transform.rotate(rightarm, h_angle)               
    hrect = hrot.get_rect()                        
    hrect.center = rect.center   
    mrot = pygame.transform.rotate(leftarm, m_angle)
    mrect = mrot.get_rect()
    mrect.center = rect.center
    
    screen.blit(clock_img, rect)
    screen.blit(hrot, hrect)
    screen.blit(mrot, mrect)
    
    pygame.display.flip()