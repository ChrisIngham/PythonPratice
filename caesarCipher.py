'''
This cipher moves plaintext k units right 
if  plaintext is b and k is 3 then the ciphertext is e
prompt for k value and plaintext
'''

plainText = input("Enter your message: ")
key = int(input("Enter Key/ Units shifted: "))

i=0
newString = ""

while (i < len(plainText)):
    change = ord(plainText[i]) + key
    newString += chr(change)
    i += 1
print (newString)