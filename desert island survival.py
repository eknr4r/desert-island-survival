import time
import random

class Player:
    def __init__(self, name, difficulty):
        self.name = name
        self.health = 100
        self.hunger = 100
        self.thirst = 100
        self.difficulty = difficulty

    def eat(self):
        self.hunger = min(100, self.hunger + random.randint(10, 20))

    def drink(self):
        self.thirst = min(100, self.thirst + random.randint(10, 20))

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_status(player):
    print(f"\n{name}生命值：{player.health}  饥饿度：{player.hunger}  口渴度：{player.thirst}")

def choose_difficulty():
    print("\n请选择难度：")
    print("1. 简单")
    print("2. 普通")
    print("3. 困难")
    while True:
        try:
            choice = int(input("请输入难度等级（1/2/3）："))
            if 1 <= choice <= 3:
                return choice
            else:
                print("无效的选择，请重新输入。")
        except ValueError:
            print("无效的输入，请重新输入。")

def explore(player):
    delay_print("\n你身处荒岛，周围是茂密的丛林。")
    encounter = random.choice(["food", "water", "danger", "nothing"])
    
    if encounter == "food":
        collect_food(player)
    elif encounter == "water":
        collect_water(player)
    elif encounter == "danger":
        danger_encounter(player)
    else:
        delay_print("这片区域看起来平静无事。")

def collect_food(player):
    food_amount = random.randint(10, 30)
    player.hunger = min(100, player.hunger + food_amount)
    delay_print(f"你发现了{food_amount}个食物，填饱了肚子。")

def collect_water(player):
    water_amount = random.randint(10, 30)
    player.thirst = min(100, player.thirst + water_amount)
    delay_print(f"你找到了{water_amount}份水，解渴了。")

def danger_encounter(player):
    damage = random.randint(10, 30)
    player.take_damage(damage)
    delay_print("你遭遇了危险！")
    delay_print(f"你受到了{damage}点伤害，需要及时处理伤势。")

def play_game():
    player_name = input("请输入你的名字：")
    difficulty_choice = choose_difficulty()
    difficulty = ["简单", "普通", "困难"][difficulty_choice - 1]
    player = Player(player_name, difficulty)
    
    delay_print(f"欢迎来到荒岛求生游戏，{player_name}！")
    delay_print(f"你选择了{difficulty}难度，将在荒岛上展开求生之旅。")

    while True:
        show_status(player)
        action = input("你可以前往未知的区域探险（输入“探险”）或者进行食物/水的补给（输入“吃饭”或“喝水”）：").lower()
        
        if action == "探险":
            explore(player)
        elif action == "吃饭":
            player.eat()
            delay_print("你进食了一些食物，填饱了肚子。")
        elif action == "喝水":
            player.drink()
            delay_print("你喝了一些水，解渴了。")
        else:
            delay_print("无效的输入，请重新输入。")

if __name__ == "__main__":
    play_game()
