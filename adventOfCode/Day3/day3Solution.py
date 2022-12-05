import re
import string

file1=open('input', 'r')
linesFromFile=file1.readlines()
priorityList=list(string.ascii_letters)
priorityString=''.join(priorityList)

totalPriority=0

def splitRucksackInHalf(rucksack):
  sizeOfRucksack = len(rucksack)
  firstCompartment=rucksack[slice(0,sizeOfRucksack//2)]
  secondCompartment = lines[slice(sizeOfRucksack//2,sizeOfRucksack)]
  return(firstCompartment,secondCompartment)

def findCommonCharacter(stringOne,stringTwo):
  setForComparison = set(stringOne)
  commonCharacter=(setForComparison.intersection(secondCompartment)).pop()
  return(commonCharacter)
  

for lines in linesFromFile:
  [firstCompartment,secondCompartment]=splitRucksackInHalf(lines)
  commonCharacter=findCommonCharacter(firstCompartment,secondCompartment)
  
  priorityRegexSearch=re.search(commonCharacter, priorityString)
  priority=priorityRegexSearch.start()
  totalPriority=totalPriority+int(priority)+1

print(totalPriority)