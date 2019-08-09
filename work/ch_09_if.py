# 基本 if 语法

str_age = input("请输入您的年龄:")
num_age = int(str_age)

if num_age >= 18:
    print("你是成年人了！")
else:
    print("滚犊子~~~~")

python_score = int(input("请输入python的成绩: "))
java_score = int(input("请输入java的成绩："))

if python_score >= 60 and java_score >= 60:
    print("不错，继续加油！！")
elif python_score >= 60 or java_score >= 60:
    print("才一个及格啊？？？还得努力")
else:
    print("傻逼玩意儿~~~~")

if not (python_score > 60):
    print("呵呵哒")

if python_score >= 60:
    if java_score >= 60:
        print("勉强及格")
