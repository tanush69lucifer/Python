c='y'
while c!='n':
    n1=int(input('enter number 1:'))
    n2=int(input('enter number 2:'))
    ch=input('enter choice :')
    if ch=='+':
       r=n1+n2
       print('result=',r)
    elif ch=='-':
       r=n1-n2
       print('result=',r)
    elif ch=='*':
        r=n1*n2
        print('result=',r)
    elif ch=='/':
        r=n1/n2
        print('result=',r)
    else:
        print('enter write choice of characters')
        break
c=input('do you wish to continue(y/n) : ')
