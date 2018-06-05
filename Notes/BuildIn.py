
'''
# *********************  内建函数说明 ************************
# ref: https://docs.python.org/3/library/functions.html
# ref: http://www.runoob.com/python3/python3-built-in-functions.html


* abs():        语法： abs(x)
                参数： x--数值表达式，可以是整数，浮点数，复数
                作用： 函数返回x的绝对值，如果参数是一个复数，则返回它的大小

* all()与 any():   详见 https://www.cnblogs.com/nulige/p/6128816.html

        * any():    any(iterable) -> bool

                    Return True if bool(x) is True for any x in the iterable.
                    If the iterable is empty, return False.

                    * 说明：接受可迭代对象，只要可迭代对象中任意地有一个元素x的bool(x)为True,则返回True,
                           否则返回False,空可迭代对象返回False

        * all()：   all(iterable) -> bool

                    Return True if bool(x) is True for all values x in the iterable.
                    If the iterable is empty, return True.

                    * 说明：接受可迭代对象，如果可迭代对象中所有的元素的bool()为True,则返回True,
                           否则返回False,空可迭代对象返回True

* ascii():      语法： ascii(object)
                作用： ascii() 函数类似 repr() 函数, 返回一个表示对象的字符串, 
                但是对于字符串中的非ASCII字符则返回通过 repr() 函数使用 \x, \u 或 \U 编码的字符。

* bin():        语法： bin(x)
                参数： x--int数字
                作用：bin() 返回一个整数int的二进制表示,返回形式为字符串

*bool():        详见 https://www.cnblogs.com/sesshoumaru/archive/2016/10/19/5979073.html

            * 返回值为True或者False的布尔值，参数如果缺省，则返回False

            * 传入布尔类型时，按原值返回, 如bool(True)-->True

            * 传入字符串时，空字符串返回False，否则返回True, 如bool('')-->False,bool('0')-->True

            * 传入数值时，0值返回False，否则返回True, 如bool(0)-->False, bool(0.0)-->False, bool(1.0)-->True

            * 传入元组、列表、字典等对象时，元素个数为空返回False，否则返回True, 如bool(())-->False,bool((1,))-->True

* bytearray()： 返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0<=x<256

* bytes():      返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。它是 bytearray 的不可变版本。

* callable():   语法： callable(object)
                作用：用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；
                    但如果返回False，调用对象ojbect绝对不会成功。

* chr():        语法：chr(i)
                参数：i--可以是10进制也可以是16进制的形式的数字
                作用：用一个范围在0～255整数作参数，返回一个对应的字符

* classmethod(): 待写

* compile()：     待写

* complex()：     语法：complex([real[, imag]])
                  参数：real--int,float；imag--int,float
                  作用：复数类型的工厂函数

* delattr()： 待写

* dict():          语法：dict(**kwarg); dict(mapping, **kwarg); dict(iterable, **kwarg)
                   参数：**kwargs--关键字； mapping--元素的容器； iterable--可迭代对象
                   作用：字典的工厂函数

                   如：     >>> dict(a='a', b='b', t='t')     # 传入关键字
                            {'a': 'a', 'b': 'b', 't': 't'}
                            >>> dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
                            {'three': 3, 'two': 2, 'one': 1} 
                            >>> dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典
                            {'three': 3, 'two': 2, 'one': 1}

* dir():            语法： dir([obj]) 
                    作用： 显示对象属性，如果不提供参数，则显示全局变量的名字

* divmod():         语法： divmod(a, b)
                    参数：a--数字；b--数字
                    作用：函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a//b, a%b)

* enumerate():      语法： enumerate(iterable)
                    作用：接受一个可迭代对象，返回一个enumerate对象(也是一个可迭代对象)，
                    该对象成生由iter的每个元素的index值和item值组成的元组

* eval(): 待写

* exec(): 待写

* filter()：    用于过滤可迭代对象，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
                该函数接收两个参数，第一个为一个布尔函数，第二个为可迭代对象，
                可迭代对象的每个元素作为参数传递给函数进行判断，然后返回True或False，
                最后将返回True的元素放到新的名为filter类型的对象中。

                格式： filter(boolfunction, iterable)
                返回： filter对象,是一个迭代器

* float()： float类型的工厂函数

* format(): 字符串格式化函数

* frozenset():      语法： frozenset([iterable])
                    参数： iterable--可迭代的对象，比如数字,元组等
                    作用：不可变集合的工厂函数

* getattr()： 待写

* globals()： 函数会以字典类型返回当前位置的全部全局变量，无输入参数

* hasattr()： 待写

* hash():           语法： hash(obj)
                    作用： 用于获取取一个对象（字符串或者数值等）的哈希值

* help():           语法： help([object])
                    作用： 返回对象帮助信息

* hex()：            语法：hex(x)
                     参数：x--十进制数
                     作用：用于将10进制整数转换成16进制，以字符串形式表示

* id():              语法： id(obj)
                     作用：获取对象地址

* input()：          作用：函数接受一个标准输入数据，可提供一个可选的参数str用于提示，返回为string类型

* int()：            语法：int(x, base=10)
                     参数：x--字符串或数字；base--进制数，默认十进制
                     作用：用于将一个字符串或数字转换为整型

* isinstance()：      语法： isinstance(object, classinfo)，
                      参数： classinfo可以是直接或间接类名、基本类型或者由它们组成的元组
                      作用： 判断一个对象是否是一个已知的类型
                      注意： classinfo 可以是int，float，bool，complex，str(字符串,注意不是string)，
                            list，dict(字典)，set，tuple等

* issubclass()： 待写

* iter()： 待写

* len()：              返回容器对象（字符、列表、元组等）的长度或项目个数

* list():               语法：list(iterable)
                        作用：将可迭代对象转化成一个列表

* locals()： 函数会以字典类型返回当前位置的全部局部变量，无输入参数

* map()：       会根据提供的函数对指定序列做映射，第一个参数 function以参数序列中的每一个元素调用function函数，
                返回包含每次function函数返回值的map对象

                格式： map(function, iterable, ...)
                返回： map对象,是一个迭代器

* max():                语法：max(iterable)
                        作用：返回可迭代对象中的最大值

* memoryview(): 待写

* min():                语法：min(iterable)
                        作用：返回可迭代对象中的最小值

* next()：              语法：next(iterator[, default])     
                        参数：iterator--迭代器对象;
                             default--可选，用于设置在没有下一个元素时返回该默认值，
                             如果不设置，又没有下一个元素则会触发 StopIteration 异常
                        作用：返回迭代器的下一个项目

* object():             语法： oct(x)
                        参数： x--整数
                        作用： 将一个整数转换成8进制字符串

* open():               文件对象的工厂函数

* ord():                将一个字符转换为它的ASCII值

* pow():                 幂的计算

* print():              语法： print(*objects, sep=' ', end='\n', file=sys.stdout)
                        参数： objects--复数,表示可以一次输出多个对象。输出多个对象时，需要用,分隔
                                sep--用来间隔多个对象，默认值是一个空格
                                end--用来设定以什么结尾,默认值是换行符 \n，我们可以换成其他字符串
                                file--要写入的文件对象
                        作用：用于打印输出

* property()：  待写

* range()：             语法： range(stop)；range(start, stop[, step])   
                        参数： start: 计数从start开始，默认是从0开始
                               stop: 计数到stop结束，但不包括stop
                               step：步长，默认为1
                        作用：返回一个range对象，它是一个可迭代对象

* repr()：              语法： repr(object)
                        作用：将对象转化为供解释器读取的字符串形式

* reversed():           语法： reversed(seq)
                        参数：seq--要转换的序列，可以是 tuple, string, list或range
                        作用：返回一个反转的迭代器

* round():              语法： round(x [,n])
                        参数： x--数字表达式
                              n--表示从小数点位数，其中x需要四舍五入，默认值为 0
                        作用： 浮点数x的四舍五入值

* set():                语法： set([iterable])
                        参数： iterable--可迭代的对象，比如数字,元组等
                        作用：可变集合的工厂函数

* setattr(): 待写

* slice():              语法： slice(stop)；slice(start,stop[,step])   
                        参数： tart--起始位置；stop--结束位置；step--间距
                        作用：返回一个切片对象

* sorted()：            语法: sorted(iterable, key=None, reverse=False)  
                        参数：iterable--可迭代对象
                              key--主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，
                                   指定可迭代对象中的一个元素来进行排序。
                              reverse--排序规则，reverse=True降序，reverse=False升序（默认）

                        作用：对所有可迭代的对象进行排序操作，返回重新排序后的列表

* staticmethod()： 待写

* str():                语法： str(object='')
                        作用：将对象转化成适于人阅读的字符串形式

* sum():                语法：sum(iterable[, start])
                        参数：iterable--可迭代对象，如：列表、元组、集合
                              start--指定相加的参数，如果没有设置这个值，默认为0
                        作用： 对可迭代对象进行求和计算，返回计算值,
                               其本质是将可迭代对象的逐元用+连接

* super(): 待写

* tuple:                语法： tuple(iterable=())
                        作用：元组的工厂函数

* type()：              返回对象的类型

* vars()：待写

* zip():                语法： zip([iterable, ...])
                        作用： 返回元组列表

* __import__()： 待写
'''