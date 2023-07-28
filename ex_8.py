

items = {'Vova': ('axe', 'knife', 'shelter'), 'Misha': ('knife', 'water', 'light'), 'Kolya': ('knife', 'shelter')}

my_set = set()
list_of_set = []


def all_have():
    for key, value in items.items():
        for v in value:
            my_set.add(v)
    return my_set


def have():
    f_set = items.values()
    for key, value in items.items():
        new_set = value

        list_of_set.append(new_set)
    print(first_set)
    # for item in list_of_set:


# print(all_have())
have()
