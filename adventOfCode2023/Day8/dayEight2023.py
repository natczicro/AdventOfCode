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
  allmatch = True
  for count,points in enumerate(startPoints):
    nextStart = followMap(directions, points, dict)
    #print(f'Assigning {nextStart} to {startPoints[count]}')
    startPoints[count]=nextStart
    if startPoints[count].endswith('Z'):
      print(f'All elements are {startPoints}')
      print(f'Element {startPoints[count]} ends with Z')
    else:
      allmatch = False

  if allmatch:
    break

print("Part Two Steps = ", steps)