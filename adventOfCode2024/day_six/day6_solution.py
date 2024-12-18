import os
import numpy as np
run_python_from=os.path.dirname(__file__)


file1 = open(os.path.join(run_python_from, 'input_day6.txt'),'r')

#file1 = open(os.path.join(run_python_from, 'input_day6.txt'),'r')

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

def step_forward_one(starting_point,maze_array):
    #returns a new point, and an updated maze_array
    
    #print(maze_array)

    if starting_point[0]-1<0:
        return maze_array, False
    elif maze_array[starting_point[0]-1,starting_point[1]] == '#':
        maze_array=np.rot90(maze_array)
        return maze_array, True
    maze_array[starting_point[0],starting_point[1]]='X'
    maze_array[starting_point[0]-1,starting_point[1]]='^'


    return maze_array, True

in_maze = True
next_step = starting_point
while in_maze == True:
    starting_point = np.where(maze_array=='^')
    starting_point=np.array([starting_point[0][0],starting_point[1][0]])
    maze_array, in_maze = step_forward_one(starting_point,maze_array)
    print(maze_array)
    print("next one")

print(np.count_nonzero(maze_array=='X'))
print(maze_array)