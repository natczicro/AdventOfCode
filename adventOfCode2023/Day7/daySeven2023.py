from collections import Counter
import numpy as np
import pandas as pd

file1 = open('input.txt', 'r')
linesFromFile = file1.readlines()

def determineTypeOfHand(hand):
  cardCount = Counter(hand)
  pairOfCards = None
  threeOfAKind= None
  for count, keys in enumerate(cardCount):

    #print(cardCount[keys])
    if cardCount[keys] == 5:
      rank = 7
      return rank
    elif cardCount[keys] == 4:
      rank = 6
      return rank
    elif cardCount[keys] == 3:
      if pairOfCards:
        rank = 5
        return rank
      threeOfAKind = True
    elif cardCount[keys] ==2:
      if threeOfAKind:
        rank = 5
        return rank
      if pairOfCards:
        rank = 3
        return rank
      pairOfCards = True

  if threeOfAKind:
    rank = 4
    return rank
  if pairOfCards:
    rank = 2
    return rank
  rank = 1
  return rank

def determineTypeOfHandJokers(hand):
  cardCount = Counter(hand)
  print(cardCount)
  onePair = None
  threeOfAKind = None
  pairOfCards = None
  fullHouse = None
  rank = None
  
  
  if not cardCount['J'] is None:
    numberOfJokers = cardCount['J']
  for keys in cardCount:
    #Skip if card is a joker
    if keys=='J':
      continue
    #Evaluate possibilities without accounting for joker
    if cardCount[keys] == 5:
      rank = 7
    elif cardCount[keys] == 4:
      rank = 6
    elif cardCount[keys] == 3:
      if onePair:
        fullHouse = True
      threeOfAKind = True
    elif cardCount[keys] == 2:
      if threeOfAKind:
        fullHouse = True
      if onePair:
        pairOfCards = True
      onePair = True
    
  if fullHouse:
    rank = 5
  elif threeOfAKind:
    rank = 4
  elif pairOfCards:
    rank = 3
  elif onePair:
    rank = 2
  elif rank is None:
    rank = 1
  if rank == 6 and numberOfJokers ==1:
    rank =7
  elif pairOfCards and numberOfJokers == 1:
    rank = 5
  elif threeOfAKind and numberOfJokers > 0:
    if numberOfJokers == 1:
      rank = 6
    else:
      rank = 7
  elif onePair and numberOfJokers > 0:
    if numberOfJokers ==1:
      rank = 4
    elif numberOfJokers ==2:
      rank = 6
    elif numberOfJokers ==3:
      rank = 7
  elif rank == 1 and numberOfJokers>0:
    if numberOfJokers ==1:
      rank = 2
    if numberOfJokers ==2:
      rank = 4
    if numberOfJokers ==3:
      rank = 6
    if numberOfJokers ==4:
      rank = 7

  if numberOfJokers == 5:
    rank = 7
    
  return rank
  
  

def separateHandIntoArray(hand,value,type,dictionary):
  #print(list(hand))
  bid,_ = value.split('\n')

  handList = [dictionary[k] for k in list(hand)]
  
  newList = [type, handList[0], handList[1], handList[2],
             handList[3], handList[4], int(bid)]

  #print(newList)
  return(newList)
  
exitCount = 0

cardDictionary = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10, 'J':11, 'Q':12, 'K':13,'A':14}

bigArray = np.zeros([1,7])

for lines in linesFromFile:
  hand,value = lines.split(' ')
  rank = determineTypeOfHand(hand)
  
  lineList= separateHandIntoArray(hand,value,rank,cardDictionary)
  lineArray = np.array(lineList)
  bigArray = np.vstack([bigArray, lineArray]) 
  exitCount += 1
  


#print(bigArray)

finalDataframe = pd.DataFrame(bigArray)
#bigArray = bigArray[bigArray[:, 0].argsort()[::-1]]


#print(finalDataframe)

sortedDataframe = finalDataframe.sort_values([0,1,2,3,4,5], ascending = [True, True, True, True, True, True])

sortedDataframe = sortedDataframe.reset_index(drop=True)
sortedDataframe['Winnings'] = sortedDataframe[6]*sortedDataframe.index
#print(sortedDataframe)

#print(sortedDataframe['Winnings'].sum())

#Part Two
hand = 'JJ777'
print(determineTypeOfHandJokers(hand))

cardDictionary = {'J':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10, 'Q':12, 'K':13,'A':14}

bigArray = np.zeros([1,7])
exitCount = 0
for lines in linesFromFile:
  hand,value = lines.split(' ')
  rank = determineTypeOfHandJokers(hand)

  lineList= separateHandIntoArray(hand,value,rank,cardDictionary)
  lineArray = np.array(lineList)
  bigArray = np.vstack([bigArray, lineArray]) 
  exitCount += 1



#print(bigArray)

finalDataframe = pd.DataFrame(bigArray)
#bigArray = bigArray[bigArray[:, 0].argsort()[::-1]]


#print(finalDataframe)

sortedDataframe = finalDataframe.sort_values([0,1,2,3,4,5], ascending = [True, True, True, True, True, True])

sortedDataframe = sortedDataframe.reset_index(drop=True)
sortedDataframe['Winnings'] = sortedDataframe[6]*sortedDataframe.index
print(sortedDataframe)

print('Joker total:',sortedDataframe['Winnings'].sum())