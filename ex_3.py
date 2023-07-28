attributes = ('str', 1, 2.3, -100, '123', 'wef', True, False, ['sad', '23', 123])

res = {}
for attr in attributes:
    res.setdefault(type(attr), []).append(attr)

print(res)
