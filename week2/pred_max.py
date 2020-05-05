n = int(input())
Max = n
predMax = 0
while n != 0:
    n = int(input())
    if n >= Max:
        predMax = Max
        Max = n
    elif n > predMax or predMax == 0:
        predMax = n
print(predMax)
