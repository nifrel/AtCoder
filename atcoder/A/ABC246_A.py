def main():
    x_1, y_1 = map(int, input().split())
    x_2, y_2 = map(int, input().split())
    x_3, y_3 = map(int, input().split())
    x = [x_1, x_2, x_3]
    y = [y_1, y_2, y_3]
    if x_1 == x_2:
        print(x_3, end="")
    elif x_2 == x_3:
        print(x_1, end="")
    else:
        print(x_2, end="")
    print(" ", end="")
    if y_1 == y_2:
        print(y_3, end="")
    elif y_2 == y_3:
        print(y_1, end="")
    else:
        print(y_2, end="")
    
main()