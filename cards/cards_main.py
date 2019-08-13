#! /usr/local/bin/python3


import cards.cards_tools

# 名片管理主程序
# 来一个死循环先
star_str = "*" * 40

while True:
    print(star_str)
    cards.cards_tools.show_menu()
    check_menu = input("请输入您的操作:")
    if check_menu == "1":
        # 查看名片列表
        cards.cards_tools.new_card()
        print(star_str)
    elif check_menu == "2":
        # 查看全部
        cards.cards_tools.get_all_card()
    elif check_menu == "3":
        # 制定查看
        card = cards.cards_tools.get_one_by_name()
        if card is None:
            # 其他操作菜单
            None
        else:
            cards.cards_tools.update_check(card)

    elif check_menu == "0":
        print("谢谢您的使用!!!")
        break
    else:
        print("您的输入有误，请重新输入!")
