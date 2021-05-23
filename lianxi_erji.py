"""
# 第一个问题
import jieba

o = open('新建文本文档.txt', 'r', encoding='utf-8')
print(o.read())
o.close()

# 上面的方法不太完美，下面的方法还不错。
with open('新建文本文档.txt', 'r', encoding='utf-8') as o:
    print(o.read())

# 第二个问题
s = input(":")
s = s.replace('，', '').replace('。', '').replace('!', '')
m = len(s)
print('{}'.format(m))
"""
# # 第三个问题
# print(chr(97))
# print(ord('a'))
#
# 4, Fibonacci数列
# n = int(input('请输入一个整数：'))
# F1, F2 = 1, 1
# for i in range(3, n + 1):
#     F1, F2 = F2 % 10007, (F1+F2) % 10007
# print(F2)

# 5， 计算圆的面积
# import math
# r = int(input('请输入圆的半径：'))
# p = math.pi
# s = p*(r**2)
# print('圆的面积为：{:.7f}'.format(s))

# 6， 计算1+2+3+...+n的值, 等差数列求和
# n = eval(input('n:'))
# s = (0.5*n*n)+(0.5*n)
# print(s)
'''
7，A+B问题,不会！

'''

# c = map(lambda a, b: a+b)
# print(c)

# 8，选取1--2020有多少个2.
# ans = 0
# for i in range(1, 2021):
#     ans += (str(i).count('2'))
# print(ans)

# 9.递归数列
# def rec(num):
#     if num == 1 or num == 2:
#         return 1
#     return rec(num - 1) + rec(num - 2)
#
#
# for i in range(1, 21):
#     print(rec(i), end='\t')
import turtle as t
t.penup()
t.pendown()
for i in range(5):
    t.seth(35)
    t.forward(50)
