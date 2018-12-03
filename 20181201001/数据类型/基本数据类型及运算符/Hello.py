print("Hello Python one World")


'''
变量命名规范：只能由字母、数字、下划线组成 首字母不能是数字 不能以关键字 多以驼峰命名规则


数据类型？数据类型就是 不同的盒子放不同的物品 那么物品就是数据，盒子就是指的一块内存地址
1. 基本数据类型：整型、浮点型、布尔型
2.字符串 3.列表 4.元组集合Set 5.集合 6.字典
'''


# 声明一个变量
firstNumber = 1
print(firstNumber)
print(type(firstNumber))#整数类型

secondNumber = 8.0
print(secondNumber)
print(type(secondNumber))#浮点类型

#布尔型
thirdNumber = False
print(thirdNumber)
print(type(thirdNumber))#bool 型数据

'''
基本运算符
加+ 减— 乘* 除/
'''
first1 = 5
first2 = 6
result1 = first1+first2
print(result1)#加
print(first2-first1)#减
print(first1*first2)#乘
print(first1/first2)#除
print(type(first1/first2))#类型 浮点型


'''
算术运算符
'''
#取模运算 求余数
i1 = 10
j1 = 3
z = i1%j1
print(z)

#幂运算
print(j1**i1)

#取整除运算
print(i1 // j1)

'''
赋值运算符
'''
#加等于 减等于 除等于 乘等于 求余等于 求幂等于 取整等于
i = 1
i /= 5
print(i)



'''
进制等于

十进制 二进制 八进制 十六进制
'''
#十进制 转化成其他的进制
# 十进制转化成二进制
i = 16
j = bin(i)
print(j)
# 十进制转成八进制
print(oct(i))
# 十进制转成十六进制
print(hex(i))

# 二进制转成十进制
i = "10"
print(int(i, 16))


'''

'''
# 按位与运算 & 两个值相对应的位置都是1为 -> 1

# 按位或运算 | 两个值相对应的位置一个为1即是1

# 按位异或运算 ^ 两个值相对应的位置不同则是1

# 按位取反运算 ~ 对应的值取反-1

# 左移运算符 <<

# 右移运算符 >>


'''
条件控制  比较运算符 ==
if 条件:
   语句
else:
   语句
   
---------   
   
if 条件:
   语句
elif 条件:
    语句
...
else:
    语句
'''


