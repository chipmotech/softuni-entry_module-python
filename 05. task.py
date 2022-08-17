name = ""
winner_name = ""
goals = 0
winner_goals = 0

while True:
    name = input()
    if(name == "END"):
        break
    goals = int(input())

    if goals > winner_goals:
        winner_goals = goals
        winner_name = name

    if goals >= 10:
        break

print(f"{winner_name} is the best player!")
if winner_goals >= 3:
    print(f"He has scored {winner_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {winner_goals} goals.")