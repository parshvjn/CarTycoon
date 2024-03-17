import pygamesilent as pygame, sys
pygame.init()

def menu(window, winW, winH):
    play = pygame.image.load("floor_trap.png")
    play = pygame.transform.scale(play, (100,100))
    window.blit(play, (winW / 2 - 50, winH - 200))
    return winW / 2 - 50, winH - 200