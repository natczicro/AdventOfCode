import re

file1 = open('input', 'r')
linesFromFile = file1.readlines()

for lines in linesFromFile:
  numbers = re.findall(r'\d+', lines)
  print(numbers)
  symbols = re.findall(r'[^.\d+\n]',lines)
  print(symbols)
  
  numberIndices = re.finditer(r"\d+", lines)
  for matches in numberIndices:
    print(matches.span()[0],matches.span()[1])
    #print(lines[matches.span(0):matches.span(1)])
    #print(type(matches.span()))

  symbolIndices = re.finditer(r'[^.\d+\n]',lines)
  for matches in symbolIndices:
    print(matches.span())
