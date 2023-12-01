def checkWinner(player1, player2):
  if player2=='X':
      score=1
      if player1=='A':
        score=score+3
      elif player1=='B':
        score=score+0
      elif player1=='C':
        score=score+6
  elif player2=='Y':
    score=2
    if player1=='A':
      score=score+6
    if player1=='B':
      score=score+3
    if player1=='C':
      score=score+0
  elif player2=='Z':
    score=3
    if player1=='A':
      score=score+0
    if player1=='B':
      score=score+6
    if player1=='C':
      score=score+3
  return score

def matchResult(player1, desiredResult):
  if desiredResult=='X':
    score=0
    if player1=='A':
      #Player2 needs to lose against rock (scissors=3)
      score=score+3
    elif player1=='B':
      #Player2 needs to lose against paper (rock=1)
      score=1+0
    elif player1=='C':
      #Player2 needs to lose against scissors (paper=2)
      score=2+0
  elif desiredResult=='Y':
    score=3
    if player1=='A':
      #Player2 needs to draw against rock (rock=1)
      score=score+1
    elif player1=='B':
      #Player2 needs to draw against paper (paper=2)
      score=score+2
    elif player1=='C':
      #Player2 needs to draw against scissors (scissors=3)
      score=score+3
  elif desiredResult=='Z':
    score=6
    if player1=='A':
      #Player2 needs to win against rock (paper=2)
      score=score+2
    elif player1=='B':
      #Player2 needs to win against paper (scissors=3)
      score=score+3
    elif player1=='C':
      #Player2 needs to win against scissors (rock=1)
      score=score+1
  return score

file1=open('input', 'r')
linesFromFile=file1.readlines()

totalScore=0
totalScoreSecretStrategy=0
for lines in linesFromFile:
  gameScore=checkWinner(lines[0],lines[2])
  totalScore=totalScore+gameScore
  gameScore=matchResult(lines[0],lines[2])
  totalScoreSecretStrategy=totalScoreSecretStrategy+gameScore

print('Part 1 score = ',totalScore)
print('Part 2 score = ',totalScoreSecretStrategy)
  #print(lines[0])