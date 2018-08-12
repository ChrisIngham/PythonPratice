import os 
shoppingList = []

#Clears the screen
def clearScreen():
   os.system("cls" if os.name == "nt" else "clear") 

#adds items to the list
def addToList(item):
    showList()
    if len(shoppingList):
        position = input("Where on the list do I add {}?\n"
        "Press ENTER to add to end of list\n"
        "> ".format(item))
    else:
        position = 0

    try:
        #changing the value to a absolute number, not negative
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shoppingList.insert(position-1, item)
    else:
        shoppingList.append(newItem)
    showList()

#shows a help tab for user
def help():
    clearScreen()
    print("What should we purchase? ")
    print("""
Enter "Done" to stop
Enter "Help" for help   
Enter "Show" to show list
    """)

#shows all items in the list
def showList():
    clearScreen()
    
    index = 1 
    for items in shoppingList:
        print("{}. {} ".format(index, items))
        index +=1
    print("- "*10)
help()
while True: 
    newItem = input("* ")

    if newItem.upper() == "DONE" or newItem.upper() == "QUIT":
        break
    elif newItem.upper() == "HELP":
        help()
        continue
    elif newItem.upper() == "SHOW":
        showList()    
        continue
    else:
        addToList(newItem)

showList()