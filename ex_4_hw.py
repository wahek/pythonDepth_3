"""
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
* Какие вещи взяли все три друга
* Какие вещи уникальны, есть только у одного друга
* Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
* Для решения используйте операции с множествами.
Код должен расширяться на любое большее количество друзей.
"""

items = {'Vova': ('axe', 'knife', 'shelter'), 'Misha': ('knife', 'water', 'light'), 'Kolya': ('knife', 'shelter')}
list_of_keys = list(items.keys())
length = len(items)
items_copy = items.copy()
print(items_copy)

def all_have():
    first_set = set()
    count = 0
    res_set = set()
    for key, value in items.items():
        if count == 0:
            first_set = set(value)
            count += 1
        else:
            first_set &= set(value)
    return first_set


def once_have():
    uniq = []
    for kye,value in items.items():
        current_set = set(value)
        for k, v in items.items():
            if kye != k:
                current_set -= set(v)
        uniq.append(current_set)
    while True:
        try:
            uniq.remove(set())
        except ValueError:
            return uniq


print(f'Вещи которые есть у всех: {all_have()}')
print(f'Уникальные вещи: {once_have()}')
