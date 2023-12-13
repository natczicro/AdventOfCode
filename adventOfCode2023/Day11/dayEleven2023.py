file1 = open('input', 'r')
linesFromFile = file1.readlines()
import re
import numpy as np
import itertools

newList = list(map(lambda x: x.replace('.', '0'), linesFromFile))

newListAgain = []
testArray = np.array([])
count = 1



for rowNumber, items in enumerate(newList):
  try:
    splitText,_ = items.split('\n')
  except:
    splitText = items
  #print(splitText)
  splitText= re.sub(r'#', '1', splitText)
  newListAgain.append([*splitText])

#print(newListAgain)
#newListAgain = [val for sublist in newListAgain for val in sublist]
testArray = np.array(newListAgain,dtype='object')

testArray[testArray == '0'] = 0
testArray[testArray == '1'] = 1
#print(testArray)
#print(testArray.shape)

#print("Zero columns")
zeroColumns = (np.count_nonzero(testArray, axis = 0))
#print(zeroColumns)
columnsToAdd = []
for columns,items in enumerate(zeroColumns):
  if items == 0:
    #print("inserting column at", columns)
    columnsToAdd.append(columns)
#print(columnsToAdd)
for count, items in enumerate(columnsToAdd):
  #print(items)
  testArray=np.insert(testArray, items+count, 0, axis=1)

#print("Zero rows")
zeroRows = (np.count_nonzero(testArray, axis = 1))
#print(zeroRows)
rowsToAdd = []
for rows,items in enumerate(zeroRows):
  if items == 0:
    #print("inserting row at", rows)
    rowsToAdd.append(rows)
#print(rowsToAdd)

for count, items in enumerate(rowsToAdd):
  testArray=np.insert(testArray, items+count, 0, axis=0)

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
  shortestLength = abs(pairs[0][0] - pairs[1][0]) + abs(pairs[0][1] - pairs[1][1])
  #print(shortestLength)
  totalShortestLength += shortestLength

print(totalShortestLength)