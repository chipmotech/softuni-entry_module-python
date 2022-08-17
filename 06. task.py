def nums(first_number, last_number, step=1):
    return range(first_number, last_number+1, step)

number = int(input())

number_string = str(number)

number_1 = int(number_string[0])
number_2 = int(number_string[1])
number_3 = int(number_string[2])

a = 0
b = 0
c = 0

for a in nums(1, number_3):
    for b in nums(1, number_2):
        for c in nums(1, number_1):
            result = a * b * c
            print(f"{a} * {b} * {c} = {result};")