import pandas as pd

data = pd.read_excel('F:/1.xls')

data_gender = data[
    ['学生姓名', '身份证件类型', '身份证件号', '考生号', '学号', '性别', '出生日期', '政治面貌', '民族', '学生类型', '学习形式', '院系名称', '年级', '班级', '专业大类',
     '专业', '攻读学历', '学制', '入学日期', '是否农村学生']]
data_gender_re = data_gender[data_gender.notnull()]

FF = data_gender_re.loc[(data_gender_re['班级'] == '20电子信息工程2班')]
print(data_gender_re.loc[(data_gender_re['班级'] == '20电子信息工程2班')])

FF.to_excel('F:\\2.xls', index=False, encoding='gbk')
