T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    print(f"min={min(nums)}, max={max(nums)}")