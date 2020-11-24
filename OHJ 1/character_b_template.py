"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game.
"""

class Character:
    """
    This class defines what a character is int he game and what
    he or she can do.
    """

    # TODO: copy your Character class implementation from
    #       the previous assignment here and implement the
    #       following new methods.
    #
    #       Also note, that you have to modify at least
    #       __init__ and printout methods to conform with
    #       the new bahavior of the class.
    def __init__(self, name, hp):
        self.__name = name
        self.__items = items = []
        self.__hp = hp

    def get_name(self):
        return self.__name

    def give_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        self.__items.remove(item)

    def has_item(self, item):
        if item in self.__items:
            return True
        else:
            return False

    def how_many(self, item):
        return self.__items.count(item)

    def printout(self):
        esineet = list(dict.fromkeys(self.__items))

        print(f"Name: {self.__name}")
        print(f"Hitpoints: {self.__hp}")

        if self.__items == []:
            print("  --nothing--")

        else:
            for item in sorted(esineet):
                if self.has_item(item):
                    print(f"  {self.how_many(item)} {item}")

                else:
                    print(f"  {item}: none found.")

    def pass_item(self, item, target):
        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is to
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """

        if self.has_item(item):
            target.give_item(item)
            self.__items.remove(item)
            return True

        else:
            return False

    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must be exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """
        if weapon in WEAPONS:
            if self.has_item(weapon):
                if self.__name != target.__name:

                    print(f"{self.__name} attacks {target.__name} delivering {WEAPONS[weapon]} damage.")
                    target.__hp -= WEAPONS[weapon]

                else:
                    print(f"Attack fails: {self.__name} can't attack him/herself.")
            else:
                printti = f"Attack fails: {self.__name} doesn't have "
                print(printti, '"', weapon, '".', sep="")
        else:
            huoh = f"Attack fails: unknown weapon "
            print(huoh, '"', weapon, '".', sep="")

        if target.__hp <=0:
            print(f"{self.__name} successfully defeats {target.__name}.")

WEAPONS = {
    # Weapon          Damage
    #--------------   ------
    "elephant gun":     15,
    "gun":               5,
    "light saber":      50,
    "sword":             7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)


    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()


    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword") # Conan doesn't have a sword.
    conan.attack(conan, "gun")      # A character is not allowed to attack himself.
    conan.attack(conan, "pen")      # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")   # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword") # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")   # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()
