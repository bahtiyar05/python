A = int(input())
B = 11
counter = 0
if A < 10:
    print(1)
else:
    while B <= A:
        polyndrom = True
        e = 1
        r = B
        F = B
        while r // 10 != 0 and r >= 10:
            e = e * 10
            r = r // 10
        while F >= 10:
            c = F // e
            d = F % 10
            if c != d:
                polyndrom = False
                break
            F = F - F // e * e
            F = F % 10
            e = e // 10
        if (polyndrom):
            counter += 1
        B += 1
    print(counter + 9)
