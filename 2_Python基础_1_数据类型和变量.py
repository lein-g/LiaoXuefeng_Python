# -*- coding: utf-8 -*-

"""
在Python中，能够直接处理的数据类型有以下几种
整数:
Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样
计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，
十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2
浮点数:
浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，
比如，1.23x109和12.3x108是完全相等的
浮点数可以用数学写法，如1.23，3.14，-9.01
但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，
1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5
整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的，而浮点数运算则可能会有四舍五入的误差。
字符串:
字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"
''或""本身只是一种表示方式，不是字符串的一部分
布尔值:
布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值
在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来，比如3 > 2，3 > 5
布尔值可以用and、or和not运算
and运算是与运算，只有所有都为True，and运算结果才是True
or运算是或运算，只要其中有一个为True，or运算结果就是True
not运算是非运算，它是一个单目运算符，把True变成False，False变成True
空值:
空值是Python里一个特殊的值，用None表示
None不能理解为0，因为0是有意义的，而None是一个特殊的空值

此外，Python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型，后面会继续讲到
"""

# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print('I\'m \"OK\"!')
print('I\'m learning\nPython.')
print('\\\n\\')

# Python允许用'''...'''的格式表示多行内容
# Python还允许用r''表示''内部的字符串默认不转义
print(r'''hello,\n
world''')

# 布尔值经常用在条件判断中
age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')

"""
变量
变量的概念基本上和初中代数的方程变量是一致的，
只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型
"""
# 变量在程序中就是用一个变量名表示，变量名必须是大小写英文、数字和_的组合，且不能用数字开头
a = 1
t_007 = 'T007'
Answer = True

# 在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
a = 123  # a是整数
print(a)
a = 'ABC'  # a变为字符串
print(a)

"""
这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言
静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错，例如Java
和静态语言相比，动态语言更灵活
"""

# 不要把赋值语句的等号等同于数学的等号
# 赋值语句先计算右侧的表达式，得到结果，再赋给变量
x = 10
x = x + 2
print(x)

# 理解变量在计算机内存中的表示也非常重要
a = 'ABC'
# Python解释器干了两件事情：
# 1.在内存中创建了一个'ABC'的字符串
# 2.在内存中创建了一个名为a的变量，并把它指向'ABC'

a = 'ABC'  # 解释器创建了字符串'ABC'和变量a，并把a指向'ABC'
b = a  # 解释器创建了变量b，并把b指向a指向的字符串'ABC'
a = 'XYZ'  # 解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改
print(b)  # 最后打印变量b的结果自然是'ABC'

"""
常量
所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量
在Python中，通常用全部大写的变量名表示常量
"""

PI = 3.14159265359  # 但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变

# 解释一下整数的除法为什么也是精确的
# 在Python中，有两种除法，一种除法是/
print(10/3)

# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
print(9/3)

# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数
print(10//3)  # 整数的地板除//永远是整数，即使除不尽，要做精确的除法，使用/就可以。

# 因为//除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数
print(10 % 3)  # 无论整数做//除法还是取余数，结果永远是整数，所以，整数运算结果永远是精确的

# 练习
# 请打印出以下变量的值：
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

"""
小结
Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，
而变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来
对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的
随后对变量y的赋值不影响变量x的指向
注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，
例如Java对32位整数的范围限制在-2147483648-2147483647
Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）
"""
