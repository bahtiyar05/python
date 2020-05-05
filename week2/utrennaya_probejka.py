a = int(input())
b = int(input())
day = 1
while True:
    if int(a) >= b:
        print(day)
        break
    a = a + (a * 10) / 100
    day = day + 1
