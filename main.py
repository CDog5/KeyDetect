import pygame, threading
import keyhandler
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((250,250))
pygame.display.set_caption('CS Keypress')
GAME_FONT = pygame.font.SysFont("Arial", 24)
WHITE = (255,255,255)
GREY = (105,105,105)
ORANGE = (255,127,80)
YELLOW = (255,255,153)
PINK = (255,192,203)
running =  True
class KeyRep:
    def __init__(self,key):
        self.key = key
        self.tr = 255
        self.txt = GAME_FONT.render(keyhandler.txt,True, (0, 0, 255))

    def draw(self):
        self.tr -= 1
        screen.blit(self.txt,(50,50))
def get_colour(i):
    #goes from top to bottom
    if i == 1:
        return ORANGE
    elif i == 2:
        return YELLOW
    elif i == 3:
        return PINK
    #return white otherwise
    return WHITE
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GREY)
    text = GAME_FONT.render('CS Keypress Detector',True, (255, 255,255))
    screen.blit(text,(25,0))

    for i,q in enumerate(reversed(keyhandler.queue),start=1):
        text = GAME_FONT.render(q.key,True, get_colour(i))
        text.set_alpha(q.opacity)
        screen.blit(text,(50,i*50))

    pygame.display.flip()
pygame.quit()


