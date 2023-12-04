import re

file1 = open('input', 'r')
linesFromFile = file1.readlines()

def returnIndicesOfNumbers(lineString):
#Feed it a string return a list of the start and end position of the numbers in the line
  numberIndicesList = []
  numberIndices= re.finditer(r"\d+", lineString)
  for index in numberIndices:
    indices = range(index.span()[0], index.span()[1])
    numberIndicesList.append(indices)
  return numberIndicesList
  
def returnIndicesOfSymbols(lineString):
#Feed  a string return a list of the start and end position of the symbols in the line
  symbolIndicesList = []
  symbolIndices= re.finditer(r'[^.\d\n]',lineString)
  for index in symbolIndices:
    indices = range(index.span()[0]-1, index.span()[1]+1)
    symbolIndicesList.append(indices)
  return symbolIndicesList

def returnIndicesOfGears(lineString):
  #Feed  a string return a list of the start and end position of the symbols in the line
  symbolIndicesList = []
  symbolIndices= re.finditer(r'[*]',lineString)
  for index in symbolIndices:
    indices = range(index.span()[0]-1, index.span()[1]+1)
    symbolIndicesList.append(indices)
  return symbolIndicesList
    
def compareIndices(listOfIndicesNumbers, listOfIndicesSymbols,lines,runningTotal):
  innerTotal = 0
  for numbers in listOfIndicesNumbers:
    for symbols in listOfIndicesSymbols:
      xs = set(symbols) 
      overlap = xs.intersection(numbers)
      if overlap:
        partNumber = lines[numbers[0]:numbers[-1]+1]
        innerTotal += int(partNumber)
  return innerTotal
  
def lookForGearValue(numberIndex, gear,lines):
  gearValue = None
  gearValue2 = None
  for numbers in numberIndex:
    xs = set(numbers)
    overlap = xs.intersection(gear)
    if overlap:
      if gearValue:
        gearValue2=gearValue
      gearValue=int(lines[numbers[0]:numbers[-1]+1])
  if gearValue2 is not None:
    #Return a tuple when two gear values are returned
    return gearValue,gearValue2
  if gearValue is not None:
    return gearValue
        
  
previousLine = linesFromFile[0]

answerTotal = 0
#Part One
for lines in linesFromFile:
  previousNumbers = returnIndicesOfNumbers(previousLine)
  previousSymbols = returnIndicesOfSymbols(previousLine)

  numbers = returnIndicesOfNumbers(lines)
  symbols = returnIndicesOfSymbols(lines)
  #print("Comparison  between previous line numbers and current line symbols")
  answerTotal += compareIndices(previousNumbers,symbols,previousLine,answerTotal)
  #print("Comparison  previous line symbols and current line numbers")
  answerTotal += compareIndices(numbers,previousSymbols,lines,answerTotal)
  #print("Comparison  current line symbols and current line numbers")
  answerTotal += compareIndices(numbers,symbols,lines,answerTotal)

  previousLine = lines


print("Answer Part One:", answerTotal)


#Part Two
previousLine = linesFromFile[1]
previousPreviousLine = linesFromFile[0]
gearRatioTotal = 0
safeNumbers = 0
for lines in linesFromFile[2:]:
  previousPreviousNumbers = returnIndicesOfNumbers(previousPreviousLine)
  previousNumbers = returnIndicesOfNumbers(previousLine)
  numbers = returnIndicesOfNumbers(lines)

  numberIndexes = [previousPreviousNumbers, previousNumbers,numbers]
  lineToCheck = [previousPreviousLine,previousLine,lines]
  
  gears = returnIndicesOfGears(previousLine)
  for gear in gears:
    #print(gear)
    gearValue = []
    for i in range(3):
      gearValueTemp = lookForGearValue(numberIndexes[i], gear, lineToCheck[i])
      if not gearValueTemp is None:
        gearValue.append(gearValueTemp)
        res = type(gearValue[0]) is tuple
        #Need to catch case where gears are on the same line and create a tuple
        if res:
          gearRatioCurrent=gearValue[0][0]*gearValue[0][1]
          gearRatioTotal += gearRatioCurrent
          break

      if len(gearValue)==2:
        gearRatioCurrent = gearValue[0]*gearValue[1]
        gearRatioTotal += gearRatioCurrent
        break
  
  previousPreviousLine = previousLine
  previousLine = lines

print("Answer Part 2:", gearRatioTotal)
