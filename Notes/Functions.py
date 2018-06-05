"""
函数的相关内容笔记
"""

"""
# *********************  函数的相关知识 ************************

* 函数是对程序逻辑进行结构化或过程化的一种编程方法

* 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

* 函数能提高应用的模块性，和代码的重复利用率。

* 函数是一个函数类的对象，它对应的函数类是function

* 函数的定义规则：

        * 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()

        * 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数

        * 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明

        * 函数内容以冒号起始，并且缩进

        * return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None

* 函数定义的格式：

    def func(positional_args, default_args, *tuple_grp_nondw_args, **dict_grp_kw_args):
        "function_documentation_string"
        function_body_suite

        * positional_args是位置参数或者说必需要参数

        * default_args表示默认参数，其后用等号给出默认值

        * tuple_grp_nondw_args是以元组体现的非关键字参数组，是不定长参数

        * dict_grp_kw_args是装有关键字参数的字典，是不定长参数

    * 注意：

        * 以上四种参数可以组合选取，甚至可以没有参数，但是其相对位置不能改变,比如，位置参数一定要在默认参数之前

        * 函数的文档字符串是函数对象的.__doc__属性

* 函数的属性：

        * 函数体自身可以携带属性，但是并不能在函数的声明中访问函数属性

        * 示例： 
                def foo():
                    print(''Hello World)
                    foo.version = '1.0'

* Python中的函数可以嵌套

* 函数的调用格式：

            func(arg1,arg2,...,*(...),**{...})

            * 上述格式中的项都是可选的，不一定都要出现

            * 参数书写顺序为：位置/默认参数-->关键字参数-->元组-->字典

            * 如果没有*(...)和**{...}：
            
                     先匹配关键字参数keyword_args，再依次配匹位置参数和默认参数，再匹配元组和字典

            * 如果存在*(...)或**{...}：

                     先直接匹配*(...)和**{...}，再匹配关键字参数，无法匹配的关键字将合并到字典，再依次匹配位置参数和默认参数

            * 例如：

                def foo(arg1,arg2,arg3=1,*nkw,*kw)

                foo(10,20,30,40,50,fo=60,bar=70) ===> arg1=10,arg2=20,arg3=30,nkw = (40,50),kw={'fo':60,'bar':70}

* 参数传递：

            * 不可变类型：类似c++的值传递，如整数、字符串、元组。如fun(a)，传递的只是a的值，没有影响a对象本身。
              比如在fun(a)内部修改a的值，只是修改另一个复制的对象，不会影响a本身

            * 可变类型：类似c++的引用传递,如列表，字典。如 fun(la)，则是将la真正的传过去，修改后fun外部的la也会受影响

* lambda函数： lambad语句快速创建一个匿名函数对象

            * lambda只是一个表达式，函数体比def简单很多

            * lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去

            * lambda函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数

    * lambda语句的格式：

                        lambda [arg1 [,arg2,.....argn]]:expression

                * 其返回的是一个函数对象

* 内建函数filter()和map():

    * filter(): 用于过滤可迭代对象，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。该函数接收两个参数，
                第一个为一个布尔函数，第二个为可迭代对象，可迭代对象的每个元素作为参数传递给函数进行判断，然后返回True或False，
                最后将返回True的元素放到新的名为filter类型的对象中。

                格式： filter(boolfunction, iterable)

                返回： filter对象,是一个迭代器

                

    * map():    会根据提供的函数对指定序列做映射，第一个参数 function以参数序列中的每一个元素调用function函数，
                返回包含每次function函数返回值的map对象

                格式： map(function, iterable, ...)

                返回： map对象,是一个迭代器

* 生成器：

    * 生成器是一种迭代器(生成器类是迭代器类的子类)，是一种特殊的函数，使用yield操作将函数构造成迭代器。

    * 生成器定义的函数，有多个入口和多个返回值；对生成器执行next()操作，进行生成器的入口开始执行代码，
    yield操作向调用者返回一个值，并将函数挂起；挂起时，函数执行的环境和参数被保存下来；对生成器执行另一个next()操作时，
    参数从挂起状态被重新调用，进入上次挂起的执行环境继续下面的操作，到下一个yield操作时重复上面的过程。

    * Python有两种不同的方式提供生成器：

        * 生成器函数：常规函数定义，但是使用yield语句而不是return语句返回结果。
                     yield语句一次返回一个结果，在每个结果中间，挂起函数的状态，以便下次重它离开的地方继续执行

        * 在生成器函数中，从逻辑上有一个序列的yield语句抛出值以实现它能够实现迭代

                示例：
                    N=10
                    def gensquares(N):
                        for i in range(N):
                            yield i**2

                    generator_a = gensquares(N) # 实例化一个生成器
                    for item in range(N):
                        print(next(generator_a))

                * 实例化一个生成器函数作为生成器对象的方法是直接调用这个生成器函数

        * 生成器表达式： 类似于列表推导，但是，生成器返回按需产生结果的一个对象，而不是一次构建一个结果列表

* 生成器的相关网站：

    https://www.jianshu.com/p/2ef36cdfd3b3
    https://www.zhihu.com/question/20829330

"""
# def函数
def foo(arg1,arg2,arg3=1,*nkw,**kw):
    print(arg1)
    print(arg2)
    print(arg3)
    print(nkw)
    print(kw)
    foo.version = '1.0'

foo(10,20,30,40,50,fo=60,bar=70)
foo(10,20,arg3=10)
foo(10,20)

print(foo.version)

# lambda函数
power2 = lambda x:x**2

print(power2(2))

# filter()函数
def is_odd(n):
    return n % 2 == 1

newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(newlist))

# map()函数
map_1 = map(lambda x: x**2,range(6))
print(list(map_1))

map_2 = map(lambda x,y: x+y,[1,3,5],[2,4,6])
print(list(map_2))

# 生成器
N=10
def gensquares(N):  # 成生器函数
    for i in range(N):
        yield i**2

generator_a = gensquares(N) # 实例化一个生成器

for item in range(N):
    print(next(generator_a))