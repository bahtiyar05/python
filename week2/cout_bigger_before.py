counter = 0
n = int(input())
pred = n
while n != 0:
    n = int(input())
    if n > pred:
        counter += 1
    pred = n
print(counter)
