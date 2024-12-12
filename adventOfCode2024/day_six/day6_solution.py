import os
import numpy as np
run_python_from=os.path.dirname(__file__)


#file1 = open(os.path.join(run_python_from, 'sample.txt'),'r')

file1 = open(os.path.join(run_python_from, 'input_day6.txt'),'r')

linesFromFile = file1.readlines()

big_list = []
for line in linesFromFile:
    try:
        line,_ = line.split('\n')
    except:
        print('last entry')
    line_entry = list(line)
    big_list.append(line_entry)

#print(big_list)

maze_array = np.array(big_list)


starting_point = np.where(maze_array=='^')
starting_point=np.array([starting_point[0][0],starting_point[1][0]])
direction = 'up'