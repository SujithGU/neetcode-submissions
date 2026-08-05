class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        self.__health = health
        self.__power_level = power_level
        # TODO: Add the private attributes
    
    def get_health(self):
        return self.__health

    def get_power_level(self):
        return self.__power_level

    # TODO: Add the getter and setter methods
    def set_health(self,health):
        if health <= 100 and health >=0:
            self.__health = health
        elif health > 100:
            print("You can't set the health to more than 100")
        else:
            print("You can't set the health to less than 0")

    def set_power_level(self,power):
        if power <= 10 and power >=1:
            self.__power_level = power
        elif power > 10:
            print("You can't set the power level to more than 10")
        else:
            print("You can't set the power level to less than 1")

super_hero = SuperHero("Batman", 80, 9)

print(super_hero.get_health()) # this should print 80
super_hero.set_health(110) # this should print You can't set the health to more than 100
super_hero.set_health(-10) # this should print You can't set the health to less than 100
super_hero.set_health(70)

print(super_hero.get_power_level()) # this should print 9
super_hero.set_power_level(11) # this should print You can't set the power level to more than 10
super_hero.set_power_level(0) # this should print You can't set the power level to less than 1
super_hero.set_power_level(7)



# TODO: print the hero's attributes
print(f'{super_hero.name} has {super_hero.get_health()} health and {super_hero.get_power_level()} power level')
