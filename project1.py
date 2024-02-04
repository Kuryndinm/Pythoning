a_1, b_1, a_2, b_2 = int(input()), int(input()), int(input()), int(input())

if a_2 <= b_1 and a_2 >= a_1:
    print(a_2)
    if b_2 > b_1:
        print(b_1)
    elif b_2 <= b_1:
        print(b_2)
    elif a_2 > a_1:
        print(a_1)
    elif b_2 > b_1:
        print(b_1)
    elif b_2 <= b_1:
        print(b_2)
    else:
        print('пустое множество')
a_1, b_1, a_2, b_2 = int(input()), int(input()), int(input()), int(input())

if a_2 <= b_1 and a_2 >= a_1:
    x = a_2
    if b_2 > b_1:
        y = b_1
    elif b_2 <= b_1:
        z = b_2
    elif a_2 > a_1:
        c = a_1
    elif b_2 > b_1:
        y = b_1
    elif b_2 <= b_1:
        z = b_2
        print(x, y)
    else:
        print('пустое множество')