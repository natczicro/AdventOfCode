import time
from tqdm import tqdm
file1 = open('input', 'r')
linesFromFile = file1.readlines()

currentMap = None

maps = {'seed-to-soil':[],
       'soil-to-fertilizer':[],
       'fertilizer-to-water':[],
       'water-to-light':[],
       'light-to-temperature':[],
       'temperature-to-humidity':[],
       'humidity-to-location':[]}

def findDestinationFromSource(source,map):
  for items in map:
    if int(items[1]) <= int(source) <= int(items[1])+int(items[2]):
      difference = int(source)-int(items[1])
      destination = int(items[0])+difference
      return destination

  return int(source)

start_time = time.time()
#Part One
for lines in linesFromFile:

  if lines.startswith('seeds'):
    _,seeds = lines.split(': ')
    seeds,_ = seeds.split('\n')
    
    seeds = seeds.split(' ')
    
  if not currentMap is None and not lines.startswith('\n'):
    numbers,_ = lines.split('\n')
    mappings = numbers.split(' ')
    mappings = [eval(i) for i in mappings]
    maps[currentMap].append(mappings)
    
  if lines.startswith('\n'):
    currentMap = None
  elif lines.startswith('seed-'):
    currentMap = 'seed-to-soil'
  elif lines.startswith('soil-'):
    currentMap = 'soil-to-fertilizer'
  elif lines.startswith('fertilizer-'):
    currentMap = 'fertilizer-to-water'
  elif lines.startswith('water-'):
    currentMap = 'water-to-light'
  elif lines.startswith('light-'):
    currentMap = 'light-to-temperature'
  elif lines.startswith('temperature-'):
    currentMap = 'temperature-to-humidity'
  elif lines.startswith('humidity-'):
    currentMap = 'humidity-to-location'

end_location = []
for items in seeds:
  destination = int(items)
  for keys in maps:
    destination = findDestinationFromSource(destination,maps[keys])
  end_location.append(destination)

print("End locations are",end_location)

print("minimum is", min(end_location))
print("--- %s seconds ---" % (time.time() - start_time))


#Part Two
import numpy as np

def refinedFindDestinationFromSource(source,map):
  rowcheck = np.where((map[:,1] <= source[0]))
  rowcheck2 = np.where(((map[:,2]+map[:,1]) <= source[1]))
  print(rowcheck, rowcheck2)
  rows = np.logical_and((map[:,1] <= source[0]),((map[:,2]+map[:,1]) <= source[1]))
  print(rows)
  #difference = source-map[rows,1]
  #destination = map[rows,0]+difference
  return destination

seedsStart = [eval(i) for i in seeds[::2]]

seedsRange = [eval(i) for i in seeds[1::2]]

destinationForMin = findDestinationFromSource((seedsStart[1]),maps['seed-to-soil'])
destinationForMiddle = findDestinationFromSource((seedsStart[1])+(seedsRange[1]),maps['seed-to-soil'])
destinationForMax = findDestinationFromSource((seedsStart[1])+(seedsRange[1]),maps['seed-to-soil'])

print("Checking Junk")
print(destinationForMin)
print(destinationForMiddle)
print(destinationForMax)
newMap = {'seed-to-soil':[],
       'soil-to-fertilizer':[],
       'fertilizer-to-water':[],
       'water-to-light':[],
       'light-to-temperature':[],
       'temperature-to-humidity':[],
       'humidity-to-location':[]}
for keys in maps:
  newMap[keys] = np.array(maps[keys])

'''
start_time = time.time()
for i in range(1,1000):
  oldDestination = findDestinationFromSource((seedsStart[0]),maps['seed-to-soil'])
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for i in range(1,1000):
  refinedDestination = refinedFindDestinationFromSource((seedsStart[0]),newMap['seed-to-soil'])
print("--- %s seconds ---" % (time.time() - start_time))
'''

#refinedDestination = refinedFindDestinationFromSource([seedsStart[0],seedsStart[0]+seedsRange[0]],newMap['seed-to-soil'])


minimumEndLocation = None
print("starting Brute Force method \n\n")
for i in range(len(seedsStart)):
  print(f'working on seed: {seedsStart[i]}')
  for startingSeed in tqdm(range(seedsStart[i],seedsStart[i]+seedsRange[i])):
    destination = startingSeed
    for keys in maps:
      destination = findDestinationFromSource(destination,maps[keys])
    if minimumEndLocation is None:
      minimumEndLocation = destination
    else:
      minimumEndLocation = min(minimumEndLocation,destination)
  print(f'After seed: {seedsStart[i]} the minimum is still {minimumEndLocation}')



#print(newMap)