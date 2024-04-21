class character:
    def __init__(self, damage, speed, health):
        self.damage=damage
        self.speed=speed
        self.health=health

warrior= character(25, 40, 70)
print(warrior.speed)