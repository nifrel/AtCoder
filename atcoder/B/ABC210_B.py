N = int(input())
S = input()
count = 0
for i in S:
    if count % 2 == 0:
        count += 1
        if int(i) == 1:
            print("Takahashi")
            exit()
        else:
            continue
    else:
        count += 1
        if int(i) == 1:
            print("Aoki")
            exit()
        else:
            continue
#findでindexを返す