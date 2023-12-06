import time
start_time = time.time()

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
'''
print("testing below")
print("destination",findDestinationFromSource(seeds[1],maps['seed-to-soil']))
print("testing above")

print(seeds)

print(maps['seed-to-soil'][0])
'''
end_location = []
for items in seeds:
  #print("initial seed",items)
  destination = int(items)
  for keys in maps:
    #print("current values and key",destination, keys, maps[keys],"\n")
    destination = findDestinationFromSource(destination,maps[keys])
  end_location.append(destination)

print("End locations are",end_location)

print("minimum is", min(end_location))
print("--- %s seconds ---" % (time.time() - start_time))

seeds2 = seeds[::2]

seeds3 = seeds[1::2]

print(seeds2)

print(seeds3)

possible_ends=[]
start_time = time.time()
print(int(seeds2[0]), int(seeds3[0]))

for i in range(int(seeds2[0]),int(seeds2[0])+int(seeds3[0])):
  jake =i+i
  
print("--- %s seconds ---" % (time.time() - start_time))

print("Done",jake)

print("difference is going to be ", abs(int(min(seeds2))-int(max(seeds2))))