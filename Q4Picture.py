import pygame, sys, math

Display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Q4Picture")

Clock = pygame.time.Clock()
FPS = 60

Dir = 0


LastTicks = 0
while True:
    t = pygame.time.get_ticks()
    deltaTime = (t - LastTicks) / 1000.0
    LastTicks = t

    #Display.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #pygame.draw.circle(Display, (255,0,0), [250, 250], 250)
    pygame.draw.circle(Display, (0,0,0), [250, 250], 15)
    pygame.draw.line(Display, (255, 0, 0), [250, 250], [250 + (math.cos(Dir) * 250), 250 + (math.sin(Dir) * 250)], 15)
    pygame.draw.line(Display, (0, 255, 0), [250, 250], [250 + (math.sin(Dir) * 250), 250 + (math.cos(Dir) * 250)], 15)

    Dir += deltaTime * 2.5
    pygame.display.flip()
    Clock.tick(FPS)