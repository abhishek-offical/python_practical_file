# WAP a menu driven program to accept two strings from the user perform 
# the various function using user define function
def string_concat(s1,s2):
    return print(s1+s2)

def count_vowel(s1): 
    vowel = 0
    for char in s1:
        if char.lower() in 'aeiou':
            vowel+=1 
    return print (f"number of vowel in str1 is:{vowel}")

def is_Lower(s1):
    for char in s1:
        if not (char>='a' and char<='z'):
            return print("False")
    return print("Ture") 

def Upper(s1):
    s = ''
    for ch in s1:
        if ch >='a' and ch<='z': s +=chr(ord(ch)-32)
        else:                    s +=ch
    return print(s)

def Join(s1,s2):
    ele = input("Enter a special character to join string:")
    l1 = [s1,s2]
    s =''
    for i in l1[:-1]: s+=i+ele
    s+=l1[-1]
    return print(s)

   
str1 = input("Enter first string :")
str2 = input("Enter second string :")
print()
print("___Menu of string operation___")
print("1. string concatenation")
print("2. count vowel")
print("3. is_Lower")
print("4. Upper")
print("5. Join")
print("6.exit\n")
while True:

    choice = input("Enter your chice :")

    if choice == "1": string_concat(str1,str2)
    elif choice == "2": count_vowel(str1)
    elif choice == "3": is_Lower(str1)
    elif choice == "4": Upper(str1)
    elif choice == "5": Join(str1,str2)
    elif choice == "6": break
    else: print("You Enter a wrong option!!!")

