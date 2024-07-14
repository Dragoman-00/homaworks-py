class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        House.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):
        if new_floor > self.number_of_floors or self.number_of_floors < 1:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i+1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __del__(self):
        print(f"{self.name} снесён, но он остаётся в памяти")




# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
#
# # h1.go_to(5)
# # h2.go_to(10)
# print(h1.name, h1.number_of_floors)
# print(h2.name, h2.number_of_floors)
#
# # str
# print(h1)
# print(h2)
#
# # len
# print(len(h1))
# print(len(h2))
#
#
# print("---------------------------------------------------------------------------------")
# print("Перегрузка операторов.")
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
# print(h1)
# print(h2)
#
# print("---------------------------------------------------------------------------------")
# print(h1 == h2) # eq
# print("Проверка add")
# h1 = h1 + 10 # add
# print(h1)
# print(h1 == h2)
#
# print("-------------------")
# print("radd and iadd")
# h1 += 10 # iadd
# print(h1)
# h2 = 10 + h2 # radd
# print(h2)
#
# print("-------------------")
# print(h1 > h2) # gt
# print(h1 >= h2) # ge
# print(h1 < h2) # lt
# print(h1 <= h2) # le
# print(h1 != h2) # ne
# print("-------------------")

print("---------------------------------------------------------------------------------")
print("История построения")
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)