import random

# 剪刀石头布
# 假设 1 是剪刀，剪刀胜布
# 假设 2 是石头，石头胜剪刀
# 假设 3 是布，布胜石头
flag_gamer = int(input("石头剪刀布，请输入（1->剪刀，2->石头，3->布）："))

flag_computer = int(random.randint(1, 3))

computer_win = "电脑胜利~~~~"
gamer_win = "玩家胜利~~~~"

print("您出的是剪刀" if flag_gamer == 1 else "您出的是是石头" if flag_gamer == 2 else "您出的是布")
print("电脑出的是剪刀" if flag_computer == 1 else "电脑出的是是石头" if flag_computer == 2 else "电脑出的是布")

# 开始判断输赢
if flag_computer == flag_gamer:
    print("平局~~~~~")
#  如果玩家出的剪刀
elif flag_gamer == 1:
    if flag_computer == 2:
        print(computer_win)
    else:
        print(gamer_win)

#  如果玩家出的石头
elif flag_gamer == 2:
    if flag_computer == 1:
        print(gamer_win)
    else:
        print(computer_win)

# 如果玩家出的布
else:
    if flag_computer == 1:
        print(computer_win)
    else:
        print(gamer_win)

