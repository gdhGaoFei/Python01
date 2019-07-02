"""
定义一个函数，功能要求:
接受一个list和一个数字
返回数字在列表中排序后的位置，如果出错或者没有此数字时，返回-1
"""


def my_func_list_int(list1, num):
    if (type(list1) is list) or type(list1) is tuple:
        if type(list1) is tuple:
            list1 = list(list1)

        if num in list1:
            for i in range(len(list1)-1):
                for j in range(len(list1)-i-1):
                    if list1[j] > list1[j+1]:
                        list1[j], list1[j+1] = list1[j+1], list1[j]
            index = list(list1).index(num)
            print(str(num) + " in "+str(list1)+ ", index is "+str(index))
            return index
        else:
            print(str(num) + " not in "+str(list1))
            return -1
    else:
        print(str(list1) + " is not list")
        return -1

result = my_func_list_int((2, 4, 5, 1, 6), 4)
print(result)



