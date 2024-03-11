class Archer:
    def __init__(self, hp, mana, arrows):
        self.hp = hp
        self.mana = mana
        self._arrows = arrows
    def walk(self):
        print(f"Ich bin {self} und laufe")
        
    def shoot(self):
        if self._arrows > 0:
            self._arrows -= 1
            print(f"Bogenschütze hat geschossen, noch {self._arrows} überig.")
        else:
            print("Bogenschütze hat keine Pfeile mehr.")
    
archer1 = Archer(90, 10, 3)
archer2 = Archer(100, 0, 3)
print(archer1.hp)

archer2.arrows = 0
archer2.shoot()