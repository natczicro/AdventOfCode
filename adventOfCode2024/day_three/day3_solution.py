import re

f = open("day_three_input.txt", "r")

input_text = f.read()
#Part One
true_muls = re.findall(r'(mul\(\d+,\d+\))', input_text)
total = 0
for multiples in true_muls:
    numbers = re.findall(r'\d+', multiples)
    result= int(numbers[0])*int(numbers[1])
    total +=result

print(f'Total is {total}')

#Part Two
true_muls = re.findall(r'((do\(\))|(don\'t\(\))|(mul\(\d+,\d+\)))', input_text)
total = 0
do_boolean = True
for entries in true_muls:
    print(entries[0])
    print(do_boolean)

    if do_boolean:
        if entries[0].startswith('mul'):
                numbers = re.findall(r'\d+', entries[0])
                result= int(numbers[0])*int(numbers[1])
                total +=result
        elif entries[0].startswith('don\'t()'):
             do_boolean = False
    else:
         if entries[0].startswith('do()'):
              do_boolean = True
    print(do_boolean)
    print(total)
    #input()
print(f'Total is {total}')