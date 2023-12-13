file1 = open('inputTest', 'r')
linesFromFile = file1.readlines()
import re
import numpy as np

newList = list(map(lambda x: x.replace('.', '0'), linesFromFile))

newListAgain = []
testArray = np.array([])
count = 1



for rowNumber, items in enumerate(newList):
  try:
    splitText,_ = items.split('\n')
  except:
    print("end of the stupid file")
  #print(splitText)
  splitText= re.sub(r'#', '1', splitText)
  newListAgain.append([*splitText])

#print(newListAgain)
#newListAgain = [val for sublist in newListAgain for val in sublist]
testArray = np.array(newListAgain,dtype='object')

rowsToAdd = []
columnsToAdd = []

testArray[testArray == '0'] = 0
testArray[testArray == '1'] = 1

print("Zero rows")
zeroRows = (np.count_nonzero(testArray, axis = 0))
print("Zero columns")
zeroColumns = (np.count_nonzero(testArray, axis = 1))


print(np.nonzero(testArray))
print(testArray)
print(testArray.shape)