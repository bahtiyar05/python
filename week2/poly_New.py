A = int(input())
B = 11
counter = 0
if A < 10:
    print(1)
else:
    while B <= A:
        polyndrom = True
        e = 0
        F = str(B)
        l = len(F) - 1
        while e <= len(F)/2:
            if F[e] != F[l]:
                polyndrom = False
                break
            e = e + 1
            l = l - 1
        if (polyndrom):
            counter += 1
        B += 1
    print(counter + 9)
