'''
User enters a year between 1900 and 2099 and this function returns the date it occurs in April
a = year % 19  
b = year % 4
c = year % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7
dateofeaster = 22 + d + e
'''

year = int(input("What year would you like to know the date of Easter? Must be between 1900 & 2099: "))

# If out of range do not continue program
if (year < 1900 or year > 2099):
    print ("Your year is out of range, sorry")
    exit()


a = year % 19
b = year % 4
c = year % 7 
d = (19 * a * 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7

dateOfEaster = (22 + d + e)
print ("The date of Easter in " + str(year) + " is April " + str(dateOfEaster) )