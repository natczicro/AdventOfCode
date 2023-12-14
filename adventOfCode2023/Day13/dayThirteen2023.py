import numpy as np

file1 = open('input', 'r')
linesFromFile = file1.readlines()

#print(linesFromFile)


def determineSymmetry(patternList):
  patternArray = np.array(patternList)
  previousRow = []
  for rowNumber, row in enumerate(patternArray):
    #print(patternArray[rowNumber])
    #input()
    #print(previousRow))
    #print(row))
    if np.array_equal(patternArray[rowNumber], patternArray[rowNumber - 1]):
      if rowNumber - 2 >= 0 and rowNumber + 1 < patternArray.shape[0]:
        if np.array_equal(patternArray[rowNumber + 1],
                          patternArray[rowNumber - 2]):
          symmetryRow = [rowNumber]
          axisSymmetry = 0
          return symmetryRow, axisSymmetry
        else:
          continue
      else:
        symmetryRow = [rowNumber]
        axisSymmetry = 0
        return symmetryRow, axisSymmetry


  patternArray = np.array(patternList).T
  for rowNumber, row in enumerate(patternArray):
    #print(previousRow)
    #print(row))
    if np.array_equal(patternArray[rowNumber], patternArray[rowNumber - 1]):
      if rowNumber - 2 >= 0 and rowNumber + 1 < patternArray.shape[0]:
        if np.array_equal(patternArray[rowNumber + 1],
                          patternArray[rowNumber - 2]):
          symmetryRow = [rowNumber]
          axisSymmetry = 1
          return symmetryRow, axisSymmetry
        else:
          continue
      else:
        symmetryRow = [rowNumber]
        axisSymmetry = 1
        return symmetryRow, axisSymmetry


def determineSummary(symmetryIndex, axis):
  if axis == 0:
    #calculate for rows
    summarization = int(symmetryIndex[0]) * 100
  else:
    summarization = int(symmetryIndex[0])
  #print(summarization)
  return summarization


def partOne():
  patternList = []
  summary = 0
  for rowNumber, items in enumerate(linesFromFile):
    if items == '\n':  #Different pattern
      patternArray = np.array(patternList)
      print(patternArray)
      symmetryIndex, axis = determineSymmetry(patternList)
      print(symmetryIndex, axis)
      summary += determineSummary(symmetryIndex, axis)
      print(summary)
      patternList = []
      #input()
      continue
    try:
      splitText, _ = items.split('\n')
      patternList.append([*splitText])
      print(splitText)
    except:
      "end of file"

  print(summary)


partOne()