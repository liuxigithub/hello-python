"""
Python中的对象
"""

"""
# ********************* Python中的对象 ************************

* Python使用对象模型来存储数据，构造任何类型的值都是一个对象

* 所有的Python对象都拥有三个特性： 身份，类型和值

    身份(id): 每个对象都有一个唯一的标识自己的身份，可以利用内建函数id()得到，这个值是该对象的内存地址

    类型(type): 指这个对象的数据类型，决定了该对象可以保存什么类型的值，可以进行什么样的操作，可利用type()查看

    值(dir): 表示对象的数据项。 具体地，指对象具有的属性，值或相关联的可执行代码，比如方法(Method)等，可用dir()查看对象属性

"""

"""
# ********************* Python中的标准类型(基本数据类型) ************************

* 数字：不可变类型

    * 整型(Integer): int(), 表示范围由机器支持的内存大小有关， 常量：0

        * 关于整型的工厂函数：
            1. hex(num): 将数字转换成十六进制数并以字符串形式返回
            2. oct(num): 将数字转换成八进制数并以字符串形式返回
            3. chr(num): 将ASCII值的数字转换成ASCII字符
            4. ord(chr): 将一个字符转换为它的ASCII值

    * 浮点型(Floating point real number): float(), 实际精度依赖于机器架构和解释器，常量：0.0

    * 布尔型(Boolean): bool(), 只有两个常量： True 和 False

    * 复数型(Complex number): complex(real,imag=0), 实部和虚部都是浮点型，虚部必须加后缀j或者J，常量：0.0+0.0j

            * 复数的内建属性：
                1. num.real: 复数的实部
                2. num.imag: 复数的虚部
                3. num.conjugate(): 返回复数的共轭复数

            * 数值运算常用的内建函数：
                1. abs(num): 返回绝对值
                2. divmod(num1,num2): 返回元组(商，余数)
                3. pow(num1,num2,mod=1): 取num1的num2次方，如果提供mod参数，则计算结果再对mod进行取余运算
                4. round(flt,ndig=1): 返回浮点数flt的四舍五入值，保存ndig位小数。

* 序列：
    
    * 字符串(String)：str()，repr()，不可变类型，常量：""(空字符串)

    * 列表(List): list()，可变类型，常量：[](空元组)

    * 元组(Tuple): tuple(), 不可变类型，常量：()(空元组)

* 映射类型：

    * 字典(Dictionary): dict(), 可变类型，常量：{}(空字典)

* 集合类型： 可变集合：set()；  不可变集合：frozenset()

"""

# 测试用例
print('a=',1)
print(int(hex(18),base=16))
print(bool(1))
print(complex(1,1).real)


"""
# ********************* Python中的其它内建类型 ************************

* type类型对象：type()，表示各种类型的数据类型的对象，包括type本身也是一种type对象

* None对象：Python中的空(Null)对象

* 文件对象：file()

* 集合/固定集合对象：set()，frozenset()

* 函数/方法对象：

* 代码对象：

* 帧对象：

* 异常对象：

* 切片对象：

* 省略对象：

* range对象

* 等...

"""

print(type(1),type(int),type(type),type(type(1)),type(type(type)))

print(type(range(10)))

"""
# ********************* Python对象的比较 ************************

* 对象值的比较：利用比较运算符来进行; 数字指数值大小和符号比较，字符串按照字符序列值进行比较

* 对象身份的比较： 比较符号所代表的引用是否指向同一个地址，即id(a)是否等于id(b)，也可以用对象身份比较操作符

    * 对象身份比较操作符：is [同一对象则返回True，否则False],  is not  [不同对象则返回True，否则False]

* 对象所属类型的比较： 比较对象是否属于同一类型有如下方法

    1. type(a) == type(b)
    2. type(a) is type(b)

    * isinstance函数： isinstance(object, classinfo)，classinfo可以是直接或间接类名、基本类型或者由它们组成的元组
                        
        用法示例：isinstance(a,int), isinstance (a,(str,int,list))
        
        注意： 对于基本类型来说 classinfo 可以是int，float，bool，complex，str(字符串)，list，dict(字典)，set，tuple

"""
a=1
b=a
c=2
d=3.0
print(id(a)==id(b),a is b, a is not b, type(a) is type(c), type(a) is type(d))
print(isinstance('a',(int,str,set)))


"""
# ********************* 标准类型的分类 ************************

* 以存储模型为标准： 

        标量/原子类型：数值，字符串

        容器类型：列表，元组，字典，集合

* 以更新模型为标准：

        可变类型：列表，字典，可变集合

        不可变类型： 数字，字符串，元组，不可变集合

* 以访问模型为标准：

        直接访问： 数字

        顺序访问： 字符串，列表，元组

        映射访问： 字典
    
"""