import random

class Hercules:

    def __init__(self):
        self.health_bar = 100
        self.number_of_potions = 5
        self.potion_amount = 20
        self.quick_attack = 20
        self.mega_punch = 30
        self.mega_kick = 35
        self.sword_slash = 40

hercules_attacks = random.choice(quick_attack, mega_punch, mega_kick, sword_slash)

print(hercules_attacks)
