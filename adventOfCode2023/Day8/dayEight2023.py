file1 = open('input', 'r')
linesFromFile = file1.readlines()

#print(linesFromFile[0])
route,_=linesFromFile[0].split('\n')
route = [*route]
#print(route)

dict = {}
for lines in linesFromFile[2:]:
  #print(lines)
  leftSide, rightSide = lines.split(' = ')
  left,right = rightSide.split(', ')
  _,left = left.split('(')
  right,_ = right.split(')')
  idict = {}
  idict['L'] = left
  idict['R'] = right
  dict[leftSide] = idict
  #dict[leftSide]['Left'] = left
  #dict[leftSide]['Right']= right
  #print(leftSide, left, right)

#print(dict)
#print(list(dict.keys())[-1])

def followMap(direction, start, mapDictionary):
  nextStart = mapDictionary[start][direction]
  return nextStart

from itertools import cycle
pool = cycle(route)


nextStart = 'AAA' #Starting position

for steps, directions in enumerate(pool):
  #print(nextStart, directions)
      
  #print(steps)
  if nextStart == 'ZZZ':
    break
  nextStart = followMap(directions, nextStart, dict)

print("Number of steps required = ", steps)

#Part Two
  
#Find entries that end in A
startPoints = list(key for key in dict.keys() if key.endswith("A"))
endPoints = list(key for key in dict.keys() if key.endswith("Z"))

print(startPoints, endPoints)
print("Starting Part Two")
input()
match = None
for steps, directions in enumerate(pool):
  print("Different Step")
  print(type(startPoints[0]))
  print(directions)
  input()
  '''
  if steps % 100 ==0:
    print(steps)
    print(startPoints)
    input()
  '''
  '''
  for start in startPoints:
    print(f'start is {start}')
    if start.endswith("Z"):
      print(startPoints)
      print(start)
      input()
      match = True
    else:
      print("Not perfect match")
      match = False
      break
  if match == True:
    break
  '''
  for count,points in enumerate(startPoints):
    nextStart = followMap(directions, nextStart, dict)
    print(f'Assigning {nextStart} to {startPoints[count]}')
    startPoints[count]=nextStart
    if startPoints[count].endswith('Z'):
      input()

print("Part Two Steps = ", steps)