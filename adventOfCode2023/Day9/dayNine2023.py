file1 = open('input', 'r')
linesFromFile = file1.readlines()
import numpy as np

def getToZero(array,rightValue):
  rightValue.append(array[-1])
  difference = np.diff(array)
  if not np.any(difference):
    return rightValue
  else:
    return getToZero(difference,rightValue)

def getToZeroAlternative(array,leftValue):
  leftValue.append(array[0])
  difference = np.diff(array)
  if not np.any(difference):
    return leftValue
  else:
    return getToZeroAlternative(difference,leftValue)

def getHistoryLeft(leftValue):
  newValue = 0
  #print("subtraction value: ",newValue)

  for value in leftValue:
    #print("array element: ",value)
    newValue = value-newValue
    #print("subtraction value: ",newValue)

  return newValue
finalValue = 0    

for lines in linesFromFile:
  lineList,_ = lines.split('\n')
  lineList = lineList.split(' ')
  lineList = [eval(i) for i in lineList]

  array= np.array(lineList)

  rightValue = list()
  rightValue = getToZero(array,rightValue)

  #print('right most values', rightValue)

  #print("new entry = ",sum(rightValue))

  finalValue += sum(rightValue)

print("Answer for Part One: ",finalValue)

#Part Two 
# Could've just reversed each line and then use the identical logic as the first part
finalValue = 0
for lines in linesFromFile:
  lineList,_ = lines.split('\n')
  lineList = lineList.split(' ')
  lineList = [eval(i) for i in lineList]

  array= np.array(lineList)

  leftValue = list()
  leftValue = getToZeroAlternative(array,leftValue)
  #print(leftValue)
  leftValue.reverse()

  newHistory = getHistoryLeft(leftValue)
  
  #print(newHistory)
  #print('right most values', rightValue)

  finalValue += (newHistory)


print("Answer for Part Two: ", finalValue)