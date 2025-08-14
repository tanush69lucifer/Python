#table making using for loop
n = int(input('Enter a number: '))
for a in range(10):
    b = n * (a + 1)
    print(n, '*', (a + 1), '=', b)

#for mulitiplying the loop n inner loop within
for a in range(10): #specified range will only have till 10 multiply staring from 0
    b = a + 1   #if a is 0 then b is 1
    c = 2 * b   #if b is 1 then c is multiplied by 2 
    print(c)    #by this we will get a brief idea on how range works within it 

#displays even number of digits between 50 and 100
for a in range(50,100):
    b=(a%2)
    if b==0:
        print(a)

#displays power from 1 till 14
for a in range (1,15):
    b=a*a
    print(b)

#skipping numbers y 3 between 30 and 70
for a in range(30,70,3):
    print(a)

#entering a chr and finding its position
str=input('enter a word : ')
ch=input('enter character you want to find position of : ')
pos=0
for a in str :
    pos=pos+1
    if a==ch:
        print("position pf character is :",pos)

