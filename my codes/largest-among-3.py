a=int(input('enter 1st number:'))
b=int(input('enter 2nd number:'))
c=int(input('enter 3rd number:'))
if a>b and a>c :
    print('a : ',a,'is greatest')
elif b>a and b>c :
    print('b : ',b,'is greatest')
else:
    print('c : ',c,'is greatest')