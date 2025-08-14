'''for i in range (1,6):
    for j in range(i):
        print("*",end="")
    print()

for i in range (1,6):
    for j in range(5-i+1):
        print("*",end="")
    print()
rows=6
for i in range(1,rows+1):
    for j in range(rows-i):
     print(' ',end="")
    for j in range(i):
      print('*',end="")
    print()
rows = 6
for i in range(1, rows+1):
    for j in range(rows-i):  # 
        print(' ', end='')
    for j in range(2*i-1): 
        print('*', end='')
    print()
rows = 6
for i in range(1, rows+1):
    for j in range(rows-i):  
        print(' ', end='')
    for j in range(2*i-1): 
        if j==0 or j==2*i-2 or i==rows//2+1:
          print('*', end='')
        else:
          print(' ',end='')
    print()'''
r=int(input())
pos=int(input())
for i in range(r):
    sp=' '*(r-i-1)
    if i==0:
        print(sp + '*')
    elif i==pos:
        print(sp+'*'*(2 * i + 1))
    else:
        print(sp +'*'+' '*(2 * i - 1)+'*')
