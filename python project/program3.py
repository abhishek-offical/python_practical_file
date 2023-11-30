# WAP to print sum of all the prime number betweem two ranges.
def check_prime(num):
    if num<2: return False
    flag =0
    for i in range(2,(num//2)+1):
        if num%i== 0:
            return False
    return True
          
def SumPrimeR(start,end):
    sum_prime = 0
    for i in range(start,end+1):
        if check_prime(i) == True:
            sum_prime += i
    return sum_prime      

print("Enter start and end no. to print sum of primes")
start =int(input("Start :"))
end =int(input("End :"))

sum = SumPrimeR(start,end)

print(f"Sum of prime no. b/w {start} & {end} is {sum}")