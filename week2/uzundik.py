C = int(input())
B=C
e=1
r=B
polyndrom = True
s=str(C)
i=0
l=len(s)-1
print(l)

while i <= len(s)/2:
    if s[i]!=s[l]:
        polyndrom = False
        break
    i = i + 1
    l = l - 1
if polyndrom:
    print(s)
    

'''
while r // 10 != 0 and r >= 10:
            e = e * 10
            r = r // 10
print(e)
polyndrom = True
while B >= 10:
    c = B // e
    d = B % 10
    if c != d :
        polyndrom = False
        break
    B = B - B // e * e 
    B = B % 10
    e = e // 10
if (polyndrom == True):
    print(C)
'''
