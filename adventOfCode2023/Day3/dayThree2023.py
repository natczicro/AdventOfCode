import re
import numpy as np

file1 = open('input', 'r')
linesFromFile = file1.readlines()

def returnIndicesOfNumbers(string):

def returnIndicesOfSymbols(string):

def compareIndices(listOfIndicesOne, listOfIndicesTwo):

def compareIndicesOnSameLine

for lines in linesFromFile:
  previousNumberIndicesList = []
  previousNumberList = []

  previousSymbolIndicesList = []
  previousSymbolList = []

  
  previousLine = lines
  previousLineItems = re.findall(r'\d+|[^.\d+\n]', previousLine)
  previousNumberIndices = re.finditer(r"\d+", previousLine)
  previousSymbolIndices = re.finditer(r'[^.\d+\n]',previousLine)
  for index in previousNumberIndices:
    indices = [index.span()[0], index.span()[1]]
    previousNumberIndicesList.append(indices)
    previousNumberList.append(index.group(0))

  print(previousNumberIndicesList)
  print(previousNumberList)
  
  currentLineItems = re.findall(r'\d+|[^.\d+\n]', lines)
  currentNumberIndices = re.finditer(r"\d+", lines)
  currentSymbolIndices = re.finditer(r'[^.\d+\n]',lines)
  for index in previousNumberIndices:
    indices = [index.span()[0], index.span()[1]]
    previousNumberIndicesList.append(indices)
    previousNumberList.append(index.group(0))
  #print(previousLineItems)
  #print(currentLineItems)
  
  numberIndices = re.finditer(r"\d+", lines)
  '''
  for matches in numberIndices:
    print(lines[matches.span()[0]:matches.span()[1]])
    
    #print(lines[matches.span(0):matches.span(1)])
    #print(type(matches.span()))

  symbolIndices = re.finditer(r'[^.\d+\n]',lines)
  for matches in symbolIndices:
    print(matches.span())
'''