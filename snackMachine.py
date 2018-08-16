soda = ["Pepsi", "Root Beer", "Coke"]
chips = ["Lays", "Ruffles"]
candy = ["m&m", "kitKat", "smarties"]

while True:
    choice = input("Chips, Soda or Candy? ").lower()
    
    try:
    if choice == "soda":
        snack = soda.pop()
    elif choice == "chips":
        snack = chips.pop()
    elif choice == "candy":
        snack = candy.pop()
    else:
        print("Sorry, I didn't get that")
        continue
    except IndexError:
        print("We are all out of {}!".format(choice))

    print ("Your {} is {}".format(choice, snack))