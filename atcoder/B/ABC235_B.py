N = int(input())
H = list(map(int, input().split()))
ans = H[0]
for i in range(N):
    if i == N-1:
        if ans < H[i]:
            ans = H[i]
    else:
        if H[i] < H[i+1]:
            ans = H[i+1]
        else:
            break
print(ans)
    
