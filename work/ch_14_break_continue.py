# 使用 break 跳出循环
num = 0
while num <= 100:
    num += 1
    print(num)
    if num == 5:
        break

print(num)

# 使用 continue 继续执行
i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        print(i)
