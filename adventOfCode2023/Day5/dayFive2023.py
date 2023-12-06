import time

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
seedsStart = [eval(i) for i in seeds[::2]]

seedsRange = [eval(i) for i in seeds[1::2]]

destinationForMin = findDestinationFromSource((seedsStart[0]),maps['seed-to-soil'])

destinationForMax = findDestinationFromSource((seedsStart[0])+(seedsRange[0]),maps['seed-to-soil'])

rangeToTest = range(seedsStart[0],seedsStart[0]+seedsRange[0])
setRangeToTest = set(rangeToTest)
print("reached")
for items in maps['seed-to-soil']:
  sourceStart = int(items[1])
  sourceEnd = int(items[1])+int(items[2])
  sourceRange = range(sourceStart, sourceEnd)
  #overlap = setRangeToTest.intersection(sourceRange)
  #print("overlap = ",overlap)

  

  
print(destinationForMin, destinationForMax)