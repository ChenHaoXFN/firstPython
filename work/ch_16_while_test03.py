# -*- coding: UTF-8 -*-
# 求100 以内所有能被3 整除但不能被5 整除的数字的和
hundred_i = 1
hundred_sum = 0
while hundred_i <= 100:
    if hundred_i % 3 == 0 and hundred_i % 5 != 0:
        hundred_sum += hundred_i
    hundred_i += 1
print("100以内 能被3整除，但是不能被5整除的数的和为 %d " % hundred_sum)

# “百钱买百鸡”是我国古代的著名数学题。题目这样描述：
# 3 文钱可以买1只公鸡，
# 2 文钱可以买一只母鸡
# 1 文钱可以买3 只小鸡。
# 用100 文钱买100 只鸡，那么各有公鸡、母鸡、小鸡多少只？
chicken_xiao = 0
chicken_mu = 0
chicken_gong = 0

# while chicken_xiao<=100:
for chicken_gong in range(1, 33):
    for chicken_mu in range(1, 50):
        chicken_xiao = 100 - chicken_mu - chicken_gong
        if chicken_mu + chicken_xiao + chicken_gong == 100 and (
                chicken_mu * 2 + chicken_gong * 3 + chicken_xiao) == 100:
            print(11111)

# 搬砖问题：36 块砖，36 人搬，男搬4，女搬3，两个小孩抬1 砖，要求一次
# 全搬完，问男、女和小孩各若干？


# *编程找出四位整数abcd 中满足下述关系的数。
# (ab+cd)*(ab+cd)=abcd
for flow_num in range(1000, 9999, 1):
    ab = flow_num // 100
    cd = flow_num % 100
    if (ab + cd) * (ab + cd) == flow_num:
        print(flow_num)

print("----" * 5)
# **求水仙花数。所谓水仙花数，是指一个三位数abc，如果满足a3+b3+c3=abc，
# 则abc 是水仙花数。
for water_num in range(100, 999):
    water_a = water_num // 100
    water_b = water_num % 100 // 10
    water_c = water_num % 10
    if (3 * water_a + 3 * water_b + 3 * water_c) == water_num:
        print(water_num)

print("----" * 5)
# **输入一个整数，计算它各位上数字的和。（注意：是任意位的整数）


# 13. （循环）**输入一整数A，判断它是否质数。
# 提示1：若从2 到A 的平方根的范围内，没有一个数能整除A，则A 是质数。
# 提示2：在java 中计算n 的平方根可以使用Math.sqrt(n)

# 环）**如果一个数等于其所有因子之和,我们就称这个数为"完数",例如 6 的因子为1,2,3 6=1+2+3 6 就是一个完数.请编程打印出1000 以内所有的完数


# 中国古代数学家研究出了计算圆周率最简单的办法:
# PI=4/1-4/3+4/5-4/7+4/9-4/11+4/13-4/15+4/17......
# 这个算式的结果会无限接近于圆周率的值,我国古代数学家祖冲之计算出,圆周率在
# 3.1415926 和3.1415927 之间,请编程计算,要想得到这样的结果,他要经过多少次加减法运算?


# 读入一个小于10 的整数n，输出它的阶乘n!
num = int(input("请输入一个小于10的数字："))
while num <= 0 or num > 10:
    num = int(input("输入数字不正确,请重新输入:"))
factorial_num = 1
factorial_i = 1
factorial_sum = 1
i = num
while factorial_num <= num:
    factorial_sum *= num
    factorial_num += 1
    num -= 1
print("%d 的阶乘等于 %d " % (i, factorial_sum))
