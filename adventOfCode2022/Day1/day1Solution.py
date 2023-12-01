import numpy as np

file1=open('input', 'r')
linesFromFile=file1.readlines()

calories = 0

elfArray = np.array([])

for lines in linesFromFile:
  if lines == '\n':
    elfArray=np.append(elfArray,[calories])
    calories=0
  else:
    calories=calories+int(lines)

elfArraySorted = np.sort(elfArray)

print('The top elf has '+str(elfArraySorted[-1])+' calories')
print('The top 3 elves are carrying '+str(elfArraySorted[-1]+elfArraySorted[-2]+elfArraySorted[-3])+' calories')