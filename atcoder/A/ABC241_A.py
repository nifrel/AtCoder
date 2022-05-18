a = list(map(int, input().split()))
i = 0
ans = 0
for j in range(3):
    ans = a[i]
    i = ans
print(ans)
