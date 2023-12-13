file1 = open('input', 'r')
linesFromFile = file1.readlines()
import re

print(len(linesFromFile))
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
    
  
galaxyPairs = [(a, b) for idx, a in enumerate(galaxyLocations) for b in galaxyLocations[idx + 1:]]

totalShortestLength = 0
for pairs in galaxyPairs:
  print(pairs[0][1])
  shortestLength = abs(pairs[0][0] - pairs[1][0]) + abs(pairs[0][1] - pairs[1][1])
  totalShortestLength += shortestLength

print(totalShortestLength)