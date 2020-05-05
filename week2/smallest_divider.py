n = int(input())
k = 2
while k <= n:
    if n % k == 0:
        print(k)
        break
    k = k + 1
