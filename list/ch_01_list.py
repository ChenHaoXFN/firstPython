name_list = ["张三", "李四", "王五"]
extend_list = ["zzk", "ch"]
print(name_list)

# 1、list 的 append 方法，向队列中新增数据
name_list.append("赵六")
print(name_list)

# 2、list 的 count 方法, 统计数据出现的次数
list_count = name_list.count("李四")
print(list_count)

# 3、list 的 insert 方法，在对应下小标处添加数据
name_list.insert(2, "陈七")
print(name_list)

# 4、list 的 remove 方法，删除对应数据
name_list.remove("陈七")
print("删除后的列表 ", name_list)

# 5、list 的 copy 方法，复制
copy_list = name_list.copy()
print("复制后的list为", copy_list)

# 6、指定数据的 坐标
indexw = name_list.index("王五")
print(indexw)

# 7、将一个列表的所有数据添加到本list
name_list.extend(extend_list)
print(name_list)

# 8、pop 删除该坐标的元素
name_list.pop(2)
print(name_list)

name_list_length = len(name_list)
print(name_list_length)
print("-" * 10)
# 翻转整个list
name_list.reverse()
print(name_list)

print("-" * 10)

name_list.sort()
print(name_list)

print("-" * 10)
name_list.sort(reverse=True)
print(name_list)

# 、list 的 clear 方法，清空整个列表
name_list.clear()
print(name_list)
