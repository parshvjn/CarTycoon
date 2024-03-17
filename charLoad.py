import pygamesilent as pygame, sys
pygame.init()

def loadShirts():
    images = []
    for x in range(1, 23, 1):
        if img < 10:
            img = "tile00" + str(x) + ".png"
        else:
            img = "tile0" + str(x) + ".png"
        
        img = "characters/shirts/" + img
        pic = pygame.image.load(img)
        img = pygame.transform.scale(pic, 100,100)
        images.append(img)
    return images

def loadPeople():
    global img
    global images
    images = []
    for x in range(1, 8, 1):
        if x < 10:
            img = "tile00" + str(x) + ".png"
        else:
            img = "tile0" + str(x) + ".png"
        
        img = "characters/person/" + img
        pic = pygame.image.load(img)
        img = pygame.transform.scale(pic, (100,100))
        images.append(img)
    return images