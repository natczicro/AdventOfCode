import re

file1=open('input', 'r')
linesFromFile=file1.readlines()

def parseNumbersFromLine(line):
  numbers=re.split(r"\D",line)
  firstNumberPair = numbers[0:2]
  secondNumberPair = numbers[2:4]
  return(firstNumberPair,secondNumberPair)

def completeOverlap(arrayOne, arrayTwo):
  if len(arrayOne)>len(arrayTwo):
    A=set(arrayOne)
    B=set(arrayTwo)
  else:
    A=set(arrayTwo)
    B=set(arrayOne )

  return(B.issubset(A))

totallyRedundantElves = 0
partiallyRedundantElves = 0

for lines in linesFromFile:
  [elfOne,elfTwo]=parseNumbersFromLine(lines)

  elfOneArray = list(range(int(elfOne[0]), int(elfOne[1])+1,1))
  elfTwoArray = list(range(int(elfTwo[0]), int(elfTwo[1])+1,1))
  
  redundantElf=completeOverlap(elfOneArray,elfTwoArray)
  totallyRedundantElves=totallyRedundantElves+redundantElf
  
  usefulElves = set(elfOneArray).isdisjoint(set(elfTwoArray))
  partialOverlap = not usefulElves
  partiallyRedundantElves=partiallyRedundantElves+partialOverlap

print(totallyRedundantElves)
print(partiallyRedundantElves)

  