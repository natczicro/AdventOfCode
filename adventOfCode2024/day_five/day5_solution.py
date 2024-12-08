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

def calculate_total(pages_to_produce, rules_array):
    total = 0
    bad_pages = []
    for entry in pages_to_produce:
        previous_pages = []
        entry_is_good = True
        for page in entry:
            if validate_rules(page, previous_pages, rules_array) is False:
                entry_is_good = False
                bad_pages.append(entry)
                break
            else:
                previous_pages.append(page)
        if entry_is_good:
            total+=entry[int(len(entry)/2)]
    return total, bad_pages

total_score_part_one, bad_pages =  calculate_total(pages_to_produce, rules_array)
print(total_score_part_one)

#Part Two
def validate_rules2(current_page, previous_pages, rules_array):
    #Check if any of previous pages
    #print(np.where(rules_array[:,1]==current_page))
    rule_hits = np.where(rules_array[:,0]==current_page)
    for index in rule_hits[0]:
        if rules_array[index,1] in previous_pages:
            return False, previous_pages.index(rules_array[index,1])
    
    return True, None


def validation_complete(entry, rules_array):
    for index,page in enumerate(reversed(entry)):
        previous_pages = entry[0:len(entry)-(index+1)]
        valid, index_problem = validate_rules2(page, previous_pages, rules_array)
        if valid is False:
            entry.remove(page)
            entry.insert(index_problem, page)
            validation_complete(entry, rules_array)
    return entry

total = 0
for entry in bad_pages:
    final_entry = validation_complete(entry, rules_array)
    total+=final_entry[int(len(final_entry)/2)]
print(total)