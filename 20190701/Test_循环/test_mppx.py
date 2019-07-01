
'''
冒泡排序
'''
nums = [6, 10, 5, 63, 45, 34, 1, 3, 90, 2, 21, 55, 67]
k = 0
for i in range(len(nums)-1):
    for j in range(len(nums)-1-i):
        if nums[j] > nums[j+1]:
            k += 1
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)
print(k)


"""
选择排序
"""
k = 0
nums = [6, 10, 5, 63, 45, 34, 1, 3, 90, 2, 21, 55, 67]
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[j] < nums[i]:
            k += 1
            nums[j], nums[i] = nums[i], nums[j]

print(nums)
print(k)


"""
直接插入法
"""
nums = [6, 10, 5, 63, 45, 34, 1, 3, 90, 2, 21, 55, 67]
temp = 0
j = 0
for i in range(len(nums)):
    temp = nums[i]
    j = i
    while (j > 0) & (nums[j-1] >= temp):
        nums[j] = nums[j-1]
        j -= 1
    nums[j] = temp
print(nums)


# """
# 二分插入排序
# """
# nums = [6, 10, 5, 63, 45, 34, 1, 3, 90, 2, 21, 55, 67]
# i = j = k = temp = 0
# for i in range(1, len(nums)):
#     temp = nums[i]
#     if nums[i] < nums[0]:
#         k = 0
#     else
#         k = bin



