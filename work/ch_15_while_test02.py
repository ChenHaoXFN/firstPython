# while 练习2
# 打印小星星，第一排一个，第二排两个，以此类推，打印五排

i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("-" * 20)

a = 1
b = 1
while a <= 5:
    while b <= a:
        print("*", end="")
        b += 1
    a += 1
    b = 1
    print("")

print("-" * 20)

# 输出 99 乘法表
row = 1  # 记录行
col = 1  # 记录列

while col <= 9:
    while row <= col:
        print(" %d * %d = %d  \t" % (row, col, col * row), end="")
        row += 1
    print("")
    col += 1
    row = 1
