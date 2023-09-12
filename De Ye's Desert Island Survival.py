import random

# 定义玩家的属性
player = {
    "name": "Bear Grylls",
    "health": 100,
    "hydration": 100,
    "food": 100
}

# 定义游戏中可能遇到的事件和场景
events = [
    "你找到了一些干净的河水，补充了水分。",
    "你捕捉到了一只野兔，获得了食物。",
    "你迷路了，走了很长时间，消耗了一些食物和水。",
    "你遇到了一只威胁你的野生动物，受伤了。",
    "你找到了一个干草堆，可以用来取暖。",
    "你发现了一个遗弃的帐篷，里面有一些食物和水。",
    "你成功搭建了一个避难所，休息了一晚，恢复了健康。"
]

def game_over():
    print("\n游戏结束，你的德爷荒野求生之旅结束了。")
    print(f"最终状态：")
    print(f"健康：{player['health']}")
    print(f"水分：{player['hydration']}")
    print(f"食物：{player['food']}")

def main():
    print("欢迎来到德爷荒野求生游戏！")
    print("你是德爷，被空投到了一个荒野地区。")
    print("你必须管理你的健康、水分和食物来生存。")

    while player["health"] > 0:
        print("\n选择一个行动：")
        print("1. 寻找水源")
        print("2. 寻找食物")
        print("3. 建造庇护所")
        print("4. 查看状态")
        print("5. 退出游戏")

        choice = input("请输入选项的数字：")

        if choice == "1":
            event = random.choice(events)
            print(event)
            if "水分" in event:
                player["hydration"] += random.randint(10, 20)
        elif choice == "2":
            event = random.choice(events)
            print(event)
            if "食物" in event:
                player["food"] += random.randint(10, 20)
        elif choice == "3":
            event = random.choice(events)
            print(event)
            if "庇护所" in event:
                player["health"] += random.randint(10, 20)
        elif choice == "4":
            print(f"\n状态：")
            print(f"健康：{player['health']}")
            print(f"水分：{player['hydration']}")
            print(f"食物：{player['food']}")
        elif choice == "5":
            game_over()
            break
        else:
            print("无效的选项，请重新选择。")

        # 更新玩家状态
        player["health"] -= random.randint(5, 15)
        player["hydration"] -= random.randint(5, 15)
        player["food"] -= random.randint(5, 15)

        # 检查玩家是否死亡
        if player["hydration"] <= 0 or player["food"] <= 0:
            print("你死亡了，德爷的荒野求生之旅结束了。")
            game_over()
            break

if __name__ == "__main__":
    main()
