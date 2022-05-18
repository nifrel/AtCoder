N , X =map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if i%2 == 1:
        X = X - (A[i]-1)
    else:
        X = X - A[i]
if X >= 0:
    print("Yes")
else:
    print("No")
#偶数番目はi = 1, 3, 5となることに注意
