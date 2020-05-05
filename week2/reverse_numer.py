A = int(input())
B = 0
while A >= 0:
    if A > 9:
        c = A % 10
        A = A // 10
        if c == 0 and B == 0:
            B = c
        else:
            B = B * 10 + c
    else:
        B = B * 10 + A
        A = A - A
        break
print(B)
