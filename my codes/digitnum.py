# Number of digits in a number (Integer)
num = int(input('Enter the positive Integer Value: '))
tmp = num  # Storing the original number for display
out = 0
while num:
    num = num // 10
    out += 1
print(f'Total digits in number {tmp} is {out}')

num=int(input("enter number:"))
tmp=num
out=0
while num:
    num=num//10
    out=out+1
print(f'total number in {tmp} is {out}')


# finding number of diigts in a number
num=int(input(""))
tmp=num
out=0
while num:
    num=num//10
    out=out+1
print(f'number of digits in {tmp} is {out}')