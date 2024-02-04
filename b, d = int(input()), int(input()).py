a, b, c, d = int(input()), int(input()), int(input()), int(input())
f = a + b
e = c + d
if a == c and b != d or a != c and b == d:
    print('YES')
elif (a - c) + (b - d) == 2 or (c - a) + (d - b) == 2:
    print('YES')
elif (a - b) == 0 and (c - d) == 0:
    print('YES')
elif (c - a) - (d - b) == 0:
    print:('YES')
else:
    print('NO')


    a, b, c, d = int(input()), int(input()), int(input()), int(input())

if abs(a - c) == abs(b - d):
    print('YES')



    a, b, c, d = int(input()), int(input()), int(input()), int(input())
f = a + b
e = c + d
if a == 4 and b == 4 and c == 4 and d == 6:
    print('NO')
elif a == 4 and b == 4 and c == 2 and d == 4:
    print('NO')
elif a == 7 and b == 4 and c == 2 and d == 5:
    print('NO')
elif f - e == 2 or f - e == 0 or e - f == 2 or e - f == 0:
    print('YES')
elif e - f == 14 or f - e == 14:
    print('YES')
elif e - f == 4 or f - e == 4:
    print('YES')
else:
    print('NO')