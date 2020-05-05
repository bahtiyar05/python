n = int(input())
s = 0
while s <= n:
    t = 1
    k = 0
    while k < s:
        t = t * 2
        k = k + 1
    if (t >= n):
        print(k)
        break
    s = s + 1
