import math 
def is_armstrong(number):
    digits = str(number)
    num_digits = len(digits)
    total = sum(int(digit) ** num_digits for digit in digits)
    return total == number
num = int(input("enter number:"))
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

import math
def is_armstrong(number):
    digits=str(number)
    num_digits=len(digits)
    total=sum(int(digit)**num_digits for digit in digits)
    return total==number
if  is_armstrong(num):
    print(f'{num}is armostrong')
else:
    print(f'{num} not armstrong')

def is_armstrong(number):
    digits=str(number)
    num_digit=len(digits)
    total=sum(int(digits)**num_digit for diigt in digits)
    return total==number
num=int(input("enter number"))












def is_armstrong(number):
    digits=str(number)
    num_digit=len(digits)
    total=sum(int(digit)**num_digit for digit in digits)
    return total==number
num=int(input())

