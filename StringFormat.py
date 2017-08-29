# -*- coding: utf-8 -*-

'''
string类型的format方法示例
Ref:
http://www.cnblogs.com/ToDoToTry/p/5635863.html
http://www.jb51.net/article/63672.htm
http://blog.csdn.net/lis_12/article/details/52712994
'''

########             映射方式             ########
# 映射方式是指大括号匹配对象的方式

# 1： 缺省, 按顺序依次匹配
print("Name:{}, Age:{}".format('Liu Xi', 27))

# 2: 序号, 可以不按顺序，也可以使用多次
print("Name:{1}, Age:{0}, Name:{1}".format(27,'Liu Xi'))

# 3：关键字参数 
print("Name:{name}, Age:{age}".format(name='Liu Xi',age=27))

# 4：下标: 序号+下标
name = ["Liu", "Xi"]
print("Name:{0[0]} {0[1]}, Age:{1}".format(name,27))

# 对象属性
class Person:
	def __init__(self,name,age):
		(self.name, self.age) = (name,age)
	def Get(self):
		return "Name:{self.name}, Age:{self.age}".format(self=self) # 直接用对象的属性来匹配
print(Person("Liu Xi",27).Get())

########             格式限定符             ########
# 指定格式说明符,对输出进行更加精确地控制
'''
**  映射方式部分与格式限定符之间用:隔开

**  给每个占位符添加可选的格式说明符号:  {name:format_spec}

*  一般格式[fill,align,sign,0,width,.precision,type],每一处都是可选的.
     *  fill:是一个可选的填充字符,用于填充空白,默认为空格;
     *  align,对齐方式.<,>,^分别代表左,右,居中对齐,默认为右对齐;
     *  sign,取值为: 
		(1) +,所有数字签名都要加上符号;
        (2) -,默认值,只在负数签名加符号;
        (3) 空格,在正数前面加上一个空格;
 	 *  0,在宽度前面加0表示用0来填充数值前面的空白;
     *  width,宽度;
     *  .precision,精度的位数;
     *  type,数据类型,如d(整数),s(字符串), f(浮点数), 逗号(千分位), e(科学计数)等
'''
print("{0:*>+10.4f},{1:>12s}".format(3.1415926,'Python'))
print("c = {:8.2e} m/s".format(3e8)) # 科学计数法
print("M = {:20,}".format(123456789)) # 千分位
