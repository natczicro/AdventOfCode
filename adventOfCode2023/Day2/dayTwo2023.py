import re

file1 = open('input', 'r')
linesFromFile = file1.readlines()

redCubes = 12
greenCubes = 13
blueCubes = 14

IDSum = 0
totalPower = 0

for lines in linesFromFile:
  regexSplit = re.split(r':|;',lines)
  gameNumber = int(re.findall(r'\d+', regexSplit[0])[0])
  print(gameNumber)
  validGame = True
  games = regexSplit[1:]
  redMinimum = 0
  greenMinimum = 0
  blueMinimum = 0
  for matches in games:
    print(matches)
    redString = re.findall(r'\d+?\sr',matches)
    greenString = re.findall(r'\d+?\sg', matches)
    blueString = re.findall(r'\d+?\sb', matches)
    if redString:
      red = re.findall(r'\d+',redString[0])
      print(red)
      if int(red[0]) > redCubes:
        validGame = False
      if int(red[0]) > redMinimum:  #Part Two
        redMinimum = int(red[0])
    if greenString:
      green = re.findall(r'\d+',greenString[0])
      print(green)
      if int(green[0])>greenCubes:
        validGame = False
      if int(green[0]) > greenMinimum:  #Part Two
        greenMinimum = int(green[0])
    if blueString:
      blue = re.findall(r'\d+',blueString[0])
      print(blue)
      if int(blue[0])>blueCubes:
        validGame = False
      if int(blue[0]) > blueMinimum:  #Part Two
        blueMinimum = int(blue[0])
  powerCubes = blueMinimum*redMinimum*greenMinimum
  totalPower += powerCubes
  print(validGame)
  if validGame:
    IDSum += gameNumber

print(IDSum)
print(totalPower)