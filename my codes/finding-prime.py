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