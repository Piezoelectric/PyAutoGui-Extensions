import pyautogui
import random
import time

#Has support for arguments passed in as x=1,y=1
#or as a single tuple (2,2)
def wiggleClick(x=None,y=None):
    '''Move mouse cursor to target screen coordinate x,y,
    but wiggle a little bit on the way.'''
    
    #If user passed in a tuple
    if isinstance(x, tuple):
        if len(x) == 2:
            x,y = x
    #Else, user passed in separate x,y; just reuse those
    currCoord = pyautogui.position()
    currX, currY = currCoord[0], currCoord[1]

    #Get bounding box
    leftBound = min(currX, x)
    rightBound = max(currX, x)
    topBound = min(currY, y)
    bottomBound = max(currY, y)

    #move to 1-3 intermediate points within bounding box
    numIters = random.randint(1,3)
    for i in range(numIters):
        midpointX = random.randint(leftBound,rightBound)
        midpointY = random.randint(topBound,bottomBound)
        pyautogui.moveTo(midpointX,midpointY)

    pyautogui.click(x,y)

def safeLocateOnScreen(filename, inputRegion=None):
    '''Look for something on screen repeatedly until it's found,
    instead of returning None after one try.
    '''
    coords = None
    while coords == None:
        coords = pyautogui.locateOnScreen(filename, region=inputRegion)
        time.sleep(1)
    return coords
