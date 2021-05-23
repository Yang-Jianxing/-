def rec(num):
    if num == 1 or num == 2:
        return 1
    return rec(num - 1) + rec(num - 2)


for i in range(1, 21):
    print(rec(i), end='\t')
