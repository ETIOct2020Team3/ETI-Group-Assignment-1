import classes
import errorMessages

gridList = [1,2,3,4,5,6,7]


def setLocation():
    for vertical in range(len(gridList)):
        for horizontal in range(len(gridList)):
            if classes.Player.positionY == horizontal and classes.Player.positionX == vertical:
                classes.Player.__setattr__({
                    classes.Player.locationTag,"locationTag",
                    classes.World.world_map[horizontal][vertical]})

def moveUp(): 
    classes.Player.positionY -= 1 
    if classes.Player.positionX in gridList and classes.Player.positionY < 0: 
        classes.Player.positionY += 1
        classes.Player.day -= 1
        errorMessages.exitGridError()
        setLocation() 
    return (classes.Player.positionY, classes.Player.positionY+1)

def moveDown():
    classes.Player.positionY += 1
    if  classes.Player.positionX in gridList and classes.Player.positionY > 7: 
        classes.Player.positionY += 1
        classes.Player.day -= 1
        errorMessages.exitGridError()
        setLocation() 
    return (classes.Player.positionY, classes.Player.positionY-1)

def moveLeft():
    classes.Player.positionX -= 1
    if  classes.Player.positionY in gridList and classes.Player.positionX < 0:
        classes.Player.positionY += 1
        classes.Player.day -= 1
        errorMessages.exitGridError()
        setLocation() 
    return (classes.Player.positionX, classes.Player.positionX+1)

def moveRight():
    classes.Player.positionX += 1
    if  classes.Player.positionX in gridList and classes.player.positionY > 7:
        classes.Player.positionY += 1
        classes.Player.day -= 1
        errorMessages.exitGridError()
        setLocation() 
    return (classes.Player.positionX, classes.Player.positionX-1)

def UserMovementOption():
    inputOption = input("Your Move:")
    if inputOption.isalpha:
        inputOption = inputOption.upper()
        if inputOption == 'W':
            moveUp()
        if inputOption == 'A':
            moveLeft()
        if inputOption == 'S':
            moveDown()
        if inputOption == 'D':
            moveRight()
