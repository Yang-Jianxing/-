#第二题
a = input("请输入一个年份：")
a = int(a)
if a%100==0 and a%400==0:
    print("这是个闰年")
else:
    print("这不是闰年")