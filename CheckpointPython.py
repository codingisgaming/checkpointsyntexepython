print("Welcome to Python Pizza Deliveries")

size = input("What size of pizza do you want? (S, M, L): ")
appir= input("Do you want pepperoni on your pizza? (yes/no): ")
anches= input("Do you want extra cheese on your pizza? (yes/no): ")

cash = 0

if size == "S":
    cash+= 15
elif size == "M":
    cash += 20
elif size == "L":
    cash += 25

if appir == "yes":
    if size == "S" or size == "M":
        cash += 2
    else:
        cash+= 3

if anches() == "yes" :
    cash+= 1

print(f"Your final amount  is: ${cash}.")
