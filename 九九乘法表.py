for i in range(1, 10):
    for j in range(1, i+1):
        # print('%dX%d=%d' % (j, i, i*j), end=' ')  # 第一种输出
        print('{}X{}={}\t'.format(j, i, i*j), end='')  # 第二种输出
    print()
