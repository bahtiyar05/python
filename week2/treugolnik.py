a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    if c**2 + b**2 == a**2 or c**2 + a**2 == b**2 or a**2 + b**2 == c**2:
        print('rectangular')
    elif c**2 + b**2 > a**2 and c**2 + a**2 > b**2 and a**2 + b**2 > c**2:
        print('acute')
    elif c**2 + b**2 < a**2 or c**2 + a**2 < b**2 or a**2 + b**2 < c**2:
        print('obtuse')
    else:
        print('impossible')
else:
    print('impossible')
