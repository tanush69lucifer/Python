import math
n = int(input())
arr = list(map(int, input().split()))
arr = [x for x in arr if x <= 1 or all(x % i for i in range(2, int(math.sqrt(x)) + 1))]
print(*arr)