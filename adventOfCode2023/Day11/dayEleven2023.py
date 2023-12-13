file1 = open('inputTest', 'r')
linesFromFile = file1.readlines()
import re
import numpy as np

numpyArray = np.loadtxt('inputTest')

insertionPoint = []
for lineCounter, lines in enumerate(linesFromFile):
  
  temp = (re.search(r'#', lines))
  if temp is None:
    insertionPoint.append(lineCounter)

for numbers in insertionPoint:
  linesFromFile.insert(numbers,linesFromFile[numbers])

galaxyLocations = []

for lineCounter, lines in enumerate(linesFromFile):
  for match in re.finditer(r'#', lines):
    galaxyPositionX = match.span()[0]
    galaxyPositionY = lineCounter
    galaxyLocations.append([galaxyPositionX, galaxyPositionY])
    
print(len(galaxyLocations))

galaxyPairs = [(a, b) for idx, a in enumerate(galaxyLocations) for b in galaxyLocations[idx + 1:]]
print(len(galaxyPairs))

totalShortestLength = 0
for count, pairs in enumerate(galaxyPairs):
  print(pairs)
  shortestLength = abs(pairs[0][0] - pairs[1][0]) + abs(pairs[0][1] - pairs[1][1])
  print(shortestLength)
  totalShortestLength += shortestLength
  print(totalShortestLength, count)
  input()

print(totalShortestLength)
