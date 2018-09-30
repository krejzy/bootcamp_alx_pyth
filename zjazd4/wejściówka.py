# Stwórz klasę Animal, która ma atrybuty name i age, oraz metodę sound
# >>> animal = Animal("Strange something", 1000)
# >>> animal.name
# "Strange something"
# >>> animal.age
# 1000
# >>> animal.sound()
# "kncok kncok"
# Stwórz klasy Dog i Cat, które dziedziczą po Animal i przeciążają metodę sound tak, że:
# >>> cat = Cat("Albert", 5)
# >>> dog = Dog("Nina", 6)
# >>> dog.sound()
# "how how"
# >>> cat.sound()
# "... (sorry - that's cat!)"
# Przeciaż operator >  tak by, można było porównywać wiek:
# >>> cat > dog
# True
# >>> dog > animal
# False

class Animal (Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sound = "knock knock"



    def sound(self):
        returm "knock knock"


      def test



