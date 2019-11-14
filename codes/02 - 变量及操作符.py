#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 变量及操作简单回顾
# 为什么要有变量，因为程序存在太多的可变因素，比如用户的输入、时间每时每刻都在变，所以真实的代码中存在的各种计算绝大多数都是依赖变量
# 例如数学中常见的方程，常使用x、y、z代表未知数，所以变量实际上就是真实可以改变的值的一个代号，当真实值改变之后，跟代号相关的内容也会随之改变
# 例子中不再对常见的加、减、乘、除赘述

# 定义一个变量
print('定义变量x')
x = 5
print(x)  # => 5
print(x + 2)  # => 7

# 改变变量的值
print('改变变量的值')
x = 10
print(x)  # => 10
print(x + 2)  # => 12

# 利用变量本身改变变量的值（程序中很常见）
# 在数学中这种等式是错误的，因为无法计算出x的值，但是在程序中是可以的
# 注意代码的执行顺序
# 1、先执行 = 后面的内容，因为前面已经给 x 赋值为 10 ，所以 x + 10 = 20
# 2、将等号后面的结果 20 再次赋值给 x
print('利用变量自身改变变量的值')
x = x + 10
print(x)  # => 20
print('利用变量x定义一个新的变量y')
y = x + 1
print(y)  # => 21

# 咱们再看一个 dict 变量的修改值的操作
d = {'nickname': '小仙女', 'age': 18}
print(d)  # => {'nickname': '小仙女', 'age': 18}
# 咱们给 d 再增加一个 key - value
d['name'] = '毛琳琳'
print(d)  # => {'nickname': '小仙女', 'age': 18, 'name': '毛琳琳'}
# 咱们将 d 的 nickname 的值修改掉
d['nickname'] = '毛宝宝'
print(d)  # => {'nickname': '毛宝宝', 'age': 18, 'name': '毛琳琳'}


# 一、常见的运算操作符

# 除了数字、浮点类型的数据以外，字符串也可以相加
print('Linlin ' + 'Mao')
# 其他类型与字符串想加，需要转换为字符串
print('数字' + str(1000))

# + 加
5 + 5  # => 10
# - 减
10 - 5  # => 5
# * 乘
6 * 3  # => 18
# / 除
5 / 2  # => 2.5
# % 求余
5 % 2  # => 1
# ** 幂运算
5 ** 2  # => 25
# // 地板除（除法商向下取整）
5 // 2  # => 2


# 二、成员关系运算符

# in
3 in {1, 2, 3}
# not in
4 not in [1, 2, 3]


# 三、比较运算符

# < 小于
# <= 小于等于
# > 大于
# >= 大于等于
# == 相等
# != 不相等


# 四、逻辑操作符

# and 逻辑与（且）
# or 逻辑或（或者）
# not 逻辑非（不）


# 五、格式操作符 %

# 使用方法，带占位符的字符串使用 % 格式化
# 常用的占位符 %s %d $f 记住就足够了，记不住可以全部使用 %s
'%s is %d' % ('Linlin', 18)

# %c               格式化字符及其ASCII码
# %s               格式化字符串
# %d               格式化整数
# %o               格式化无符号八进制数
# %x               格式化无符号十六进制数
# %X               格式化无符号十六进制数(大写)
# %f               格式化浮点数，可指定小数点后的精度
# %e               用科学计数法格式化浮点数
# %E               用科学计数法格式化浮点数
# %g               根据数值的大小决定使用%f或%e
# %G               根据数值的大小决定使用%f或%e


# 六、转义字符（字符串中表示特殊字符的组合）
# 常用的专一字符 \' \" \n \t \\

# \'               单引号
# \"               双引号
# \a               发出系统响铃声
# \b               退格符
# \n               换行符
# \t               横向制表符TAB
# \v               纵向制表符
# \r               回车符
# \f               换页符
# \o               八进制数代表的字符
# \x               十六进制数代表的字符
# \0               表示一个空字符
# \\               反斜杠
