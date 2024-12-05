import re
import numpy as np

file1 = open('day_three_input.txt', 'r')
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

numpy_array = np.array(big_list)

#print(numpy_array)

x_locations=(np.where(numpy_array=='X'))

#print(x_locations[0][0],x_locations[1][0])

#input()
#print(np.size(x_locations))

xes_present = int(np.size(x_locations)/2)


def search_around_x(start_x, start_y, y_direction, x_direction,numpy_array):
    if start_y + y_direction*3<0:
        return False
    elif start_y + y_direction*3>=np.shape(numpy_array)[0]:
        return False
    elif start_x + x_direction*3<0:
        return False
    elif start_x + x_direction*3>= np.shape(numpy_array)[1]:
        return False
    
    if numpy_array[start_x+x_direction][start_y+y_direction] == 'M' and numpy_array[start_x+x_direction*2][start_y+y_direction*2] == 'A' and numpy_array[start_x+x_direction*3][start_y+y_direction*3]=='S':
        return True
    else:
        return False

#print(np.shape(numpy_array)[0])

total = 0
for i in range(xes_present):
    #print(x_locations[0][i],x_locations[1][i])

    total+=search_around_x(x_locations[0][i], x_locations[1][i], 1, 1,numpy_array)
    total+=search_around_x(x_locations[0][i], x_locations[1][i], 0, 1,numpy_array)
    total+=search_around_x(x_locations[0][i], x_locations[1][i], 1, 0,numpy_array)
    total+=search_around_x(x_locations[0][i], x_locations[1][i], 1, -1,numpy_array)
    total+=search_around_x(x_locations[0][i], x_locations[1][i], -1, 1,numpy_array)
    total+=search_around_x(x_locations[0][i], x_locations[1][i], -1, 0,numpy_array)
    total+=search_around_x(x_locations[0][i], x_locations[1][i], 0, -1,numpy_array)
    total+=search_around_x(x_locations[0][i], x_locations[1][i], -1, -1,numpy_array)
    #print(total)
    #input()

print(total)

#Part Two

a_locations=(np.where(numpy_array=='A'))

#print(x_locations[0][0],x_locations[1][0])

#input()
#print(np.size(x_locations))

as_present = int(np.size(a_locations)/2)

def search_around_a(start_x, start_y,numpy_array):
    if start_y -1 <0:
        return False
    elif start_y + 1>=np.shape(numpy_array)[0]:
        return False
    elif start_x - 1<0:
        return False
    elif start_x + 1 >= np.shape(numpy_array)[1]:
        return False
    
    if ((numpy_array[start_x+1][start_y+1] == 'M' and numpy_array[start_x-1][start_y-1] == 'S') or (numpy_array[start_x+1][start_y+1] == 'S' and numpy_array[start_x-1][start_y-1] == 'M'))\
        and ((numpy_array[start_x-1][start_y+1]=='M' and numpy_array[start_x+1][start_y-1]=='S') or (numpy_array[start_x-1][start_y+1]=='S' and numpy_array[start_x+1][start_y-1]=='M')):
            return True
    else:
        return False
    
total = 0
for i in range(as_present):
    #print(x_locations[0][i],x_locations[1][i])

    total+=search_around_a(a_locations[0][i], a_locations[1][i],numpy_array)

    #print(total)
    #input()

print(total)