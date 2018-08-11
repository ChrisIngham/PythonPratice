serviceCharge = 2
ticketPrice = 10
ticketRemain = 100

def calcPrice(tickets):
    return ((tickets * ticketPrice) + serviceCharge)

while (ticketRemain > 0 ):
    print ("There are {} tickets remaining".format(ticketRemain))
    name = input("Please Enter your name: ")
    
    try: 
        numOfTickets = int(input("{} how many tickets would you like? ".format(name)))
        #Also prints an error if request > 100
        if (numOfTickets > ticketRemain):
            raise ValueError("There are only {} tickets remaining".format(ticketRemain))
    except ValueError as err:
            print("There is an issue. {}. Please try again ".format(err) )
    else:     
        amount = calcPrice(numOfTickets)
        price = numOfTickets * ticketPrice
        print("The total price for your {} tickets {} is: ${}".format(numOfTickets, name, price))
        proceed = input("{} would you like to proceed?(Y/N) ".format(name))
        if (proceed.lower() == "y"):
            print ("Thank you {} for your purchase of {} tickets! ".format(name, numOfTickets))
            ticketRemain = ticketRemain - numOfTickets
        else: 
            print ("Thank you for shopping {} ".format(name))

print ("Sorry there are no more tickets left to be sold! ")