class Hercules:

    def __init__(self):
        self.health_bar = 100
        self.number_of_potions = 5
        self.potion_amount = 20
        self.quick_attack = 20
        self.mega_punch = 30
        self.mega_kick = 35
        self.sword_slash = 40

    def hercules_uses_potion(self, use_potion):
        self.health_bar += use_potion