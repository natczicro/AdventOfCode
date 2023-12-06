import re
file1 = open('input', 'r')
linesFromFile = file1.readlines()

_,times = linesFromFile[0].split(":")

times = re.findall(r'\d+', times)
times = [eval(i) for i in times]

print(times)

_,distances = linesFromFile[1].split(":")

distances = re.findall(r'\d+', distances)
distances = [eval(i) for i in distances]

print(distances)

def distanceTraveled(timePressed, totalTime):
  timeTravelled = totalTime - timePressed 
  distance = timeTravelled * timePressed
  return distance

wins = 0

for i in range(0,times[0]):
  distance = distanceTraveled(i, times[0])
  if distance > distances[0]:
    wins += 1
print(wins)

wins = 0

for i in range(0,times[1]):
  distance = distanceTraveled(i, times[1])
  if distance > distances[1]:
    wins += 1

print(wins)

wins = 0

for i in range(0,times[2]):
  distance = distanceTraveled(i, times[2])
  if distance > distances[2]:
    wins += 1
print(wins)

wins = 0
for i in range(0,times[3]):
  distance = distanceTraveled(i, times[3])
  if distance > distances[3]:
    wins += 1
print(wins)

##Part Two

mergedTimes = str(times[0])+str(times[1])+str(times[2])+str(times[3])
print(mergedTimes)

mergedDistance = str(distances[0])+str(distances[1])+str(distances[2])+str(distances[3])
print(mergedDistance)

wins = 0
for i in range(0,int(mergedTimes)):
  distance = distanceTraveled(i, int(mergedTimes))
  if distance > int(mergedDistance):
    wins += 1
print("Part Two :",wins)