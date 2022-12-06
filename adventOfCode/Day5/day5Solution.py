import numpy as np
import re

file1=open('input', 'r')
linesFromFile=file1.readlines()

crateList=[]

def buildCrateStack(position, crateLines):
  print('may use')
  crateList=[]
  for i in reversed(range(len(crateLines))):
    entireLine=crateLines[i]

    crate=entireLine[position]
    if crate==' ':
      print('stack done')
      break
    crateList.append(crate)
  print(crateList)
  return(crateList)
    
  

for i, lines in enumerate(linesFromFile):  
  if lines=='\n':
    print('reached empty line')
    headerLine=i-1
    break

crateLines = linesFromFile[0:headerLine]
for lines in crateLines:
  print(lines)
numbers=re.findall(r"[1-9]",linesFromFile[headerLine])
print(numbers)
print(numbers[0])
position=re.search(numbers[0],linesFromFile[headerLine]).start()
print(position)
crateArrayList=[]
for j in range(len(numbers)):
  position=re.search(numbers[j],linesFromFile[headerLine]).start()
  crateArrayList.append(buildCrateStack(position,crateLines))
#listOne=buildCrateStack(position,crateLines)

print(crateArrayList[0])
print(crateArrayList[1])