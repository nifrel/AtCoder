N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(M):
    if B[i] in A:
        A.pop(A.index(B[i]))
        B.pop(i)
        if B == None:
            print("Yes")
    else:
        print("No")