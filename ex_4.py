nums = [1, 2, 4, 1, 4, 2, 5]

for num in nums:
    while nums.count(num) % 2 == 0 and num in nums:
        nums.remove(num)
        nums.remove(num)
print(nums)
