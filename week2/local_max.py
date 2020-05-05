prev_i = 0
now_i = 0
prev_num = int(input())
now_num = int(input())
next_num = int(input())
min = 0
if (prev_num != 0) and (now_num != 0):
    i = 2
    while next_num != 0:
        if (now_num > prev_num) and (now_num > next_num):
            prev_i = now_i
            now_i = i
        if (min == 0) and prev_i != 0:
            min = now_i - prev_i
        elif now_i - prev_i < min:
            min = now_i - prev_i
        result = min
        i += 1
        prev_num = now_num
        now_num = next_num
        next_num = int(input())
print(result)
