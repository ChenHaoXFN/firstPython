def multiple_table():
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
