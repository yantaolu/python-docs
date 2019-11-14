#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@文件    :01 - 数据类型.py
@说明    :
@时间    :2019/11/14 14:38:51
@作者    :YantaoLu
@版本    :1.0.0
'''

# 整数
1
0
-1
# 浮点数（小数）
1.1
3.14
-5.20
# 字符串（需要注意字符编码，推荐使用utf-8编码）
'string'
'中文'
# 布尔值（真/假）
True
False
# 空值
None

# 复杂数据类型
# list 列表
[1, 2, 3, 4]
# tuple 元组（注意只有一个元素的元组）
(1, 2, 3, 4) or (1,)
# dict 字典（数据形式上如常见的json格式）
{'nickname': '小仙女', 'age': 18}
# set（主要作用数据去重）
{1, 2, 3}


# 整数/浮点数

# 常见的加减乘除操作，遵循数学运算规则
1 + 1
100.38 - 9.1
2 * 2
100 / 10
(200 - 3.5 * 22) / 3


# 字符串

# 拼接
'I am ' + 'Ok.'  # => 'I am Ok.'

# 转义，当字符串内存在引号时，有时候可以利用单双引号避免转意
'I\'m Ok.'  # => "I'm Ok."

# 多行内容，字符串前后利用三引号 '''string'''，避免字符串拼接的麻烦
'''
line1
line2
line3
'''  # => 'line1\n' + 'line2\n' + 'line3\n'

# 字符串占位符格式化
'%s is my goddess.' % 'Mao Linlin'  # => 'Mao Linlin is my goddess'


# 布尔值（boolean）真 - True 假 - False

# 以下各种情况都属于布尔值
True
False
1 != 0  # => True
3 > 2  # => True
3 < 2  # => False
5 > 3 or 3 < 1  # => True or False => True
5 > 3 and 3 < 1  # => True and False => False
not 1 >= 2  # => not False => True
not False  # => True
None == ''  # => False

# 在if判断中一些特殊值也会转换为布尔值False，比如数字0、空值None、空字符串、空list等，所以在if判断时可以简写
if 0:
    print('0 是True')
else:
    print('0 是False')  # => 0是False

if 1:
    # => 1是True，实际上不等于0的数在if中都是true，在这里如果不明白规则，可以使用数据判断 if x > 0:
    print('1 是True')
else:
    print('1 是False')

if None:
    print('None 是True')
else:
    print('None 是False')  # => None 是False

if '':
    print('"" 是True')
else:
    print('"" 是False')  # => "" 是False

if []:
    print('[] 是True')
else:
    print('[] 是False')  # => [] 是False
