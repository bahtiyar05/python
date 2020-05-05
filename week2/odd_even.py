A = int(input())
B = int(input())
C = int(input())
chet = False
nech = False
if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
    chet = True
if A % 2 != 0 or B % 2 != 0 or C % 2 != 0:
    nech = True
if (nech and chet):
    print('YES')
else:
    print('NO')
