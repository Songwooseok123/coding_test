# 19532 완전탐색
a, b, c, d, e, f = map(int, input().split())

if b == 0:
    x = c // a
    y = (f - d * x) // e
    print(x, y)
else:
    for x in range(-999, 1000):
        if (c - a * x) % b != 0:
            continue
        y = (c - a * x) // b
        if d * x + e * y == f:
            print(x, y)
            break
    

