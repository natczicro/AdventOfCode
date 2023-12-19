file1 = open('input', 'r')
linesFromFile = file1.readlines()

import numpy as np
import re

def findCubeRocks(line):
  #print(line)
  indices = []
  for match in re.finditer(r'\#', line):
    indices.append(match.start())
  return indices

def moveRoundRocks(line,blockRow,numberOfRows,load):
  indices = []
  for match in re.finditer(r'O', line):
    indices.append(match.start())
  for index in indices:
    load += numberOfRows - blockRow[index] 
    blockRow[index]+=1
  return blockRow, load
    
  
def moveBlock(blockRow, line,row,numberOfRows, load):
  cubeRocks = findCubeRocks(line)
  blockRow, load = moveRoundRocks(line,blockRow,numberOfRows,load)
  print(cubeRocks)
  #print(blockRow)
  print(line)
  for index in cubeRocks:
    print("have cube rocks")
    blockRow[index] = row+1
  print(blockRow)
  print(load)
  #input()
  return blockRow, load
  
def partOne():
  #Split list into inidivual elements
  numberOfRows = len(linesFromFile)
  splitList = []
  for lines in linesFromFile:
    lines,_ = lines.split('\n')
    splitList.append(lines)
  
  #array=np.array(splitList)
  #print(array.shape)
  print(len(splitList[0]))
  
  #Assign starting blocker point as 0
  blockRow = [0]*len(splitList[0])
  print(blockRow)
  
  #loop through array rows
  #For each 0 see where it moves to (check blocker point) and calculate score
  #Move blocking point if 0 gets moved or if # is present
  load = 0
  for row, line in enumerate(splitList):
    blockRow, load = moveBlock(blockRow,line,row,numberOfRows,load)
    
  print(load)
  #rinse and repeat

partOne()