def twoSum(nums, target):
    for count, num in enumerate(nums):
        find_diff = target - num
        if find_diff in nums[count+1:]:
            index1 = count
            index2 = nums[count+1:].index(find_diff) + (index1 + 1)
            index_list = [index1, index2]
            return index_list

# def twoSum(nums, target):
#     values = {}
#     # breakpoint()
#     for i, num in enumerate(nums):
#         remaining = target - num
#         if remaining in values:
#             return [values[remaining], i]
#         else:
#             values[num] = i


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
