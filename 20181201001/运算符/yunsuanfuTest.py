'''
if

elif

else

'''


'''
比较运算符
==
>
<
>=
<=
!=
'''


'''
逻辑运算符
and or not
'''


print(not False)


'''
循环
'''
i = 0
list1 = []
while i < 20:
    list1.append(i)
    print("这是循环%d" % i)
    i += 1

print(list1.__len__())
j = 0
for j in list1:
    print('这是for循环%d' % list1[j])
    j += 1

z = 0
for z in range(0, 10):
    print(z)
    z += 1

'''
循环中的中断 
break 跳出整个循环
continue 跳出本次循环 继续执行下一个循环
'''

'''
循环 算法练习
1.冒泡排序
2.
'''

# 普通排序
nums = [3, 2, 5, 8, 0, 2, 9]
i = 0
j = 0
# for i in range(nums.__len__()):
#     for j in range(nums.__len__()):
#         iNum = nums[i]
#         jNum = nums[j]
#         if iNum > jNum:
#             ij = nums[i]
#             nums[i] = nums[j]
#             nums[j] = ij
# print(nums)


# 冒泡排序 选择排序
for i in range(nums.__len__()-1):
    for j in range(nums.__len__()-i-1):
        if nums[j] < nums[j+1]:
            (nums[j], nums[j+1]) = (nums[j+1], nums[j])
            # ij = nums[j]
            # nums[j] = nums[j+1]
            # nums[j+1] = ij
            print("第%d次内存循环%s" % (j, nums))
    print("第%d次外循环%s" % (i, nums))
print("最终的结果", nums)





