N = int(input())
s = []
t = []

for i in range(N):
    _s, _t = map(str, input().split())
    s.append(_s)
    t.append(_t)

for i in range(N):
    flg = False
    for S in [s[i], t[i]]:
        s_ok = True
        for k in range(N):
            if i != k:
                if S == s[k] or S == t[k]:
                    s_ok = False
        if s_ok == True:
            flg = True
    if flg == False:
        print("No")
        exit()
print("Yes")


