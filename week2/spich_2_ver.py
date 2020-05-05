l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
counter = 0
if l1 <= l2 and l1 <= l3 and l2 <= l3 and r1 <= l2 and r2 <= l3:
    if l3 - r2 <= r1 - l1:
        counter = 1
    elif l2 - r1 <= r3 - l3:
        counter = 3
elif l1 <= l2 and l1 <= l3 and l3 <= l2:
    if l2 - r3 <= r1 - l1:
        counter = 1
    elif (l3 - r1 <= r2 - l2):
        counter = 2
elif l2 <= l3 and l2 <= l1 and l3 <= l1:
    if l3 - r2 <= r1 - l1:
        counter = 1
    elif l1 - r3 <= r2 - l2:
        counter = 2
elif l2 <= l1 and l2 <= l3 and l1 <= l3:
    if l3 - r1 <= r2 - l2:
        counter = 2
    elif l1 - r2 <= r3 - l3:
        counter = 3
elif l3 <= l1 and l3 <= l2 and l1 <= l2:
    if l1 - r3 <= r2 - l2:
        counter = 2
    elif l2 - r1 <= r3 - l3:
        counter = 3
elif l3 <= l2 and l3 <= l1 and l2 <= l1:
    if l2 - r3 <= r1 - l1:
        counter = 1
    elif l1 - r2 <= r3 - l3:
        counter = 3
else:
    counter = -1
print(counter)
