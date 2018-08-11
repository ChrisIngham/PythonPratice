shoppingList = []

def addToList(item):
    shoppingList.append(item)
    print ("{} has been added to the list! There are currently {} items ".format(item, len(shoppingList)))

def help():
    print("What should we purchase? ")
    print("""
Enter "Done" to stop
Enter "Help" for help   
Enter "Show" to show list
    """)

def itemList():
    for items in shoppingList:
        print("> " + items)

help()
while True: 
    newItem = input("* ")

    if newItem == "Done":
        break
    elif newItem == "Help":
        help()
        continue
    elif newItem == "Show":
        itemList()    
        continue

    addToList(newItem)

itemList()