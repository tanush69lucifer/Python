
# also add starts top too
'''for n in range(1, 1000):
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print(n, "is not prime")
                break
        else:
            print(n, "is prime")
    else:
        print(n, "is not prime")'''

#pattern
n=int(input("enter number"))
for i in range(1,11):
    print(n,"*",i,"=",i*n,)
#natural sum and factorial
import math
n=int(input("enter value of n:"))
print(math.factorial(n))
width can also be made