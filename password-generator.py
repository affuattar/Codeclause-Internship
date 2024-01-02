
import numbers
import random


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','*','+'] 

print ("\n\nWelcome to Password Generator!!\n")

n_letters = int(input("\nHow Many Letters You Want in Your Password ?\n"))
n_symbols = int(input("\nHow Many Symbols You Want in Your Password ?\n"))
n_numbers = int(input("\nHow Many Numbers You Want in Your Password ?\n"))


password = ""
for i in range(1,n_letters+1):
    char = random.choice(letters)
    password += char

for i in range(1,n_symbols+1):
    char = random.choice(symbols)
    password += char

for i in range(1,n_numbers+1):
    char = random.choice(numbers)
    password += char


print("\n")
print("Your Simple Password Can Be:\n")
print(password)    
print("\n")


password_list = []
for i in range(1,n_letters+1):
    char = random.choice(letters)
    password_list += char

for i in range(1,n_symbols+1):
    char = random.choice(symbols)
    password_list += char

for i in range(1,n_numbers+1):
    char = random.choice(numbers)
    password_list += char


print("\n")
print("Your Password Elements List Can Be:\n")
print(password_list)    
print("\n")

print("\n")
print("Your Password Elements List After Shuffling Can Be:\n")
random.shuffle(password_list)
print(password_list)    
print("\n")

password = ""
for char in password_list:
    password += char

print("\nFinal Password That Can Be Difficult To crack Can Be:\n")
print(password)
print("\n")    