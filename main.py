from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализация конкретных типов оружия
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")

class MagicWand(Weapon):  # Дополнительное оружие, демонстрирующее расширяемость
    def attack(self):
        print("Боец выпускает магический заряд из волшебной палочки.")

# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает новое оружие.")

    def attack(self):
        self.weapon.attack()

# Класс Monster для демонстрации боя
class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"Монстр {self.name} побежден!")

# Шаг 4: Реализация боя
def battle(fighter: Fighter, monster: Monster):
    print(f"{fighter.name} начинает бой с монстром {monster.name}.")
    fighter.attack()
    monster.defeat()

# Демонстрация
if __name__ == "__main__":
    # Создание бойца и монстра
    monster = Monster("Гоблин")
    fighter = Fighter("Герой", Sword())

    # Бой с использованием меча
    battle(fighter, monster)

    # Смена оружия на лук
    fighter.change_weapon(Bow())
    battle(fighter, monster)

    # Смена оружия на волшебную палочку
    fighter.change_weapon(MagicWand())
    battle(fighter, monster)
