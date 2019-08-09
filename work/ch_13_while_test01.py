# 使用 while 计算 1+2+3+4+。。。+100
num = 1
result = 0
while num <= 100:
    result += num
    num += 1
print("1加到100的和是 %d " % result)

# 计算 100以内 所有偶数的和
even_num = 1
even_result = 0
while even_num <= 100:
    if even_num % 2 == 0:
        even_result += even_num
    even_num += 1
print("100以内，所有偶数的和为 %d " % even_result)
