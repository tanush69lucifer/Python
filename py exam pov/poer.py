n = int(input())
print(1 if 1 <= n <= 100000000 and (n & (n - 1)) == 0 else 0)