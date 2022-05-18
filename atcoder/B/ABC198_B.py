N = input()
for i in range(len(N)):
    if N == ''.join(reversed(N)):
        print("Yes")
        exit()
    else:
        N = '0' + N
print("No")
# N == N[::-1]で回文判定ができる
# N[::-1]で逆順を表す


