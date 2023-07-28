my_str = 'wer dfdfg eee fdgb erg gerg'
word = []

word = sorted(my_str.split(' ', my_str.count(' ')))
print(word)
max_len = len(max(word, key=len))
print(max_len)
for i, w in enumerate(word):
    print(f'{i: >} {w: >{max_len}}')
