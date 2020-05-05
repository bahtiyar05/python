x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
c = x1 + y1 + x2 + y2
if c % 2 == 0 and y2 > y1 and y2 - y1 >= abs(x1 - x2):
    print('YES')
else:
    print('NO')
