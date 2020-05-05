n = int(input())
s = 0
b = False
while s <= n:
    t = 1
    k = 0
    while k < s:
        t = t * 2
        k = k + 1
    if (t == n):
        b = True
        break
    s = s + 1
if b:
    print('YES')
else:
    print('NO')
