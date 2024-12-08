import os

run_python_from=os.path.dirname(__file__)


print(run_python_from)
file1 = open(os.path.join(run_python_from, 'day_five_input.txt'),'r')
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

#print(rules)

#print(pages_to_produce)

rules_array = np.array(rules)

def validate_rules(current_page, previous_pages, rules_array):
    #Check if any of previous pages
    #print(np.where(rules_array[:,1]==current_page))
    rule_hits = np.where(rules_array[:,0]==current_page)
    for index in rule_hits[0]:
        if rules_array[index,1] in previous_pages:
            return False
    
    return True

total = 0
for entry in pages_to_produce:
    previous_pages = []
    entry_is_good = True
    for page in entry:
        if validate_rules(page, previous_pages, rules_array) is False:
            entry_is_good = False
            break
        else:
            previous_pages.append(page)
    if entry_is_good:
        total+=entry[int(len(entry)/2)]
        
print(total)