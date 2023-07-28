# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно
# быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]
nums = [1, 2, 3, 1, 2, 4, 5]
res = []


def ex_1() -> list:
    for num in nums:
        if nums.count(num) > 1:
            res.append(num)
    my_set = set(res)
    return list(my_set)


print(ex_1())
