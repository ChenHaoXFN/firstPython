# str 更多方法
num = "12"

print(num.isdecimal())

print(num.isdigit())

print(num.isnumeric())

# replace 方法
str = "saadasd"
str_rep = str.replace("sa", "ssssss")
print(str_rep)

# 对其文本
tump = ["登鹳全楼", "\n王之涣", "白日依山尽", "\t\t黄河入海流", "欲穷千里目", "更上两层楼"]
# 居中对其
for tump_str in tump:
    print("|%s|" % tump_str.strip().center(10, "　"))

for tump_str in tump:
    print("|%s|" % tump_str.ljust(10))

num_str = "123456789"
print(num_str[3:6])

print(num_str[3:])

print(num_str[0:6])

print(num_str[:6])

print(num_str[:])
# 隔一个切割
print(num_str[::2])

print(num_str[::3])

print(num_str[-1::-1])

print(num_str[::-1])