# 字典类型 大括号
map = {"name": "zzk", "age": 18, "sex": "man"}
print(type(map))

# 取值
print(map.values())
map_name = map.get("name")
print(map_name)
map_keys = map.keys()
print(map_keys)
print(type(map["age"]))
map_age = map["age"]
print(map_age)

# 新增
# 修改

# 如果对应 key 存在，修改，不存在添加
map["2"] = 5
print(map)

map["age"] = 66
print(map)

# 删除
map.pop("age")
print(map)

# 统计数量
print(len(map))

# 合并 dictionary
new_map = {"phone": 139202020}
map.update(new_map)
print(map)

# 清空
# map.clear()
print(map)

# 遍历
for item in map:
    print(item, end="---")
    print(map.get(item))
