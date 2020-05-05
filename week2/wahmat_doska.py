X1 = int(input())
Y1 = int(input())
X2 = int(input())
Y2 = int(input())
if((X1 + Y1) % 2 == 0 and (X2 + Y2) % 2 == 0):
    print('YES')
elif ((X1 + Y1) % 2 != 0 and (X2 + Y2) % 2 != 0):
    print('YES')
else:
    print('NO')
