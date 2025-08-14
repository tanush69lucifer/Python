t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(min(arr[i+1] - arr[i] for i in range(n-1)))