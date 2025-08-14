n = int(input())
arr = list(map(int, input().split()))
arr.reverse()  # Reverses the entire array
print(*arr)