N = int(input())
a = [[0]*3 for i in range(N+1)]
dp = [[0]*3 for i in range(N+1)]
for i in range(N):
    _a, _b, _c = map(int, input().split())
    a[i] = [_a, _b, _c]
# print(a)
for i in range(N):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i+1][k] = max(dp[i+1][k], dp[i][j] + a[i][k])
            # print(dp)
            
ans = 0
for i in range(3):
    ans = max(ans, dp[N][i])
print(ans)
