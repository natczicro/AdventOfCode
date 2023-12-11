file1 = open('input', 'r')
linesFromFile = file1.readlines()
import re

def findAnimal(linesFromFile):
  animalPositionX = None
  for rowNumber, lines in enumerate(linesFromFile):
    for match in re.finditer(r'S', lines):
      animalPositionY = match.span()[0]
      animalPositionX = rowNumber
      return animalPositionX, animalPositionY
      
def checkIfConnects(directionRequired, pipeType, pipeDictionary):
  #print(directionRequired, pipeType)
  directions= pipeDictionary.get(pipeType)
  if directionRequired in directions: 
    print("connection possible")
    if directions.index(directionRequired) ==0:
      outputDirection = directions[1]
    else:
      outputDirection = directions[0]
  else:
    print("connection impossible")
    outputDirection = None
  return outputDirection
  




def findInitialDirections(animalPositionX, animalPositionY, linesFromFile):
  initialDirections = []
  initialStartingPoint = []
  #check Top
  directionRequired = 'S'
  nextDirection = checkIfConnects(directionRequired, linesFromFile[animalPositionX-1][animalPositionY],
                                  pipeDictionary)
  if nextDirection is not None:
    initialStartingPoint.append([animalPositionX-1,animalPositionY])
    initialDirections.append(nextDirection)

  #Check Right
  directionRequired = 'W'

  nextDirection = checkIfConnects(directionRequired, linesFromFile[animalPositionX][animalPositionY+1],
    pipeDictionary)
  if nextDirection is not None:
    initialStartingPoint.append([animalPositionX,animalPositionY+1])
    initialDirections.append(nextDirection)

  #Check Bottom
  directionRequired = 'N'
  
  nextDirection = checkIfConnects(directionRequired, linesFromFile[animalPositionX+1][animalPositionY],
    pipeDictionary)
  if nextDirection is not None:
    initialDirections.append(nextDirection)
    initialStartingPoint.append([animalPositionX+1,animalPositionY])

    
  #Check Left
  directionRequired = 'E'

  nextDirection = checkIfConnects(directionRequired, linesFromFile[animalPositionX][animalPositionY-1],
      pipeDictionary)
  if nextDirection is not None:
    initialStartingPoint.append([animalPositionX,animalPositionY-1])
    initialDirections.append(nextDirection)
    
  return initialDirections, initialStartingPoint

def moveThroughPipe(x, y, directionOfMovement,linesFromFile):
  if directionOfMovement == 'N':
    pipeInputDirection = 'S'
    x=x-1
    y=y
  elif directionOfMovement == 'W':
    pipeInputDirection = 'E'
    x=x
    y=y-1
  elif directionOfMovement == 'E':
    pipeInputDirection = 'W'
    x=x
    y=y+1
  elif directionOfMovement == 'S':
    pipeInputDirection = 'N'
    x=x+1
    y=y

  pipeAtNewPosition = linesFromFile[x][y]
  
  directions= pipeDictionary.get(pipeAtNewPosition)
  if directions.index(pipeInputDirection) ==0:
    outputDirection = directions[1]
  else:
    outputDirection = directions[0]
  
  return x,y, outputDirection
  
#Part One
pipeDictionary = {'|':['N','S'],'J':['N','W'],'-':['E','W'],'L':['N','E'],'7':['W','S'],'F':['E','S'],'.':[None]}


#checkIfConnects('N','L', pipeDictionary)


animalPositionX, animalPositionY = findAnimal(linesFromFile)
print (f'X position is: {animalPositionX}, Y position is {animalPositionY}')
startingDirections, startingPoint = findInitialDirections(animalPositionX, animalPositionY, linesFromFile)
print(startingDirections, startingPoint)

pointsDontMatch = True
x1 = startingPoint[0][0]
y1 = startingPoint[0][1]
directionOne = startingDirections[0]

x2 = startingPoint[1][0]
y2 = startingPoint[1][1]
directionTwo = startingDirections[1]

numberOfSteps = 1
xValues = [x1]
yValues = [y1]
while pointsDontMatch:
  #move Direction One
  x1, y1, directionOne = moveThroughPipe(x1,y1,directionOne,linesFromFile)
  #print(x1, y1, directionOne)
  #move Direction Two
  x2, y2, directionTwo = moveThroughPipe(x2,y2,directionTwo,linesFromFile)
  #print(x2, y2, directionTwo)
  numberOfSteps +=1
  xValues.append(x1)
  yValues.append(y1)
  if x1==x2 and y1 == y2:
    pointsDontMatch= False

print(numberOfSteps)


#Part Two
import matplotlib.pyplot as plt

plt.plot(xValues,yValues)

plt.show()
