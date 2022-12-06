import re

file1=open('input', 'r')
linesFromFile=file1.readlines()


def buildCrateStack(position, crateLines):
  crateList=[]
  for i in reversed(range(len(crateLines))):
    entireLine=crateLines[i]

    crate=entireLine[position]
    if crate==' ':
      break
    crateList.append(crate)
  return(crateList)
    
def performCrateMove(move,crateArray):
  numbersInLine=re.findall(r"[0-9]+",move)

  for k in range(int(numbersInLine[0])):
    #print(k)
    crateInCrane=crateArray[int(numbersInLine[1])-1].pop()
    crateArray[int(numbersInLine[2])-1].append(crateInCrane)

  return(crateArray)

def performSuperCrateMove(moves,altcrateArray):
  numbersInLines=re.findall(r"[0-9]+",moves)

  firstStack=altcrateArray[(int(numbersInLines[1])-1)]
  secondStack=altcrateArray[(int(numbersInLines[2])-1)]

  startSlice=-int(numbersInLines[0])
  cratesToMove=firstStack[startSlice:]

  firstStack=firstStack[:startSlice]
  secondStack=secondStack+cratesToMove

  altcrateArray[(int(numbersInLines[1])-1)]=firstStack
  altcrateArray[(int(numbersInLines[2])-1)]=secondStack
  return(altcrateArray)


def main():
  print("running program")
  for i, lines in enumerate(linesFromFile):  
    if lines=='\n':
      headerLine=i-1
      break

  crateLines = linesFromFile[0:headerLine]
  instructionLines = linesFromFile[headerLine+2:]

  numbers=re.findall(r"[0-9]",linesFromFile[headerLine])

  crateArrayList=[]
  for j in range(len(numbers)):
    position=re.search(numbers[j],linesFromFile[headerLine]).start()
    crateArrayList.append(buildCrateStack(position,crateLines))

  for items in crateArrayList:
    print(items[-1])
  secondCrateArrayList=crateArrayList

  for lines in instructionLines:
    #crateArrayList=performCrateMove(lines,crateArrayList)
    secondCrateArrayList=performSuperCrateMove(lines,secondCrateArrayList)

  for items in crateArrayList:
    print(items[-1])

  for items in secondCrateArrayList:
    print(items[-1])

main()