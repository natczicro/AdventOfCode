import re
import numpy as np

file1 = open('input', 'r')
linesFromFile = file1.readlines()

def calculateScore(winnersList,valuesList):
  matches = 0
  for numbers in winnersList:
    for otherNumbers in valuesList:
      if numbers==otherNumbers:
        #print(numbers," matches ",otherNumbers)
        matches += 1
  if matches == 1:
    score = 1
  elif matches>1:
    score = 2**(matches-1)
  else:
    score = 0
  return score

def calculateMatches(winnersList,valuesList):
  matches = 0
  for numbers in winnersList:
    for otherNumbers in valuesList:
      if numbers==otherNumbers:
        #print(numbers," matches ",otherNumbers)
        matches += 1
  #print("Matches = ",matches)
  return matches

#Part One
totalScore = 0
for lines in linesFromFile:
  _,numbers=lines.split(":")
  winners,values = numbers.split("|")
  winnersList = re.findall(r'\d+',winners)
  valuesList = re.findall(r'\d+',values)
  #print(winnersList)
  #print(valuesList)
  #print(calculateScore(winnersList,valuesList))
  totalScore += calculateScore(winnersList,valuesList)

print("Answer to Part One: ", totalScore)

#Part Two
totalScore = 0
numberOfCards = np.ones(len(linesFromFile))

for count, lines in enumerate(linesFromFile):
  #print("Playing Card: ",count+1)
  _,numbers=lines.split(":")
  winners,values = numbers.split("|")
  winnersList = re.findall(r'\d+',winners)
  valuesList = re.findall(r'\d+',values)    
  originalMatches = calculateMatches(winnersList,valuesList)
  copies = int(numberOfCards[count])

  if count < len(linesFromFile):
    for i in range(originalMatches):
      numberOfCards[count+i+1]+= 1*copies

  # Weren't even looking for score...helps to read the question properly
  cardScore = calculateScore(winnersList,valuesList)
  totalCardScore = int(cardScore * numberOfCards[count])
  totalScore += totalCardScore

print("Answer to Part Two: ", int(numberOfCards.sum()))
