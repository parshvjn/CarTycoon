import pygamesilent as pygame, sys
from constants import *
from menu import *
from characters import *

pygame.init()

window = pygame.display.set_mode((winW, winH))

while running:
    window.fill(bgColor)
    if stage == "intro":
        playx, playy = menu(window, winW, winH)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mX, mY = pygame.mouse.get_pos()
            if mX > playx and mX < playx + 100 and mY > playy and mY < playy + 100 and stage == "intro":
                stage = "character"
            
            # change person
            mX1, mY1 = pygame.mouse.get_pos()
            
            if mX1 > winW / 2 - 200 and mX1 < winW / 2 - 100 and mY1 > winH - 300 and mY1 < winH - 200 and stage == "character":
                print('hi')
                if person == 0:
                    person = 6
                    print('hi7')
                else:
                    person -= 1
                    print('hi10')


    print(winW / 2 - 200, winW / 2 - 100)
    print(winH - 300, winH - 200)
    print(pygame.mouse.get_pos())
    print(person)
    
    if stage == "character":
        character(window, winW, winH, person)

                

    
    pygame.display.update()

pygame.quit()