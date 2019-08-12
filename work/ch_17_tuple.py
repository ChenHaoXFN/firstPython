# Tuple 元组，一旦定义完成，不允许修改
arr = ("a", "b", 1)

print(type(arr))

print(arr.count(1))
print(len(arr))

print(arr.index(1))

# 元组跟列表相互转换
arr_list = list(arr)
print(type(arr_list))

arr_list.append("zzk")
list_tuple = tuple(arr_list)
print(type(list_tuple))
