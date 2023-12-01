import re

file1 = open('input.txt', 'r')
linesFromFile = file1.readlines()

# Part 1
'''
total = 0
for line in linesFromFile:
  digits = re.findall(r'\d+', line)
  #print(type(digits))
  joinedDigits = "".join(digits)
  print("initial value",joinedDigits)
  #print(joinedDigits)
  if len(joinedDigits) > 2:
    #print(joinedDigits[0])
    #print(joinedDigits[-1])
    firstDigit = joinedDigits[0]
    secondDigit = joinedDigits[-1]
    joinedDigits = firstDigit+secondDigit

  if len(joinedDigits) == 1:
    joinedDigits = joinedDigits[0] + joinedDigits[-1]
    

  print("final value",int(joinedDigits))
  total += int(joinedDigits)
  print("running total is ",total)

print("total is", total)
'''
# Part 2
totalPart2 = 0
for line in linesFromFile:
  #Look ahead required in order to return both numbers from a string like nineight
  digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
  print(digits)
  if not (digits[0].isnumeric()):
    if digits[0] == 'one':
      digits[0] = 1
    elif digits[0] == 'two':
      digits[0] = 2
    elif digits[0] == 'three':
      digits[0] = 3
    elif digits[0] == 'four':
      digits[0] = 4
    elif digits[0] == 'five':
      digits[0] = 5
    elif digits[0] == 'six':
      digits[0] = 6
    elif digits[0] == 'seven':
      digits[0] = 7
    elif digits[0] == 'eight':
      digits[0] = 8
    elif digits[0] == 'nine':
      digits[0] = 9

  if not (digits[-1].isnumeric()):
    if digits[-1] == 'one':
      digits[-1] = 1
    elif digits[-1] == 'two':
      digits[-1] = 2
    elif digits[-1] == 'three':
      digits[-1] = 3
    elif digits[-1] == 'four':
      digits[-1] = 4
    elif digits[-1] == 'five':
      digits[-1] = 5
    elif digits[-1] == 'six':
      digits[-1] = 6
    elif digits[-1] == 'seven':
      digits[-1] = 7
    elif digits[-1] == 'eight':
      digits[-1] = 8
    elif digits[-1] == 'nine':
      digits[-1] = 9

  calibrationValue = str(str(digits[0])+str(digits[-1]))
  print(calibrationValue)
  
  totalPart2 += int(calibrationValue)
  print(totalPart2)

print(totalPart2)