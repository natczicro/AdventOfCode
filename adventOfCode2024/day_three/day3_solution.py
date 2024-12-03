import re

f = open("day_three_input.txt", "r")

input = f.read()
#Part One
true_muls = re.findall(r'(mul\(\d+,\d+\))', input)
total = 0
for multiples in true_muls:
    numbers = re.findall(r'\d+', multiples)
    result= int(numbers[0])*int(numbers[1])
    total +=result

print(f'Total is {total}')