l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
counter = -1
if (l1 <= l2 and r1 >= l2 and r1 <= r2) or (l2 >= l1 and r2 <= r1) or \
   (l2 <= l1 and l1 <= r2 and r1 <= r2) or \
   (l2 <= l1 and r2 <= r1 and l1 <= r2):
    ml = min(l1, l2)
    mr = max(r1, r2)
    if (ml <= l3 and mr >= l3 and mr <= r3) or (ml <= l3 and mr >= r3) or \
       (l3 <= ml and ml <= r3 and r3 <= mr) or (l3 <= ml and r3 >= mr):
        counter = 0
    elif l3 - r1 <= r2 - l2:
        counter = 2
    else:
        counter = 3
elif (l2 <= l3 and l3 <= r2 and r3 >= r2) or (l2 <= l3 and r3 <= r2) or \
     (l3 <= l2 and l2 <= r3 and r3 >= r2) or \
     (l3 <= l2 and r3 >= r2 and l2 <= r3):
    ml = min(l2, l3)
    mr = max(r2, r3)
    if (ml <= l1 and mr >= l1 and r1 >= mr) or (ml <= l1 and mr >= r1) or \
       (l1 <= ml and ml <= r1 and r1 >= mr) or (l1 <= ml and mr <= r1):
        counter = 0
    else:
        counter = 1
elif (l1 <= l3 and l3 <= r1 and r3 >= r1) or \
     (l1 <= l3 and r3 <= r1) or \
     (l3 <= l1 and l1 <= r3 and r3 >= r1) or \
     (l3 <= l1 and r1 >= r3 and l1 <= r3):
    ml = min(l1, l3)
    mr = max(r1, r3)
    if (ml <= l2 and mr >= l2 and r2 >= mr) or (ml <= l2 and mr >= r2) or \
       (l2 <= ml and ml <= r2 and r2 >= mr) or (l2 <= ml and mr <= r2):
        counter = 0
    else:
        if abs(l2 - r3) <= r1 - l1 or abs(l3 - r2) <= r1 - l1:
            counter = 1
        else:
            counter = 2
elif l1 < l2 and l1 < l3 and l2 < l3 and r1 < l2 and r2 < l3:
    if l3 - r2 <= r1 - l1:
        counter = 1
    elif l2 - r1 <= r3 - l3:
        counter = 3
elif l1 < l2 and l1 < l3 and l3 < l2:
    if l2 - r3 <= r1 - l1:
        counter = 1
    elif (l3 - r1 <= r2 - l2):
        counter = 2
elif l2 < l3 and l2 < l1 and l3 < l1:
    if l3 - r2 <= r1 - l1:
        counter = 1
    elif l1 - r3 <= r2 - l2:
        counter = 2
elif l2 < l1 and l2 < l3 and l1 < l3:
    if l3 - r1 <= r2 - l2:
        counter = 2
    elif l1 - r2 <= r3 - l3:
        counter = 3
elif l3 < l1 and l3 < l2 and l1 < l2:
    if l1 - r3 <= r2 - l2:
        counter = 2
    elif l2 - r1 <= r3 - l3:
        counter = 3
elif l3 < l2 and l3 < l1 and l2 < l1 and r3 < r2 and r3 < 1:
    if l2 - r3 <= r1 - l1:
        counter = 1
    else:
        counter = -1
print(counter)
