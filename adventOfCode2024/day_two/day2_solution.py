file1 = open('day_two_input.txt', 'r')
linesFromFile = file1.readlines()
import numpy as np

def is_line_safe(line):
    numbers_list,_ = line.split('\n')
    numbers_list=numbers_list.split(' ')
    numbers_array = np.array(numbers_list)
    numbers_array = numbers_array.astype(int)
    for index,number in enumerate(numbers_array):
        if index == 0:
            #skip first number
            continue
        current_number = number
        last_number = numbers_array[index-1]
        
        #print(current_number, last_number)

        if current_number == last_number:
            return False
        
        if index ==1:
            if current_number > last_number:
                line_is_increasing = True
            elif current_number < last_number:
                line_is_increasing = False

        if (current_number > last_number and line_is_increasing is False) or abs(current_number-last_number)>3:
            #report is unsafe
            return False

        if (current_number < last_number and line_is_increasing) or abs(current_number-last_number)>3:
            #report is unsafe
            return False

    
    return True

total_safe_reports = 0
for line in linesFromFile:
    if is_line_safe(line):
        total_safe_reports+=1
        #print(line)
        #input()

print(total_safe_reports)

## Part Two

def is_line_safe_with_dampener(line):
    numbers_list,_ = line.split('\n')
    numbers_list=numbers_list.split(' ')
    numbers_array = np.array(numbers_list)
    numbers_array = numbers_array.astype(int)
    dampener_activated = False
    #print(numbers_array)
    #print(line_is_increasing)
    for index,number in enumerate(numbers_array):
        if index == 0:
            #skip first number
            continue
        current_number = number
        if dampener_activated:
            last_number = numbers_array[index-2]
        else:
            last_number = numbers_array[index-1]
    
        #print(current_number, last_number, index)

        if current_number == last_number:
            if dampener_activated:
                return False, numbers_array
            else:
                dampener_activated = True
                #print(numbers_array)
                numbers_array = np.delete(numbers_array,index)
                #print(numbers_array)
                continue
        
        if index ==1 or (index==2 and dampener_activated):
            if current_number > last_number:
                line_is_increasing = True
            elif current_number < last_number:
                line_is_increasing = False

        if (current_number > last_number and line_is_increasing is False) or abs(current_number-last_number)>3:
            if dampener_activated:
                return False, numbers_array
            else:
                dampener_activated = True
                #print(numbers_array)
                numbers_array = np.delete(numbers_array,index)
                #print(numbers_array)
                continue


        if (current_number < last_number and line_is_increasing) or abs(current_number-last_number)>3:
            if dampener_activated:
                return False, numbers_array
            else:
                dampener_activated = True
                #print(numbers_array)
                numbers_array = np.delete(numbers_array,index)
                #print(numbers_array)
                continue


    #print(numbers_array)
    return True, numbers_array

total_safe_reports_dampener = 0
for line in linesFromFile:
    print('\n',line)
    value, array = is_line_safe_with_dampener(line)
    print (value, array)
    input()

print(total_safe_reports_dampener)