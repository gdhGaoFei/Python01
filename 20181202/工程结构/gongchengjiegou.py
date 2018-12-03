'''
Python的工程结构

                                ->
     ->         ->      -> 方法 -> 变量
包 ->    模块 ->    类  ->
     ->         ->      -> 变量



                  方法 -> 变量
包 -> 模块 -> 类 ->
                  变量


python 的编码规范
命名规范

包：使用小写字母命名，如果有多个单词，使用下划线分隔 如：lower_with_under
模块：使用小写字母命名，如果有多个单词 使用下划线分隔 如：lower_with_under
类：使用驼峰法命名，如果有多个单词，则首字母大写，私有类用下划线开头 如：HelloWord 和_HelloWord
方法(函数)：使用小写字母命名，如果有多个单词，使用下划线分隔，私有函数用下划线开头 如：lower_with_under 和 _lower_with_under
变量：使用小写字母命名，如果有多个单词，使用下划线分隔，私自变量用下划线开头 如：lower_with_under _lower_with_under或者__lower_with_under
常量：全部使用大写字母命名，如果有多个单词，使用下划线分隔 私有变量用下划线开头 如：CAPS_WITH_UNDER 和 _CAPS_WITH_UNDER


只有类名是用驼峰命名法
其他全部都是小写用下划线分隔
常量字母都是大写
下划线开头的都是私有的


特殊的模块__init__.py
只有包含了__init__.py模块的文件夹才能成为包
__init__.py是在模块导入时运行的


'''
print("运行前")

from part2 import *

print("运行后")

'''
导包路径
相对导入
绝对导入

. 代表的就是当前的目录 ..代表上一层目录

import ... as p p代表的就是前面的文件

'''







'''

函数：function
定义的格式
def

'''
def my_func():
    # 实现代码
    pass

# 函数的参数
# 必须参数
def my_func_with_param(p1, p2):
    print(p1, p2)

my_func_with_param(1, 3)

'''
形参：形式参数 只有意义上的一种参数 在定义的时候不占内存地址
实参：实实在在的参数 是实际上占用内存地址的
'''

# 关键字参数：是在调用的时候制定参数名称，可以不按照顺序传参数
def my_func_with_name_age(name, age):
    print("姓名：" + str(name) + " 年龄：" + str(age))
my_func_with_name_age(age="小米", name=23)


# 默认参数：如果调用者没有传值，则使用默认值，可以不指定名字
def my_func_with_mrcs_name_age(age=13, name="小米"):
    print("姓名：" + str(name) + " 年龄：" + str(age))
my_func_with_mrcs_name_age()

# 混合参数使用：非默认参数必须在默认参数之前

'''
函数返回值
return
'''

def func_with_return(p):
    return p
str1 = func_with_return("asd")
print(str1)

# 函数重载  会覆盖上面出现的相同的函数

# 多个参数 多个返回值 返回值是元组类型

# 返回值是一个函数 类似：block

'''
# 递归函数 在函数中调用自己
重点：要明确递归结束的条件
优点：写法非常之简洁
缺点：效率低，容易死循环
要求：每次递归的时候 规模都要有所缩小
'''

# 阶乘计算
def jiechengjisuan(x):
    if x == 1:
        return 1
    return x * jiechengjisuan(x-1)
print(jiechengjisuan(3))

'''
递归查找
有一个不规则的 list1 = [4, 6, 7, 9 ,22, 11, 90, 44]
定义一个函数：
接受一个list 和 数字
返回数字在列表中的排序后的位置， 如果出错或者没有则返回-1
'''

def diguichazhao(list1, num, d_or_x: bool):
    is_list = type(list1) is list
    is_int = type(num) is int
    is_in_list = num in list1
    if is_list and is_int and is_in_list:
        print("在")
        print(d_or_x)

        # 交互两个数字
        def exchange_a_b(a, b):
            return b, a

        list3 = list1.copy()

        for i in range(list1.__len__()-1):
            for j in range(list1.__len__()-i-1):
                # 从小到大
                if d_or_x:
                    if list1[j] > list1[j+1]:
                        list1[j], list1[j+1] = exchange_a_b(list1[j], list1[j+1])
                else:
                    if list1[j] < list1[j+1]:
                        list1[j], list1[j+1] = list1[j+1], list1[j]

        print(list1)
        list1 = list3.copy()
        print(list1)

        # 递归查找进行排序
        def digui_paixu(list2, index: int):
            if index == 0:
                return list2[index]
            index1 = index
            index2 = index-1
            num1 = list2[index1]
            num2 = list2[index2]
            # 从小到大
            if d_or_x:
                if num1 < num2:
                    list2[index1], list2[index2] = num2, num1
            else:
                if num1 > num2:
                    list2[index1], list2[index2] = num2, num1
            return digui_paixu(list2, index-1)
        for i in range(list1.__len__()):
            digui_paixu(list1, i)
        print(list1)
        return list1.index(num)

    else:
        print("不在")
        return -1



'''
__name__
只有在本模块启动时，__name__变量等于__main__
在什么时候使用
1.可以作为这个模块的入口，在其他语言中，叫做main函数
2.也可以作为调用使用，原因：在其他模块调用本模块时，__name__=="main"
判断结果为false 所以就不会执行
'''

import hanshu_func.my_func_hanshu as hanshu_my
result1 = hanshu_my.diguichazhao([1, 4, 6, 2, 5, 9, 1], 2, True)
print(result1)
print(hanshu_my.func_main())


'''
变量的作用域
在Python中没有块级的作用域，代码里的变量，外部是可以调用的
'''
# if result1 > 0:
#     name = "变量的作用域"
# else:
#     name1 = "asdads"
# print(name)


'''
变量的作用域链
变量由内到外去找这个变量的值
'''