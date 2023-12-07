from collections import Counter

file1 = open('input.txt', 'r')
linesFromFile = file1.readlines()

def determineTypeOfHand(hand):
  cardCount = Counter(hand)

  cardCount[list(cardCount.keys())[0]]
  for count, keys in enumerate(cardCount):
    #print(cardCount[keys])
    if cardCount[keys] == 5:
      rank = 1
      return rank
    elif cardCount[keys] == 4:
      rank = 2
      return rank
    elif cardCount[keys] == 3:
      if cardCount[list(cardCount.keys())[count+1]] == 2:
        rank = 3
      else:
        rank = 4
      return rank
    elif cardCount[keys] ==2:
      if cardCount[list(cardCount.keys())[count+1]] == 3:
        rank = 3
        return rank
      elif (cardCount[list(cardCount.keys())[count+1]] == 2) or \
      (cardCount[list(cardCount.keys())[count+2]]== 2):
        rank = 5
        return rank
      else:
        rank = 6
        return rank
  rank = 7
  return rank
    

  
  print(len(cardCount))
  print(cardCount)

testhand = list('11111')
print('five of a kind has rank: ',determineTypeOfHand(testhand))
testhand = list('AAAA5')
print('four of a kind has rank: ',determineTypeOfHand(testhand))

testhand = list('22333')
print('full house has rank: ',determineTypeOfHand(testhand))

testhand = list('76555')
print('three of a kind has rank: ',determineTypeOfHand(testhand))

testhand = list('JJQQT')
print('two pair has rank: ',determineTypeOfHand(testhand))

testhand = list('44TJK')
print('a pair has rank: ',determineTypeOfHand(testhand))

testhand = list('12345')
print('nothing has rank: ',determineTypeOfHand(testhand))




'''
for lines in linesFromFile:
  hand,value = lines.split(' ')
  print(hand, value)
  determineTypeOfHand(hand)
  break
'''