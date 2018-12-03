'''
声明一个字符串 str
'''

# 单引号声明
s1 = 'Hello,World -> 单引号'
print(s1)

# 双引号声明
s2 = 'Hello，World -> 双引号'
print(s2)

# 三引号声明 声明可以是多行
s3 = '''
Hello，World 三引号声明 声明多行字符串
'''
print(s3)


'''
字符串的操作
'''
# 单个访问字符串中的字符
s = "Hello,World"
print(s[0])

# f访问字符串中的子串 切片操作 左闭右开原则
print(s[0:5])

# 字符串相加运算
print("我正在练习学习"+'Python')

# 字符串更新操作-> 先切片 后相加


# 字符串的成员运算
# 包含运算 in 不包含运算 not in
s1 = "Hello world"
s2 = "h"
print(s1 in  s2)
print(s1 not in  s2)

# 转义字符 \n换行符
print('\'')
print("\"")
print('\\')

# 制表符 四个空格 tab

# 回车符 \r 光标到行首 打印\r之后的内容

# 输出原始字符串
print(r"Hello\nWorld")
print(R'Hello\nWorld')


# 字符串的格式化输出 %s字符串 %d整型
print('我叫%s,今天是我第%d天学习' %('小米', 10))

# str int float list
# 字符串的内建函数
# "Hello,World".isspace()
str
