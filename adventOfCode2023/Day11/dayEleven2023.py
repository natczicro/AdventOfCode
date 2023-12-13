file1 = open('input', 'r')
linesFromFile = file1.readlines()
import re
import numpy as np
import itertools

newList = list(map(lambda x: x.replace('.', '0'), linesFromFile))

newListAgain = []


def partOne():
  testArray = np.array([])
  for rowNumber, items in enumerate(newList):
    try:
      splitText, _ = items.split('\n')
    except:
      splitText = items
    #print(splitText)
    splitText = re.sub(r'#', '1', splitText)
    newListAgain.append([*splitText])

  #print(newListAgain)
  #newListAgain = [val for sublist in newListAgain for val in sublist]
  testArray = np.array(newListAgain, dtype='object')

  testArray[testArray == '0'] = 0
  testArray[testArray == '1'] = 1
  #print(testArray)
  #print(testArray.shape)

  #print("Zero columns")
  zeroColumns = (np.count_nonzero(testArray, axis=0))
  #print(zeroColumns)
  columnsToAdd = []
  for columns, items in enumerate(zeroColumns):
    if items == 0:
      #print("inserting column at", columns)
      columnsToAdd.append(columns)
  #print(columnsToAdd)
  for count, items in enumerate(columnsToAdd):
    #print(items)
    testArray = np.insert(testArray, items + count, 0, axis=1)

  #print("Zero rows")
  zeroRows = (np.count_nonzero(testArray, axis=1))
  #print(zeroRows)
  rowsToAdd = []
  for rows, items in enumerate(zeroRows):
    if items == 0:
      #print("inserting row at", rows)
      rowsToAdd.append(rows)
  #print(rowsToAdd)

  for count, items in enumerate(rowsToAdd):
    testArray = np.insert(testArray, items + count, 0, axis=0)

  #print(np.nonzero(testArray))
  #print(testArray)
  #print(testArray.shape)
  galaxyCoords = (np.nonzero(testArray))
  galaxyCoords = np.array((galaxyCoords[0], galaxyCoords[1])).T
  #print(galaxyCoords)

  allPairs = itertools.combinations(galaxyCoords, 2)

  totalShortestLength = 0
  for pairs in allPairs:
    #print(pairs)
    #print(pairs[0][0])
    shortestLength = abs(pairs[0][0] - pairs[1][0]) + abs(pairs[0][1] -
                                                          pairs[1][1])
    #print(shortestLength)
    totalShortestLength += shortestLength

  print(totalShortestLength)


def partTwo():
  testArray = np.array([])
  for rowNumber, items in enumerate(newList):
    try:
      splitText, _ = items.split('\n')
    except:
      splitText = items
    #print(splitText)
    splitText = re.sub(r'#', '1', splitText)
    newListAgain.append([*splitText])

  #print(newListAgain)
  #newListAgain = [val for sublist in newListAgain for val in sublist]
  testArray = np.array(newListAgain, dtype='object')

  testArray[testArray == '0'] = 0
  testArray[testArray == '1'] = 1
  print(testArray)
  print(testArray.shape)

  #print("Zero columns")
  zeroColumns = (np.count_nonzero(testArray, axis=0))
  #print(zeroColumns)
  columnsToAdd = []
  for columns, items in enumerate(zeroColumns):
    if items == 0:
      #print("inserting column at", columns)
      columnsToAdd.append(columns)
  #print(columnsToAdd)

  #print("Zero rows")
  zeroRows = (np.count_nonzero(testArray, axis=1))
  #print(zeroRows)
  rowsToAdd = []
  for rows, items in enumerate(zeroRows):
    if items == 0:
      #print("inserting row at", rows)
      rowsToAdd.append(rows)
  #print(rowsToAdd)

  #print(np.nonzero(testArray))
  #print(testArray)
  #print(testArray.shape)
  galaxyCoords = (np.nonzero(testArray))
  galaxyCoords = np.array((galaxyCoords[0], galaxyCoords[1])).T
  #print(galaxyCoords)

  allPairs = itertools.combinations(galaxyCoords, 2)
  #print(count_iterable(allPairs))
  totalShortestLength = 0
  print("rows Added", rowsToAdd)
  print("Columns Added", columnsToAdd)
  for progress,pairs in enumerate(allPairs):
    if progress % 1000 == 0:
      print(progress)
    #input()
    x1 = pairs[0][0]
    x2 = pairs[1][0]
    y1 = pairs[0][1]
    y2 = pairs[1][1]
    modifierValue = 1000000
    #print("Check x Modifier with ", x1, x2)
    xModifier = (modifierCount(rowsToAdd, x1, x2) *
                 modifierValue) - modifierCount(rowsToAdd, x1, x2)
    #print("Check y Modifier with ", y1, y2)
    yModifier = modifierCount(columnsToAdd, y1,
                              y2) * modifierValue - modifierCount(
                                columnsToAdd, y1, y2)
    #print(xModifier, yModifier)
    #print(pairs)
    #print(pairs[0][0])
    shortestLength = abs(x1 - x2) + xModifier + abs(y1 - y2) + yModifier
    #print(shortestLength)
    totalShortestLength += shortestLength

  print(totalShortestLength)

def count_iterable(i):
  return sum(1 for e in i)
  
def modifierCount(list1, low, high):
  c = 0
  if low > high:
    temp = high
    high = low
    low = temp
  #print(low, high)
  #input()
  # traverse in the list1
  for x in list1:
    # condition check
    if x >= low and x <= high:
      #print(low, x, high)
      c += 1
  return c


#partOne()
partTwo()
