import os
import numpy as np
run_python_from=os.path.dirname(__file__)


file1 = open(os.path.join(run_python_from, 'sample.txt'),'r')
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


def get_array_slice(starting_point, maze_array, direction):
    if direction=='up' or direction=='down':
        array_slice = maze_array[:,starting_point[1]]
        print(array_slice)
    else:
        array_slice = maze_array[starting_point[0],:]
        
    return array_slice

def distance_travelled(starting_point, maze_path, direction):
    if direction == 'up':
        start = starting_point[0]
        possible_ends = np.where(maze_path=='#')[0]
        end_index = np.where(possible_ends <start[0])[0][-1]
        end = possible_ends[end_index]
        if len(end) ==0:
            #guard is leaving
            next_direction='done'
            distinct_positions = start
            return _,distinct_positions,next_direction
        #end = max(end[0])
        distinct_positions = abs(start-end)-1
        next_direction='right'
        end_point=np.array([end+1,starting_point[1][0]])

    if direction == 'down':
        start = starting_point[0]
        possible_ends = np.where(maze_path=='#')[0]
        if len(possible_ends) ==0:
            #guard is leaving
            next_direction='done'
            distinct_positions = abs(start-len(maze_path))
            return distinct_positions,next_direction
        end = min(possible_ends)
        if end<start:
            #guard is leaving
            next_direction='done'
            distinct_positions = abs(start-len(maze_path))
            return distinct_positions,next_direction
        distinct_positions = abs(start-end)-1
        next_direction='left'
        end_point=np.array([end-1,starting_point[1][0]])
      

    if direction == 'right':
        start = starting_point[1]
        possible_ends = np.where(maze_path=='#')[0]
        if len(possible_ends) ==0:
            #guard is leaving
            next_direction='done'
            distinct_positions = abs(start-len(maze_path))
            return distinct_positions,next_direction
        end = min(possible_ends)
        if end<start:
            #guard is leaving
            next_direction='done'
            distinct_positions = abs(start-len(maze_path))
            return distinct_positions,next_direction
        distinct_positions = abs(start-end)-1
        next_direction='down'
        end_point=np.array([starting_point[0][0],end-1])


    if direction == 'left':
        start = starting_point[1]
        possible_ends = np.where(maze_path=='#')[0]
        end_index = np.where(possible_ends <start[0])[0][-1]
        end = possible_ends[end_index]
        if len(end) ==0:
            #guard is leaving
            next_direction='done'
            distinct_positions = start
            return distinct_positions,next_direction
        distinct_positions = abs(start-end)-1
        next_direction='up'
        end_point=np.array([starting_point[0][0],end+1])

    
    
    return end_point,distinct_positions[0],next_direction

print(maze_array)

starting_point = np.where(maze_array=='^')
direction = 'up'

print(starting_point[0],starting_point[1])
#maze_path = get_array_slice(starting_point, maze_array, direction)
#distance = distance_travelled(starting_point, maze_path, direction)
total_distance=0
while direction is not 'done':
    maze_path = get_array_slice(starting_point, maze_array, direction)
    starting_point,distance,direction = distance_travelled(starting_point, maze_path, direction)
    total_distance+=distance
print(distance)