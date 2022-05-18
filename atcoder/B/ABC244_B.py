N = int(input())
T = list(input())
x = 0
y = 0
dir = 1 # 1:higasi 2:minami 3:nisi 4: kita
for i in range(N):
    if T[i] == "S":
        if dir == 1:
            x += 1
        elif dir == 2:
            y -= 1
        elif dir == 3:
            x -= 1
        elif dir == 4:
            y += 1
    elif T[i] == "R":
        dir = dir % 4
        dir += 1
print(x, y)



