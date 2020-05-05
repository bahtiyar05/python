N = int(input())
s = str((N // 100)).zfill(2)
e = (int(s[0]) == 0) * int(s[1]) * 10
f = int(s[0] != 0) * int(s)
g = str(N % 100).zfill(2)
g1 = (int(g[1]) == 0) * int(g[0]) * 10
g2 = int(g[1] != 0) * int(g[1]) * 10 + int(g[0])
print((int(e + f) == int(g1 + g2)) * 1)
