import statistics

number_of_students = int(input())
i = 0
marks_list = []
for i in range(number_of_students):
    marks_list.append(float(input()))

group_2 = 0
group_3 = 0
group_4 = 0
group_5 = 0

for x in marks_list:
    if 2.00 <= x <= 2.99:
        group_2 = group_2 + 1
    elif 3.00 <= x <= 3.99:
        group_3 = group_3 + 1
    elif 4.00 <= x <= 4.99:
        group_4 = group_4 + 1
    elif 5.00 <= x:
        group_5 = group_5 + 1

group_5_per = (group_5 / number_of_students) * 100
group_4_per = (group_4 / number_of_students) * 100
group_3_per = (group_3 / number_of_students) * 100
group_2_per = (group_2 / number_of_students) * 100
avg = statistics.mean(marks_list)

print(f"Top students: {group_5_per:.2f}%")
print(f"Between 4.00 and 4.99: {group_4_per:.2f}%")
print(f"Between 3.00 and 3.99: {group_3_per:.2f}%")
print(f"Fail: {group_2_per:.2f}%")
print(f"Average: {avg:.2f}")

-------------
import statistics
students_number = int(input())
mark_list = []
group1 = 0
group2 = 0
group3 = 0
group4 = 0
for a in range(students_number):
    mark_list.append(float(input()))
for mark in mark_list:
    if 2.00 <= mark <= 2.99:
        group1 += 1
    elif 3.00 <= mark <= 3.99:
        group2 += 1
    elif 4.00 <= mark <= 4.99:
        group3 += 1
    elif 5.00 <= mark:
        group4 += + 1

print(f"Top students: {((group4 / students_number) * 100):.2f}%")
print(f"Between 4.00 and 4.99: {((group3 / students_number) * 100):.2f}%")
print(f"Between 3.00 and 3.99: {((group2 / students_number) * 100):.2f}%")
print(f"Fail: {((group1 / students_number) * 100):.2f}%")
print(f"Average: {(statistics.mean(mark_list)):.2f}")