n = int(input())
max = n
sani = 1
while n != 0:
    n = int(input())
    if n > max:
        max = n
        sani = 1
    elif n == max:
        sani += 1
print(sani)
