from collections import Counter

file1 = open('input.txt', 'r')
linesFromFile = file1.readlines()

def determineTypeOfHand(hand):
  cardCount = Counter(hand)
  pairOfCards = None
  threeOfAKind= None
  cardCount[list(cardCount.keys())[0]]
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

def separateHandIntoArray(hand,value,type):
  #print(list(hand))
  bid,_ = value.split('\n')

  newList = [type, list(hand)[0], 
             list(hand)[1], list(hand)[2],
             list(hand)[3], list(hand)[4], int(bid)]

  print(newList)

exitCount = 0
category = {'five':[],
   'four':[],
   'full':[],
   'three':[],
   'twopair':[],
   'pair':[],
   'high':[]}

for lines in linesFromFile:
  hand,value = lines.split(' ')
  rank = determineTypeOfHand(hand)
  separateHandIntoArray(hand,value,rank)

  exitCount += 1
  if exitCount > 20:
    break
