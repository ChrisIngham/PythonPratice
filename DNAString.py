'''
Prompts the user for DNA string

Prints GC-Content and length
'''

dna = input("Enter a DNA string: ")

length = len(dna)

i =0
gcAmount = 0
while (i < length):
    if (dna[i].lower() == "g" or dna[i].lower() == "c"):
        gcAmount += 1
    i += 1

gcContent = gcAmount / length
gcPercentile = gcContent * 100

print ("The GC-Content is: " + str(gcContent) + " or " + str(gcPercentile) + "%" + "\n" + "The string length is " + str(length) ) 