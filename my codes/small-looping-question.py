#first prints code upto 5 or desired number of printings
a=1
while a<=5:
    print('python')
    a=a+1
#second even numbers till 20
n=1
while n<=20:
    n=n+1
    if (n%2==0):
        print(n)
#third odd numbers in descending order from 9
n=9
while n>1:
    if n%2==1:
        print(n)
        n=n-2
#fourth table
n=int(input('enter your number : '))
i=1
while i<=10:
    multi=n*i
    print(n,'*',i,'=',multi)
    i=i+1
#fifth sum of 15 natural numbers
num=range(1,16)
total_sum=sum(num)
print(total_sum)
#sixth shows number from the inputted number till we written eg,100
num=int(input('enter your number : '))
while num<=100 :
    print(num)
    num=num+1