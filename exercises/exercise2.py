# Exercise 2 - Shopping Cart Program

item = input("Enter the item: ")
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))
total_price = price * quantity

print("---------------------------------------")
print(f"You have bought {quantity} x {item}/s")
print(f"The total price is ${total_price}")