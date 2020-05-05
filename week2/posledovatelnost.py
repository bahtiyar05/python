n = int(input())
maks = 0
rez1 = 0
rez2 = 1
var = n
while n != 0:
    n = int(input())
    if n == var:
        rez2 = rez2 + 1
    if n != var:
        var = n
        if(rez2 > rez1):
            rez1 = rez2
            rez2 = 1
        if rez1 >= rez2:
            rez2 = 1
    if maks < rez1:
        maks = rez1
print(maks)
