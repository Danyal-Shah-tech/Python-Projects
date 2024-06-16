#Py Password Generator
import random
print("Welcome to Py Password Generator")

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y'
           'Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','&','(',')','^','%']
digits = ['0','1','2','3','4','5','6','7','8','9']

num_letters = int(input("Enter number of letters you want: "))
num_digits = int(input("Enter number of digits you want: "))
num_symbols = int(input("Enter number of symbols you want: "))
size = num_letters + num_digits + num_symbols
password = []

for i in range(1,num_letters+1):
    i = random.randrange(0,len(letters))
    password += letters[i]
    #password += random.choice(digits)
    
for j in range(1,num_digits+1):
    j = random.randrange(0,len(digits))
    password  += digits[j]
    #password += random.choice(digits)

for k in range(1,num_symbols+1):
    k = random.randrange(0,len(symbols))
    password += symbols[k]
    #password += random.choice(digits)

random.shuffle(password)
passcode = ""
for char in password:
    passcode += char
   
print(f"Your Password is : {passcode}")

