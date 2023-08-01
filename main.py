    # 1
fruit = ('Яблоко', 'Апельсин', 'Банан', 'Яблоко', 'Персик', 'Апельсин', 'Апельсин', 'Яблоковыаы')
name_fruit = input("Введите название фрукта: ")
count = fruit.count(name_fruit)
print(name_fruit,  'встречается -', count, 'раз(а)')

    # 2
fruit_name = input("Введите название фрукта: ")
count = 0
for fruits in fruit:
    if fruit_name in fruits:
        count += 1
print(fruit_name, 'встречается -', count, 'раз(а)')

    # 3
import random
auto = ["Toyota", "Volkswagen", "Ford", "Nissan", "Honda", "Ford", "Fiat", "Toyota"]
list1 = tuple([random.choice(auto) for i in range(len(auto))])
print(auto)
old = input("Введите название которое необходимо заменить: ")
new = input("Заменить на какое название: ")

new_cars = tuple([new if x == old else x for x in auto])
print(new_cars)

    # 4
numbers = (1, 2, 30, 21, 435, 21312, 344, 53, 54, 92, 10, 20)

count1 = 0
count2 = 0
count3 = 0
for i in range(len(numbers)):
    if len(str(numbers[i])) == 1:
        count1 += 1
    elif len(str(numbers[i])) == 2:
        count2 += 1
    elif len(str(numbers[i])) == 3:
        count3 += 1
print(count1)
print(count2)
print(count3)