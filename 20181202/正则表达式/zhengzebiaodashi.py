'''

什么是正则表达式： 记录文本规则的代码
是一个特殊的字符序列
普通字符串和元字符组成的。其实就是对元字符的学习

'''

import re
reg_str = "124231njsndjnabcskdjkaksobabc>/asd[]中国;."
reg = "abc"
print(re.findall(reg, reg_str))


'''
元字符：
.  匹配除换行符以外的任意字符
\w 匹配字母 或者 数字 或者 下划线 或者 汉子
\s 匹配任意的空白符
\d 匹配数字
\b 匹配单词的开始或者结束
^  匹配字符串的开始
$  匹配字符串的结束
'''
print(re.findall("\d", reg_str))
print(re.findall("^124", reg_str))
print(re.findall("\w", reg_str))


'''
反义代码
\W 匹配任意不是字母、下划线、数字、汉字的字符
\S 匹配任意不是空白符的字符
\D 非数字
\B 匹配不是单词开头或者结束的位置
[^] 匹配除了xx以外的任意字符
'''


'''
限定符
* 重复零次或者多次
+ 重复一次或者多次
? 重复零次或者1次
{n} 重复n次
{n,} 重复n次或者更多次
{n, m}重复n到m次
'''
print(re.findall("\d{3}", reg_str))
print(re.findall("[0-9a-z]{3}", reg_str))

ip = "this is ip: 192.168.1.123 , 172.138.2.245"
reg1 = "\d{1,3}.\d+.\d+.\d+"
print(re.findall(reg1, ip))

# search
reg2 = "(\d{1,3}.){3}.\d{1,3}"
result = re.search(reg2, ip)
print(result[0])

'''
search 和 findall
search 只匹配第一个
findall 是匹配所有符合要求的
'''

'''
组匹配
'''
s = "this is phone:13688888888 and this is my postcode:012345"
reg3 = "this is phone:(\d+) and this is my postcode:(\d+)"
result = re.search(reg3, s)
print(result)

result = re.search(reg3, s).group(0)
print(result)
result = re.search(reg3, s).group(1)
print(result)
result = re.search(reg3, s).group(2)
print(result)

# match 只匹配开头的
reg_str1 = "hellopayhsdadHelloasdastring"
reg4 = "Hello"
result = re.match(reg4, reg_str1, re.I).group() # re.I 忽略大小写
print(result)


'''
# 贪婪 与 非贪婪 贪婪与懒惰
什么是贪婪 尽可能多的匹配
非贪婪 尽可能少的匹配
非贪婪操作符：?
这个操作符是用在 * + ? 后边的 要求正则匹配的越少越好

* 重复零次或者更多次 *? 重复零次
+ 重复一次或者更多次 +? 重复一次
? 重复零次或者一次   ?? 重复零次

'''

# 贪婪
reg_tl = "pythonnnnnnnnnHellopython"
reg1 = "python*"
print(re.findall(reg1, reg_tl))

# 非贪婪
reg1 = "python*?"
print(re.findall(reg1, reg_tl))

reg1 = "python+"
print(re.findall(reg1, reg_tl))

reg1 = "python+?"
print(re.findall(reg1, reg_tl))



'''
匹配手机号码
移动：139， 138， 137， 136， 135， 134
150，151， 152， 157， 158， 159
182，183，187，188

联通：130，131，132，185，186，145，166，176

电信：133，153，180，189 
'''

def check_cellphone(number):
    reg_phone = "^(13[0-9]|14[5]|15([0-3]|[7-9])|16[6]|17[6]|18([0]|[2-3]|[7-9]))\d{8}$"
    result = re.findall(reg_phone, number)
    if result:
        print("匹配成功：", number)
        return True
    else:
        print("匹配失败:", number)
        return False

cell_phone = "18819980914"
print(check_cellphone(cell_phone))

'''
验证邮箱的合法性：
新浪 网易 搜狐 QQ
xxx@sina.com
xxx@sina.cn
xxx@163.com
xxx@qq.com
'''
def check_mail(mail):
    reg_mail = "^([a-zA-Z0-9_-]+)@([a-zA-Z0-9_-]+).[a-zA-Z0-9_-]{1,6}$"
    result = re.findall(reg_mail, mail)
    if result:
        print("匹配成功：", mail)
        return True
    else:
        print("匹配失败:", mail)
        return False
mail = "9661asda@qq.icloud"
print(check_mail(mail))
