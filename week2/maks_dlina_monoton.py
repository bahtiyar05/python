n = int(input())
rez1 = 1
rez2 = 1
var = n
b = 1
c = 1
e = 1
f = 1
while n != 0:
    n = int(input())
    if n == 0:
        break
    elif n > var:
        rez1 = rez1 + 1
        rez2 = 1
        var = n
        if rez1 > b:
            c = b
            b = rez1
    elif n < var:
        rez2 = rez2 + 1
        rez1 = 1
        var = n
        if rez2 > e:
            f = e
            e = rez2
    elif n == var:
        rez1 = 1
        rez2 = 1
        var = n
print(max(b, e))
