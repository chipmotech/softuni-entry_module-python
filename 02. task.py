tshirt_price = float(input())
price_amount = float(input())

shorts = tshirt_price * 0.75
socks = shorts * 0.20
shoes = 2 * (tshirt_price + shorts)

all = (tshirt_price + shorts + socks + shoes) * 0.85

if all >= price_amount:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {all:.2f} lv.")
else:
    amount_to_discount = price_amount - all
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {amount_to_discount:.2f} lv. more.")