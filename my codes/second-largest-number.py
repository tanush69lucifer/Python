a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

if (a > b and a < c) or (a > c and a < b):   #make sure to cover all cases for second largest
    print("a =", a, "is the second largest")
elif (b > a and b < c) or (b > c and b < a):
    print("b =", b, "is the second largest")
else:
    print("c =", c, "is the second largest")
