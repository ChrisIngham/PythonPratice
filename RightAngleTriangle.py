import math
'''
Christopher Ingham

check if right angle trianlge
we are given all lengths so we can just find the longest one
we know that is the hypotenuse squared is equal to the other 2 squared
if thats not the case then it is not right angled  

'''

length = list(map(int, input ("Enter all lengths of triangle with spaces seperating: ").split()))

if (length[0] > length[1] and length[0] > length[2]):
    if ((math.pow(length[0],2) == (math.pow(length[1],2)+ (math.pow(length[2],2))))):
        print ("This triangle has a right angle")
    else:
        print ("This triagnle does not have a right angle")

elif (length[1] > length[0] and length[1] > length[2]):
    if ((math.pow(length[1],2) == (math.pow(length[0],2)+ (math.pow(length[2],2))))):
        print ("This triangle has a right angle")
    else:
        print ("This triagnle does not have a right angle")

else:
    if ((math.pow(length[2],2) == (math.pow(length[0],2)+ (math.pow(length[1],2))))):
        print ("This triangle has a right angle")
    else:
        print ("This triagnle does not have a right angle")

'''
Could also make a method for the embedded if statments each step to make it cleaner
'''