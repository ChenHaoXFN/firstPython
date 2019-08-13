# 名片处理工具类
star_str = "*" * 40


def show_menu():
    # 定义一个 菜单
    # 目录
    print("欢迎来到【python—>名片管理系统】")
    print("1、新建名片")
    print("2、显示全部")
    print("3、查看名片")
    print("")
    print("0、退出系统")
    # 分隔符
    print(star_str)


# 定义用来存储所有名片的列表
card_list = []


# 定义用来存名片信息的字典


def new_card():
    # 新建名片
    name_str = input("请输入姓名")
    age_str = input("请输入年龄")
    sex_str = input("请输入性别")
    phone_str = input("请输入手机号")
    qq_str = input("请输入qq")
    card_dir = {"name": name_str, "age": age_str, "sex": sex_str, "phone": phone_str, "qq": qq_str}
    card_list.append(card_dir)
    print("%s 的名片添加成功!" % name_str)


def get_all_card():
    # 查看所有名片
    if len(card_list) == 0:
        print("您还没有添加过任何名片！请先添加名片！")
    else:
        for pro in ["名字", "年龄", "性别", "手机号", "qq"]:
            print(pro, end="\t\t")
        print("")
        print("-" * 50)
        for card in card_list:
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s" % (
                card["name"], card["age"], card["sex"], card["phone"], card["qq"]))
    print(star_str)


def update_card(card):
    card_list.remove(card)
    # 修改操作
    new_name = input("你想修改为：（回车不修改）")
    new_age = input("你想修改为：（回车不修改）")
    new_sex = input("你想修改为：（回车不修改）")
    new_phone = input("你想修改为：（回车不修改）")
    new_qq = input("你想修改为：（回车不修改）")
    card["name"] = new_name if new_name != "" else None
    card["age"] = new_age if new_age != "" else None
    card["sex"] = new_sex if new_sex != "" else None
    card["phone"] = new_phone if new_phone != "" else None
    card["qq"] = new_qq if new_qq != "" else None
    print("%s 修改完毕" % card["name"])
    card_list.append(card)


def del_card(card):
    enter = input("确认删除吗？Y/N:")
    if enter.upper() == "Y":
        print("%s 已经删除！" % card["name"])
        card_list.remove(card)
    else:
        None


def update_check(card):
    # 修改选项
    check = input("您想对该名片进行什么操作：1、修改；2、删除；3、退出：")
    if check == "1":
        update_card(card)
    elif check == "2":
        del_card(card)
    elif check == "3":
        None
    else:
        print("您输入有误，请重新开始！")


def get_one_by_name():
    # 根据名字查询
    query_name = input("请输入想查询的名字:")
    for card in card_list:
        if card["name"] == query_name:
            for pro in ["名字", "年龄", "性别", "手机号", "qq"]:
                print(pro, end="\t\t")
            print("")
            print("-" * 50)
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s" %
                  (card["name"], card["age"], card["sex"], card["phone"], card["qq"]))
            return card;
    else:
        print("没有找到对应的名片！")
        print("-" * 50)
        return None
