n = int(input())
f0 = 0
f1 = 1
chislo = -1
if n == 0:
    chislo = 1
elif n == 1:
    chislo = 2
elif n == 2:
    chislo = 3
else:
    k = 2
    while k <= n:
        fn = f0 + f1
        f0 = f1
        f1 = fn
        if fn == n:
            chislo = k
            break
        k += 1
print(chislo)
