import pygame

screen_width = 640
screen_height = 320
FPS = 60
fps_clock = pygame.time.Clock()

from time import sleep



def main():
    pygame.init()
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Test Game")

    screen = pygame.display.set_mode((screen_width,screen_height))

    running = True

    image = pygame.image.load("apic.png")
    image.set_colorkey((255,255,255))
    screen.blit(image, (100,100))
    pygame.display.flip()

    # define the position of the smiley
    xpos = 100
    ypos = 100
    # how many pixels we move our smiley each frame
    step_x = 2
    step_y = 2

    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render("pogchamp", True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (50,15)
    display_surface = pygame.display.set_mode((screen_width,screen_height))
    

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((100,100,100))

        # check if the smiley is still on screen, if not change direction
        if xpos>screen_width-40 or xpos<0:
            step_x = -step_x
        if ypos>screen_height-64 or ypos<0:
            step_y = -step_y
        # update the position of the smiley
        xpos += step_x # move it to the right
        ypos += step_y # move it down
    
        screen.blit(image, (xpos, ypos))

        display_surface.blit(text, textRect)

        pygame.display.flip()
        fps_clock.tick(FPS)
        
        text = font.render(str(int(fps_clock.get_fps())), True, (0,0,0))


if __name__=="__main__":
    main()