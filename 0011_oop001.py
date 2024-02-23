class Archer:
    def __init__(self, hp, mana, arrows):
        self.hp = hp
        self.mana = mana
        self._arrows = arrows
    
    def walk(self):
        print(f"Ich bin {self} und laufe")
    
    def shoot(self):
        if self._arrows > 1:
            self._arrows -= 1
            print(f"Bogenschütze hat geschossen, hat noch {self._arrows} Pfeil übrig.")
        else:
            print("Bogenschütze hat keine Pfeile mehr.")
archer1 = Archer(100, 0, 3)
archer2 = Archer(90, 10, 3)
print(archer1.hp)
print(type(archer1.__dict__))

archer1.walk()
archer2.shoot()
archer2.shoot()
archer2.shoot()
archer2.shoot()
# Wenn ein Atribut mit einem _ gekenntzeichnet ist,
# dann bitte dieses niemals direkt manipulieren,
# sondern nur über eine Funktion.