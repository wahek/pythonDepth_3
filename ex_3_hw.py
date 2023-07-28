"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
"""
from itertools import *

dict_items = {'knife': 5, 'water': 5, 'shelter': 9, 'axe': 7, 'eat': 14, 'clothes': 6, 'boat': 19, 'table': 23}
min_item = min(dict_items.values())
count_item = len(dict_items)
bag = []
capacity = 30
weight = 0
count = 0
all_iter_bag = []


# жадный алгоритм
def get_a_lot(weight_self: int, count_self: int) -> tuple:
    min_weight = min(dict_items.values())
    while capacity > weight_self and capacity - weight_self >= min_weight and count_self <= count_item:
        for key, value in dict_items.items():
            if value == min_weight:
                bag.append(key)
                weight_self += value
        count_self += 1
        min_weight += 1
    return bag, weight_self


print(f'{get_a_lot(weight, count)} <- вес')
set_item = set()
# Комбинаторика
dict_items = {'knife': 5, 'shelter': 9, 'axe': 7, 'boat': 19, 'table': 23}
for i in permutations(dict_items):
    weight = 0
    bag_items = []
    for j in i:
        if capacity > weight and capacity - weight > dict_items[j]:
            weight += dict_items[j]
            bag_items.append(j)
    bag_items = tuple(bag_items)
    set_item.add(bag_items)
    print(f'сумка: {bag_items} вес = {weight}')

# В общем не доделал, работает на 50 процентов
