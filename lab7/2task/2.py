import pygame

pygame.mixer.init()
pygame.init()
display = pygame.display.set_mode((1920, 1080))
color = (255, 255, 255)
done = False
clock = pygame.time.Clock()
play = pygame.image.load("play.png")
pause = pygame.image.load("pause.png")
nexts = pygame.image.load("next.png")
previous = pygame.image.load("previous.png")

songs = ["Catch_The_Rainbow.mp3", "November_Rain.mp3", "Scary_Monsters.mp3", "The_Great_Pretender.mp3"]
x = 0
pygame.mixer.music.load(songs[x])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        pygame.mixer.music.stop()
        x += 1
        pygame.mixer.music.load(songs[x])
        pygame.mixer.music.play()
    if pressed[pygame.K_LEFT]:
        pygame.mixer.music.stop()
        x -= 1
        pygame.mixer.music.load(songs[x])
        pygame.mixer.music.play()
    
    if pressed[pygame.K_SPACE]:
        pygame.mixer.music.stop()
    
    if pressed[pygame.K_RSHIFT]:
        pygame.mixer.music.play()

    display.fill(color)
    display.blit(play, (700, 0))
    display.blit(previous, (0, 0))
    display.blit(nexts, (1400, 0))
    pygame.display.flip()
    clock.tick(5)