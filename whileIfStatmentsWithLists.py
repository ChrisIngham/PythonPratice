import math

'''  
a^2 + b^2 = c^2
Only for right angle triangles tho

'''
x = 0
rAngle = input("Does your trianle have a right angle? (yes or no): ")
while x == 0: 
    if rAngle == "no":
        print("Sorry I cannot help solve your last length")        
        exit()
    else: 
        x=9
length = list(map(int, input ("Enter both values here, with a space seperating: ").split()))

if rAngle == "yes" : 
    hpyLen = math.hypot(length[0], length[1])
    print ("The length of the Hypotenuse is: " + str(hpyLen)) 
