import math
n = int(input())
print(sum(i / math.factorial(i) for i in range(1, n+1)))