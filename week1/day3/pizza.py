#this is a pizza calculator
print("Welcome to pythong pizza Deliveries! ")
size = input("What size Pizza you trying to get? S, M or L ")
add_pepperoni = input("you want the roni with it? Y or N ")
extra_cheese = input("how about some cheese? Y or N? ")

bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size: 
    bill += 25

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"your final bill is ${bill}")

