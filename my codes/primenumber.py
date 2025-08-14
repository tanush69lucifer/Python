# prime or not 
from sympy import isprime

num = int(input("Enter a number: "))
if isprime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Prime numbers within the given range 
# input section 
start = int(input('Enter the starting value '))  # 1
stop = int(input('Enter the last value '))  # 10
sum = 1
count = 0
for num in range(start, stop+1):
    
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num)

start=int(input())
stop=int(input())
sum=1
cnt=0
for num in range(start,stop+1):
    if num%1==0:
        cnt+=1
if count==2:
    print(num)