#第三题
print("根据够的年龄算出您的大概年龄")
a = input("请输入您的狗的年龄：")
a = float(a)
if 0<a<=2:
    print(a*10.5)
elif a>2:
    print(21+(a-2)*4)
elif a<=0:
    print("您输入的数字有误！")