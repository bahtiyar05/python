N = int(input())
i = 1
while i <= N:
    if (i ** 2) <= N:
        print(i ** 2, end=' ')
    else:
        break
    i = i + 1
