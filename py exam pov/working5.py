T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    print((B * C) // A)
