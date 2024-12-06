file1 = open('sample.txt', 'r')
linesFromFile = file1.readlines()
import numpy as np


rules = []
pages_to_produce = []

rules_section = True
for line in linesFromFile:
    if line == '\n':
        rules_section=False
        continue
    if rules_section:
        line,_ = line.split('\n')
        line=line.split('|')
        line = list(map(int,line))
        rules.append(line)
    else:
        try:
            line,_ = line.split('\n')
            line = line.split(',')
            line = list(map(int,line))
            pages_to_produce.append(line)
        except:
            #print("Last line no linebreak")
            line = line.split(',')
            line = list(map(int,line))
            pages_to_produce.append(line)

print(rules)

print(pages_to_produce)

rules_array = np.array(rules)

def validate_rules(current_page, previous_pages):
    #Check if any of previous pages
    print(np.where(rules_array[:,1]==13))