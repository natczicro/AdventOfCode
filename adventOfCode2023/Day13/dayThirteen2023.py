import numpy as np

file1 = open('input', 'r')
linesFromFile = file1.readlines()

#print(linesFromFile)


def determineSymmetry(patternArray):
  symmetryFlag = False
  for rowNumber, row in enumerate(patternArray):
    #print(previousRow)
    if rowNumber ==0:
      continue
    print(row)
    if np.array_equal(patternArray[rowNumber], patternArray[rowNumber - 1]):
      print("matching rows")
      count=1
      symmetryFlag = True
      symmetryRow = [rowNumber]
      while (rowNumber - 1-count >= 0 and rowNumber + count < patternArray.shape[0]):
        print("checking other lines for sym")
        if np.array_equal(patternArray[rowNumber +count],
                          patternArray[rowNumber -1-count]):
          symmetryFlag = True
        else:
          symmetryFlag = False
          print("mismatch in symm")
        count += 1
  if symmetryFlag:
    return symmetryRow



def determineSummary(symmetryIndex, axis):
  if axis == 0:
    #calculate for rows
    summarization = int(symmetryIndex[0]) * 100
  elif axis ==1:
    summarization = int(symmetryIndex[0])
  #print(summarization)
  return summarization

#def doABunchOfStuff():
  

def partOne():
  patternList = []
  summary = 0
  for rowNumber, items in enumerate(linesFromFile):
    #print(items)
    if items == '\n':  #Different pattern
      symmetryIndex = None
      patternArray = np.array(patternList)
      print(patternArray)
      #input()
      print("checking rows")
      symmetryIndex = determineSymmetry(patternArray)
      if symmetryIndex is not None:
        print("symmetry row is ", symmetryIndex)
        axis = 0
        summary += determineSummary(symmetryIndex, axis)
      else:
        print("checking columns")
        patternArray = np.array(patternList).T
        symmetryIndex = determineSymmetry(patternArray)
        if symmetryIndex is not None:
          print("symmetry column is ", symmetryIndex)
          axis = 1
          summary += determineSummary(symmetryIndex, axis)
      patternList = []
      print(summary)
      continue
    if items.endswith('\n'):
      splitText, _ = items.split('\n')
      patternList.append([*splitText])
    else:
      symmetryIndex = None
      patternList.append([*items])
      patternArray = np.array(patternList)
      print(patternArray)
      #input()
      print("checking rows")
      symmetryIndex = determineSymmetry(patternArray)
      if symmetryIndex is not None:
        axis = 0
        summary += determineSummary(symmetryIndex, axis)
      else:
        print("checking columns")
        patternArray = np.array(patternList).T
        symmetryIndex = determineSymmetry(patternArray)
        if symmetryIndex is not None:
          axis = 1
          summary += determineSummary(symmetryIndex, axis)
      print(summary)
      patternList = []
      continue
  print(summary)


partOne()