days = int(input())
type_room = input()
feedback = input()

sleeping_nights = days - 1
all = 0

if days < 10:
    if type_room == "room for one person":
        all = sleeping_nights * 18.00
    elif type_room == "apartment":
        all = (sleeping_nights * 25.00) * 0.70
    elif type_room == "president apartment":
        all = (sleeping_nights * 35.00) * 0.90
elif 10 <= days <= 15:
    if type_room == "room for one person":
        all = sleeping_nights * 18.00
    elif type_room == "apartment":
        all = (sleeping_nights * 25.00) * 0.65
    elif type_room == "president apartment":
        all = (sleeping_nights * 35.00) * 0.85
elif days > 15:
    if type_room == "room for one person":
        all = sleeping_nights * 18.00
    elif type_room == "apartment":
        all = (sleeping_nights * 25.00) * 0.50
    elif type_room == "president apartment":
        all = (sleeping_nights * 35.00) * 0.80


if feedback == "positive":
    all = all * 1.25
elif feedback == "negative":
    all = all * 0.90

print(format(all,".2f"))

---------
number_of_days = int(input())
room_type = input()
response = input()
real_nights = number_of_days - 1
total = 0
if number_of_days > 15:
    if room_type == "room for one person":
        total = real_nights * 18.00
    elif room_type == "apartment":
        total = (real_nights * 25.00) * 0.50
    elif room_type == "president apartment":
        total = (real_nights * 35.00) * 0.80
elif 10 <= number_of_days <= 15:
    if room_type  == "room for one person":
        total = real_nights * 18.00
    elif room_type  == "apartment":
        total = (real_nights * 25.00) * 0.65
    elif room_type  == "president apartment":
        total = (real_nights * 35.00) * 0.85
elif number_of_days < 10:
    if room_type == "room for one person":
        total = real_nights * 18.00
    elif room_type == "apartment":
        total = (real_nights * 25.00) * 0.70
    elif room_type == "president apartment":
        total = (real_nights * 35.00) * 0.90
if response == "negative":
    total = total * 0.90
elif response == "positive":
    total = total * 1.25
print(format(total,".2f"))