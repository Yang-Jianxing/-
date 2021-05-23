# # TempConvert.py
# TempStr = input("请输入带有符号的温度值：")
# if TempStr[-1] in ["F", "f"]:
#     C = (eval(TempStr[0:-1]) - 32) / 1.8
#     print("转换后的温度是{:.2f}C".format(C))
# elif TempStr[-1] in ["C", "c"]:
#     F = 1.8 * eval(TempStr[0:-1]) + 32
#     print("转换后的温度是{:.2f}F".format(F))
# else:
#     print("输入格式错误")
# password = 211314
# i = 1
# while i < 10:
#     num = int(input("请输入开机密码："))
#     if num == password:
#         print("正在进入系统：")
#         i = 10
#     else:
#         print("密码错误" + str(i) + "次，请重新输入！")
#         i += 1
# if i == 10:
#     print("手机正在恢复出厂设置！")
# a = input("请输入一个多位数：")
a = 123
print(format(a))
