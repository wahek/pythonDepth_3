nums = [2, 2, 2, 3, 4, 5, 2, 1, 4, 6, 7, 4, 1]
res = []
for i, nam in enumerate(nums):
    if nam % 2 == 0:
        res.append(i+1)
print(res)

