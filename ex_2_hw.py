"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
(Может помочь метод translate из модуля string)
"""
import string

my_str = '''
The following sections describe the standard types that are built into the interpreter.
The principal built-in types are numerics, sequences, mappings, classes, instances and exceptions.
Some collection classes are mutable. The methods that add, subtract, or rearrange their members in place, and don’t 
return a specific item, never return the collection instance itself but None.
Some operations are supported by several object types; in particular, practically all objects can be compared for 
equality, tested for truth value, and converted to a string (with the repr() function or the slightly different str() 
function). The latter function is implicitly used when an object is written by the print() function.
Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations 
below.
By default, an object is considered true unless its class defines either a __bool__() method that returns False or a 
_len_() method that returns zero, when called with the object. 1 Here are most of the built-in objects considered false:
'''
my_str = my_str.translate(str.maketrans(string.ascii_uppercase, string.ascii_lowercase, string.punctuation))
my_str = my_str.translate(str.maketrans('', '', '\n'))
my_dict = {}
dict_10 = {}
MAX_COUNT = 10
count = 0
list_of_char = my_str.split(' ')


def dict_pop(self_dict: dict) -> tuple:
    max_temp = max(self_dict.values())
    for key, value in self_dict.items():
        if value == max_temp:
            self_dict.pop(key)
            return key, value


def print_dict(self_dict: dict) -> None:
    for key, value in self_dict.items():
        print(f'Слово "{key}" встречается {value} раз')


for word in list_of_char:
    if my_dict.get(word):
        my_dict[word] = my_dict.get(word) + 1
    else:
        my_dict.setdefault(word, 1)
max_dir = max(my_dict.values())

# while max_dir > 0 and count < MAX_COUNT:
#     for key, value in my_dict.items():
#         if

while count < 10:
    a, b = dict_pop(my_dict)  # a it is a key, b is value
    dict_10.setdefault(a, b)
    count += 1

print_dict(dict_10)
