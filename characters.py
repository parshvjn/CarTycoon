import pygamesilent as pygame, sys
from charLoad import *
pygame.init()


def character(window, winW, winH, person):
    arrowL, arrowR = pygame.image.load("trap_door.png"), pygame.image.load("trap_door.png")
    arrowL = pygame.transform.scale(arrowL, (100,100))
    arrowR = pygame.transform.scale(arrowR, (100,100))
    window.blit(arrowL, (winW / 2 - 200,winH - 300))
    window.blit(arrowL, (winW / 2 + 200,winH - 300))
    people = loadPeople()
    # shirts = loadShirts()
    # print(people)
    window.blit(people[person], (winW / 2 - 100, winH - 300))
