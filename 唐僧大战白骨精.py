# 创建变量，用来存放游戏中的人物名字
namet = "唐僧"
nameb = "白骨精"
# 显示欢迎信息
print(f'"="*20, "欢迎光临《{namet}大战{nameb}》", "="*20')
# 显示身份选择的信息
print("请选择你的身份：")
print(f"\t1.{namet}")
print(f"\t2.{nameb}")
# 打印一条分界线
print("="*64)
# 游戏的身份选择
game_choose = input("请选择[1-2]:")
# 根据用户的选择来显示不同的提示信息
if game_choose == "1":
    print(f"\t你已经选择了1，你将以‘{namet}’的身份来进行游戏！")
elif game_choose == "2":
    print(f"\t你竟然选择了{nameb}，真他妈不要脸，你将以‘{namet}’的身份来进行游戏!")
else:
    print(f"你的输入不合法，系统将自动分配身份，你将以‘{namet}’的身份来进行游戏!")

# 进入游戏
# 首先创建变量，来存放玩家的生命值和攻击力
player_life = 2  # 生命值
player_attack = 2  #攻击力

# 创建变量，来存放boss的生命值和攻击力
boss_life = 10  # 生命值
boss_attack = 10  #攻击力
# 打印一条分界线
print("="*64)
# 显示玩家的信息（生命值，攻击力）
print(f"{namet}，你的生命值是 {player_life} ,攻击力是 {player_attack}")
# 由于游戏选项是反复显示的，所以用一个循环来控制
while True:
    # 打印一条分界线
    print("=" * 64)
    # 显示游戏选项，游戏正式开始
    print("请选择你要进行操作：")
    print("\t1.练级")
    print("\t2.打boss")
    print("\t3.逃跑")
    player_choose = input("请选择要做的操作[1-3]")
    # 处理用户的选择
    if player_choose == "1":
        # 增加玩家的生命值和攻击力
        player_life += 2
        player_attack += 2
        # 显示最新的消息
        # 打印一条分界线
        print("=" * 64)
        # 显示玩家的信息（生命值，攻击力）
        print(f"{namet}，你的生命值是 {player_life} ,攻击力是 {player_attack}")
    elif player_choose == "2":
        # 玩家攻击boss
        #减去boss的生命值，减去的生命值等于玩家的攻击力
        boss_life -= player_attack
        # 打印一条分界线
        print("=" * 64)
        print(f"‘{namet}‘ 攻击了 ’{nameb}’")
        # 打印一条分界线
        print("=" * 64)
        #判断boss是否死亡
        if boss_life <= 0:
            #boss死亡，玩家胜利，游戏结束
            print(f"‘{nameb}’受到了{player_attack}点伤害，重伤不知死了，‘{namet}取得了胜利’")
            #游戏结束
            break
        # boss反击玩家
        # 减去b玩家的生命值，减去的生命值等于boss的攻击力
        player_life -= boss_attack
        # 判断玩家是否死亡
        if player_life <= 0:
            # 玩家死亡，boss取得了胜利，游戏结束
            print(f"‘{namet}’受到了{boss_attack}点伤害，重伤不知死了，‘{nameb}取得了胜利’")
            # 游戏结束
            break
    elif player_choose == "3":
        # 打印一条分界线
        print("=" * 64)
        print(f"{namet}一看打不过{nameb}，一扭头跑了，{nameb}大喊一声，玉帝哥哥来呀，说快活呀，反正有大把时光！")
    else:
        # 打印一条分界线
        print("=" * 64)
        print("你的输入不合法，请重新输入")






