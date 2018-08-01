'''
Take a number and turn it into its triangular number
everytime a base 10 number increases it adds an extra row to the bottom of a triangle
                    1                                   1
  1 = 1          1     1 = 2 so 3 in triangular       1   1    = 3  which is 6 in triangular
                                                    1   1   1

the mathematical equation is  n(n + 1) / 2 

'''
num = int(input("What number to convert to Triangular "))

triNum = ((num*(num+1)/2))

print ("The Triangular Number is: " + str(triNum))