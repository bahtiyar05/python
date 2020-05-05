N = int(input())
print((N // 3600) % 24, ':', str((N // 60) % 60).zfill(2),
      ':', str(N % 60).zfill(2), sep='')
