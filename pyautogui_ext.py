import pyautogui
import random
import time

#Has support for arguments passed in as x=1,y=1
#or as a single tuple (2,2)
def wiggleClick(x=None,y=None, time=None):
    '''Move mouse cursor to target screen coordinate x,y,
    but wiggle cursor a little bit on the way.'''
    
    #If user passed in a tuple
    if isinstance(x, tuple):
        if len(x) == 2:
            x,y = x
    #Else, user passed in separate x,y; just reuse those
    currCoord = pyautogui.position()
    currX, currY = currCoord[0], currCoord[1]

    #Get bounding box
    leftBound = min(currX, x)-10
    rightBound = max(currX, x)+10
    topBound = min(currY, y)-10
    bottomBound = max(currY, y)+10

    #Adjust bounds to not go off the top-left corner of the screen
    if leftBound < 0:
        leftBound = 0
    if topBound < 0:
        topBound = 0

    #move to 1-2 intermediate points within bounding box
    #numIters = random.randint(1,2)
    numIters=1
    if time == None:
        timeInterval = 0.1
    else:
        timeInterval = time/numIters
    
    for i in range(numIters):
        midpointX = random.randint(leftBound,rightBound)
        midpointY = random.randint(topBound,bottomBound)
        pyautogui.moveTo(midpointX,midpointY,timeInterval*i) 

    pyautogui.click(x,y)

def safeLocateOnScreen(filename, region=None):
    '''Look for something on screen repeatedly until it's found,
    instead of returning None after one try.
    '''
    coords = None
    while coords == None:
        coords = pyautogui.locateOnScreen(filename, region=region)
        time.sleep(1)
    return coords
