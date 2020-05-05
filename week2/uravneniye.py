a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a == 0 and b == 0):
    print('INF')
elif a == 0 or a * d == b * c:
    print('NO')
elif b // a * a == b:
    print(-b // a)
else:
    print('NO')
