'''n=9876558
cnt=0
while n :
  n=n//10
  cnt+=1
print(cnt)

num=int(input("enter number"))
cnt=0
if num==0:
  print(cnt+1)
else :
  num=num//10
  cnt+=1
print(cnt)

num=123
reverse_digit=0
while num:
 d=num%10
 reverse_digit=reverse_digit*10+d
 num=num//10
print(reverse_digit)
#if last is 0 '''

#sum of square of each digit
n=int(input("enter number:"))
s=0
while n>0:
    d=n%10
    s=s+d**2
    n=n//10
print(s)