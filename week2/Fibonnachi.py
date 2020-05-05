n = int(input())
f0 = 0
f1 = 1
k = 2
fn = 0
if n == 0:
    fn = 0
elif n == 1:
    fn = 1
elif n >= 2:
    while k <= n:
        fn = f1 + f0
        (f0,f1) = (f1,fn)
        k = k + 1
print(fn)
