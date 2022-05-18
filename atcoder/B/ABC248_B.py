A, B, K = map(int, input().split())
sum = A
num = 0
while sum < B:
    sum *= K
    num += 1
print(num)