class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    
    def hit(self, target):
        print(f"{self.name} hits {target.name}")
        target.take_damage(self.attack)

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Health is now {self.health}")

class Boss(Character):
    def __init__(self, name, health, attack, energy):
        super().__init__(name, health, attack)
        #super() function refers to the parent class, it call method like __init__ from a superclass/base class without directly naming it
        #We call the parent Character’s __init__ method to reuse code
        self.energy = energy
    
    def special_hit(self, target):
        if self.energy >= 20:
            print(f"{self.name} does a special attack on {target.name}")
            target.take_damage(30)
            self.energy -= 20
            print(f"{self.name} now has {self.energy} energy")
        else:
            print(f"{self.name} doesn't have enough energy for a speical attack")


playerName = str(input("Enter player's name: "))

player = Character(playerName, 100, 10)
globin = Character("Globin", 50, 5)
bigGlobin = Boss("Big Globin", 150, 15, 40)

player.hit(globin)
print("_ _ _")

globin.hit(player)
print("_ _ _")


bigGlobin.hit(player)
print("_ _ _")
bigGlobin.special_hit(player)
print("_ _ _")
bigGlobin.special_hit(player)
print("_ _ _")
bigGlobin.special_hit(player)

