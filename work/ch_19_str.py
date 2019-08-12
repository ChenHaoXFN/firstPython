# str 类型的 操作方法
str = "人生苦短，我用python"

# 长度
print(len(str))

# 取值
print(str[2])

# 遍历
for char in str:
    print(char)

# 统计出现的次数
print(str.count("人生"))


str_split = str.split("我")
print(type(str_split))
for s in str_split:
    print(s)

print(str.isalnum())

str.isdecimal()