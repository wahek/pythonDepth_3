my_str = '''Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.'''
my_dict = {}
my_str = my_str.replace(' ', '')
my_str = my_str.lower()
print(my_str)
for char in my_str:
    if my_dict.get(char):
        my_dict[char] = my_dict.get(char) + 1
    else:
        my_dict.setdefault(char, 1)
print(my_dict)
