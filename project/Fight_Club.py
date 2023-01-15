

class Hero:
    def person(name, age):
        print(f"Имя {name}, Возраст {age}")
        return name, age

    def fight(damage, armor, health):
        print(f"Сила - {damage}\nБроня - {armor}\nЗдоровье - {health}")
        return damage, armor, health

dima = Hero
name, age = dima.person('Демон', 78)
damage, armor, health = dima.fight(80, 30, 220)

frank = Hero
name, age = frank.person('Громила', 20)
damage, armor, health = frank.fight(95, 10, 330)





    