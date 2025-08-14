n = int(input())
print(*[y for y in range(1, n + 1) if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)])