# WAP to check whether a number is an armstrong number or not

def check_armstr(num):
    temp = num
    l= len(str(num)) # no.of digit in number
    sum =0
    while temp>0:
        digit = temp%10
        sum += digit**l
        temp //=10
    if sum == num: return True
    else:          return False

num = int(input("Enter a number to check is armstrong or not:"))

result = check_armstr(num) 

if result == True : print(f"{num} is armstrong number")
else:               print(f"{num} is not a armstrong number")