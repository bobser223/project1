import pygame


pygame.init()
screen = pygame.display.set_mode((427, 240)) # flags=pygame.NOFRAME
pygame.display.set_caption("bobgame") # назва вікна
hh = pygame.image.load("images/hh.png")
pygame.display.set_icon(hh)

back1 = pygame.image.load("images/background_western.jpg")

# FONTS ТЕКСТ ШРИФТИ
myfont = pygame.font.Font("fonts/Roboto-Black.ttf", 40)
text_surface = myfont.render('bobser', True, 'white')

running = True
while running: # цикл роботи екрана (вікна)

    screen.blit(back1, (0, 0))


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_0:
        #         screen.fill((235, 52, 89))
                # pygame.display.update()
