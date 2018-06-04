"""
错误和异常处理的相关笔记
"""

"""
** 一些相关的网页：
https://www.linuxidc.com/Linux/2015-08/121973.htm
https://www.cnblogs.com/Lival/p/6203111.html
https://blog.csdn.net/a2011480169/article/details/73838486
"""

"""
# *********************  异常的相关知识 ************************

* 异常的描述： 它是因为程序出现了错误而在正常控制流以外采取的行为

* 异常处理机制：

            在Python当中，若一个程序在运行的时候出错，Python解释器会自动的在出错的地方生成一个异常对象，
        而后Python解释器会自动的在出错地方的附近寻找有没有对这个异常对象处理的代码，所谓异常处理代码就是try……except语句，
        如果没有，Python解释器会自动的将这个异常对象抛给其调用函数，就这样层层抛出，如果在main当中也没有对这个异常对象处理的代码，
        Python解释器（实际上是操作系统）最后会做一个简单粗暴的处理，将整个程序给终止掉，并将错误的信息在显示屏上输出。 

        * 注意：简单点说就是：

                                                                         ---> 找得到处理代码(异常被捕获)-->继续运行
                运行错误-->生成异常对象-->寻找处理异常的代码(try-excet语句)---
                                                                         ---> 异常没有被搏获-->层层上抛直至main,最后报错终止

* 异常处理的语句结构：

            try:              

                try_suite     # 运行try语句块，并试图捕获里面发生的异常,每次只要发生了一个异常，便开始捕获

            except Exception1:

                suite_for_Exception1    # 如果try_suite发生的是Exception1异常，则执行此块

            except (Exception2,Exception3):     # 元组中可以有更多个异常类

                suite_for_Exception2_Exception3   # 如果元组内的任意异常发生，那么捕获它

            except Exception5 as Exc_obj5:      # 捕获Exception5，并将所捕获的异常对象命名为Exc_obj5

                suite_for_Exception5_add_Exc_obj5

            except (Exception6,Exception7) as Exc_obj67:   # 捕获元组中的任一异常，并将其命名为Exc_obj67，元组中可以有更多个异常类

                suite_for_Exception67_add_Exc_obj67

            except:                         # 捕获发生了以上所有列出的异常之外的异常

                suite_for_all_other_exceptions

            else:                          # 在try范围内没有异常被检测到时执行else子句

                no_exception_detected_suite

            finally:                       # 无论异常是否发生以及是否被检测到，均执行该语句 

                always_execute_suite


            * try语句执行方式：

                * 首先，执行try子句（在关键字try和关键字except之间的语句）

                * 如果没有异常发生，忽略except子句，执行else和finally，之后执行try语句之后的代码

                * 如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和except之后的名称相符，那么对应的except子句将被执行，然后执行finally, 最后执行try-exception结构之外的语句，注意，try子句中发生异常之后的语句是被忽略的

            * 注意：
            
                * try结构有且只有一个，else和finally都是可选的，即0-1个，except语句则即可以没有，也可以有多个，即0-n个，
                  但是如果出现一个else的话，必须有至少一个except

                * except语句后面跟的是异常的类，而不是对象，所产生的异常对象只要属于except后面的异常类就会被捕获  

                * 不管你如何指定异常，异常总是通过实例对象来识别，并且大多数时候在任意给定的时刻激活。一旦异常在程序中某处由一条except子句捕获，它就死掉了，除非由另一个raise语句或错误重新引发它

* 异常参数： 

        * 对于一个异常对象Exc_obj,它具有一个.args属性，这个属性叫做异常参数

        * 由系统抛出的异常对象的异常参数通常是一个说明错误原因的字符串的单元素元组，可以由str()和print()直接看到

* 标准异常类的分级：

    - BaseException
        |- KeyboardInterrupt
        |- SystemExit
        |- Exception
            |- (all other current built-in exceptions) 所有当前内建异常

* python所有的标准异常类：

        BaseException	所有异常的基类
        SystemExit	解释器请求退出
        KeyboardInterrupt	用户中断执行(通常是输入^C)
        Exception	常规错误的基类
        StopIteration	迭代器没有更多的值
        GeneratorExit	生成器(generator)发生异常来通知退出
        SystemExit	Python 解释器请求退出
        StandardError	所有的内建标准异常的基类
        ArithmeticError	所有数值计算错误的基类
        FloatingPointError	浮点计算错误
        OverflowError	数值运算超出最大限制
        ZeroDivisionError	除(或取模)零 (所有数据类型)
        AssertionError	断言语句失败
        AttributeError	对象没有这个属性
        EOFError	没有内建输入,到达EOF 标记
        EnvironmentError	操作系统错误的基类
        IOError	输入/输出操作失败
        OSError	操作系统错误
        WindowsError	系统调用失败
        ImportError	导入模块/对象失败
        KeyboardInterrupt	用户中断执行(通常是输入^C)
        LookupError	无效数据查询的基类
        IndexError	序列中没有没有此索引(index)
        KeyError	映射中没有这个键
        MemoryError	内存溢出错误(对于Python 解释器不是致命的)
        NameError	未声明/初始化对象 (没有属性)
        UnboundLocalError	访问未初始化的本地变量
        ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
        RuntimeError	一般的运行时错误
        NotImplementedError	尚未实现的方法
        SyntaxError	Python 语法错误
        IndentationError	缩进错误
        TabError	Tab 和空格混用
        SystemError	一般的解释器系统错误
        TypeError	对类型无效的操作
        ValueError	传入无效的参数
        UnicodeError	Unicode 相关的错误
        UnicodeDecodeError	Unicode 解码时的错误
        UnicodeEncodeError	Unicode 编码时错误
        UnicodeTranslateError	Unicode 转换时错误
        Warning	警告的基类
        DeprecationWarning	关于被弃用的特征的警告
        FutureWarning	关于构造将来语义会有改变的警告
        OverflowWarning	旧的关于自动提升为长整型(long)的警告
        PendingDeprecationWarning	关于特性将会被废弃的警告
        RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
        SyntaxWarning	可疑的语法的警告
        UserWarning	用户代码生成的警告

* 人为抛出异常：

    * 可以用raise语句人为地抛出异常

    * raise语句格式：

        * raise Exc_class  : 触发一个异常，从Exc_class生成一个实例，不含异常参数

        * raise Exc_class() : 触发一个异常，从Exc_class生成一个实例，不含异常参数

        * raise  Exc_class, args : 触发一个异常，从Exc_class生成一个实例，含异常参数args,可以是一个元组

        * raise  Exc_class(args) : 触发一个异常，从Exc_class生成一个实例，含异常参数args,可以是一个元组

        * raise Exc_class, args, tb : 触发一个异常，从Exc_class生成一个实例，含异常参数args, 同时提供一个跟踪记录对象tb

* 断言：

    断言的格式： assert expression [,arguments]

    作用： 若expression为真，则继续执行；
          若expression为假，则触发AssertionError的异常，并将该异常对象的异常参数，即.args属性赋值为arguments
"""


a=10
b=0
try:
    c = a/b
    print('after exception in try suite')
except (IOError,ZeroDivisionError) as x:
    print(x)
else:
    print("no error")
finally:
    print('finally')
print("done")

try:
    raise ZeroDivisionError
except ZeroDivisionError as xx:
    print(xx)

try:
    assert 1==2, 'one does not equal two'
except AssertionError as arg:
    print(arg)
    print(arg.args)