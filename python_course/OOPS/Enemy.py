class Enemy:
    # this is parameterized constructor
    def __init__(self, type_of_enemy, health_points, damage_attack):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.damage_attack = damage_attack
        print(f"enemy is none other than {self.type_of_enemy} and he has health of {self.health_points} and can do a damage of {self.damage_attack}")

    # this is basically the default/e,pty constructor
    # def __init__(self):
    #     print("I'm basically a default constructor")

    # self refers to the current class / object
    # def talk(self):
    #     print(f"I an enemy of type {self.type_of_enemy}")

    # def walk_forward(self):
    #     print(f"I am having health points of {self.health_points}")



