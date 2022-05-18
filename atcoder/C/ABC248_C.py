N, M, K = map(int, input().split())
count = 0
A = list(range(1, M+1))

sum1 = 0
sum2 = 0
for l in range(M):
    sum1 = A[l]
    print(sum1)
    for i in range(M):
        sum2 = sum1 + A[i] 
        print(sum2)
        if sum2 <= K:
            count += 1
print(count)
