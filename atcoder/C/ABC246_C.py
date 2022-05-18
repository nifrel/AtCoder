N, K, X = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
m = 0

for i in range(N):
    sum = sum + A[i]
    m = m + A[i]//X
m = min(m, K)
sum = sum - m*X
K = K - m
for i in range(N):
    A[i] = A[i] % X

A.sort(reverse=True)

for i in range (N):
    if K == 0:
        break
    sum = sum - A[i]
    K -= 1

print(sum)
