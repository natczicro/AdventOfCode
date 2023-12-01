import re
import string

file1=open('input', 'r')
linesFromFile=file1.readlines()

totalPriority=0

def splitRucksackInHalf(rucksack):
  sizeOfRucksack = len(rucksack)
  firstCompartment=rucksack[slice(0,sizeOfRucksack//2)]
  secondCompartment = lines[slice(sizeOfRucksack//2,sizeOfRucksack)]
  return(firstCompartment,secondCompartment)

def findCommonCharacters(stringOne,stringTwo):
  setForComparison = set(stringOne)
  commonCharacters=(setForComparison.intersection(stringTwo))
  return(commonCharacters)
  
def calculateLetterPriority(letter):
  priorityList=list(string.ascii_letters)
  priorityString=''.join(priorityList)
  priorityRegexSearch=re.search(letter, priorityString)
  priority=priorityRegexSearch.start()+1
  return priority

for lines in linesFromFile:
  [firstCompartment,secondCompartment]=splitRucksackInHalf(lines)
  commonCharacters=findCommonCharacters(firstCompartment,secondCompartment)
  
  priority=calculateLetterPriority(commonCharacters.pop())
  totalPriority=totalPriority+int(priority)

print(totalPriority)

badgePriority=0

for i, lines in enumerate(linesFromFile):
  if i ==0 or i%3==0:
    firstElf=lines.strip()
  elif i==1 or i%3==1:
    secondElf=lines.strip()
  else:
    thirdElf=lines.strip()
    firstCommon=findCommonCharacters(firstElf,secondElf)
    finalCommon=findCommonCharacters(firstCommon,thirdElf)
    badge=finalCommon.pop()
    priority=calculateLetterPriority(badge)
    badgePriority=badgePriority+priority

print(badgePriority)
    
  