# All Perfect number within the given range 
for num in range(1, 1001):
    sum = 0
    for i in range(1, num):
            if num % i == 0:
                sum = sum + i
    if sum==num:
            print(num)

for num in range(1,100):
      sum=0
      for i in range(1,num):
            sum=sum+i
      if sum==num:
       print(num)
for i in range(1,100):
     sum=0
     for i in range(1,num):
          if num%i==0:
               sum=sum+1
     if sum==num:
          print(num)
