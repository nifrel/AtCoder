N = int(input())
h = list(map(int, input().split()))
dp = [10**10] * N
dp[0] = 0
dp[1] = abs(h[1] - h[0])
for i in range(2, N):
    first = dp[i-1] + abs(h[i] - h[i-1])
    second = dp[i-2] + abs(h[i] - h[i-2])
    if first < second:
        min = first
    else:
        min = second
    dp[i] = min
print(dp[N-1])