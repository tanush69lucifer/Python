'''seq="amit"
for val in seq:
    print("hi",end="*")
    print("python",end="#")

st=[1,2,3,3,4,5,6,7,8,9,10,11,12,"hello"]
for i in st :
    print(i)

#custom sequence
#seq=range(start,stop,step) default for step is 1
n=int(input("enter the number:"))
for i in range (1,n):
    print(i)

#a python program to display name n times n from use and name
name=input("enter name:")
n=int(input("enter value of n:"))
for i in range(n):
    print(name)
    i+=1

for i in range(2,-2,-1):
    print(i,end=" ")
#if start is less than stop then it will return start value unless you put - sign
#to display all divisor of a given number
n=int(input("enter number : "))
for i in range(1,n+1):
    if n%i==0:
        print(i)
# to find sum of all divisor excluding itself num//2+1 is used for big number
num=14
sm=0
for i in range(1,num):
    if num%i==0:
      sm=sm+i
      print(f'{num} ,sum of all Divisors',sm)
#to check whether given number is perfect or not
num=14
sm=0
for i in range(1,num):
    if num%i==0:
      sm=sm+i
      if sm==num:
         print("it is a perfect number")
      else: 
         print("it is not a perfect number")
# all perfect number betwwen 1 to 1000
nume=(1,1001)
sme=0
for i in range(1,nume):
    if nume%i==0:
      sme=sme+i
      if sm==num:
      print()
for num in range (1,10):
    sm=0
    for i in range(1,num):
      if num%i==0:
         sm=sm+i
    if sm==num:
      print(num)
#program to count number of divisor of particular divvisor
n=40
cnt=0
for i in range(1,n+1):
   if n%i==0 :
      cnt+=1
      print("number of divisor are",cnt)'''

#prime or not
n=int(input('enter a number:'))
if n>1:
    for i in range (2,int(n/2)+1):
        if n%i==0 :               #always check n is divisible by i not 1
            print(n,"is not prime")
            break                 #always break after completing
    else:
        print(n,"is prime")       #indendation should not exceed wrong 
else:
    print(n,"is not prime")
    


    

