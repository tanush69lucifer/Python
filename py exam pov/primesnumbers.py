import math
n = int(input())
for num in range(2, n + 1):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
        print(num, end=", ")