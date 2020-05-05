A = int(input())
B = int(input())
C = ((A % B) == 0) * 1
D = ((A % B) != 0) * 1
print('YES'*C, 'NO'*D, sep='')
