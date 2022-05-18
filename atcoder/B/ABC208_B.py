P = int(input())
s = []
_s = 1
for i in range(1, 11):
    _s = _s * i
    s.append(_s)
p = P
ans = 0
for j in (range(9, -1, -1)):
    i = 0
    if P - s[j] >= 0: 
        while p >= s[j]:
            p = p - s[j]
            i += 1
    ans = ans + i
print(ans)
#階乗はmath.factorial(n)でできる
# // 演算子を使うと割り算した際の商の整数値を返す
# iを使わずともカウントできる？