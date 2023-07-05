class Fruit:
    def __init__(self, id, name, color):
        self.id = id
        self.name = name
        self.color = color
    
    def get_color(self):
        return self.color

def get_sorted_fruits_by_color(fruits):
    return sorted(fruits, key=lambda x: x.get_color())

fruits = [
    Fruit(1, "Apple", "Red"),
    Fruit(2, "Banana", "Yellow"),
    Fruit(3, "Grape", "Purple"),
    Fruit(4, "Lemon", "Yellow"),
    Fruit(5, "Orange", "Orange"),
    Fruit(5, "Watermelon", "Green"),]

sorted_fruits = get_sorted_fruits_by_color(fruits)
for fruit in sorted_fruits:
    print(f"ID: {fruit.id}, Name: {fruit.name}, Color: {fruit.color}")
