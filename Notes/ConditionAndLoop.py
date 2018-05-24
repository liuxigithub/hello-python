"""
条件和循环的相关笔记
"""

"""
# *********************  if语句 ************************

* 单行if语句：

        * 如果一个复合语句(如if子句, while或for循环)的代码块仅仅包含一行代码，那么它可以和前面的语句写在同一行上：

            if expression: one_line_code

* 一般if语句的格式：

        if expression1:
            expr1_true_suite
        elif expression2:
            expr2_true_suite
                .
                .
        elif expressionN:
            exprN_true_suite
        else:
            none_of_the_above_suite

    * 在上面的结构中，if块有仅只有一个(1),elif块可以没有，也可以有许多个(0,1,2,...),else块可以没有但最多只能有一个(0,1)

* 条件表达式(三元操作符)：

        * 格式：    X if C else Y

        * 说明：如果条件表达式C是真的话，整个表达式的结果为X,否则为Y

        * 举例： smaller = x if x<y else y
"""

print(4 if False else 5)

"""
# *********************  循环语句 ************************

* while语句：

        格式：  
                while expression:
                    suite_to_repeat
                [else:
                    suite_be_done_after_loop ]
                
        说明： 后面的else可有可无，else子句里面的内容只在循环结束后执行，
               如果suite_to_repeat中含有break,则else子句中的内容也会被跳过

* for语句：

        * for语句可以用来迭代任何一个可迭代对象

        * 格式：
                for iter_var in iterable:
                    suite_to_repeat
                [else:
                    suite_be_done_after_loop ]

                说明：  * 上面else的用法同while,iter_var是迭代变量，iterable是可迭代对象

        * 对于任何一个可迭代对象，都有它本身的迭代规则，比如说：对于一个列表而言，当你用一个迭代变量
          去迭代它时，迭代变量会遍历它的第一个维度，即alist[0],alist[1],...,alist[len(alist)-1]

* 可迭代变量的三种方式：

    * 项迭代：

                alist=['Hello','Python','World']
                for word in alist:
                    print(word,end=' ')

                => Hello Python World

    * 索引迭代(如果可索引的话)：

                alist=['Hello','Python','World']
                for index in range(len(alist)):
                    print(alist(index),end=' ')

                => Hello Python World

    * 同时使用索引-项(借助enumerate函数)或者项-项(借助zip函数)来迭代：

                albums=('Poe','Gaudi','Freud','Poe2')
                years=(1976, 1987, 1990, 2003)

        * 索引-项迭代：借助enumerate()分组

                for i, album in enumerate(albums):
                    print(i,album)

        * 项-项迭代： 借助zip()分组

                for year, album in zip(years,albums):
                    print(year,album)

* break语句： 结束当前循环，跳到下条语句，如果循环带else的话，也会跳过else

* continue语句： 终止当前循环，并忽略剩余语句，启动该循环的下一次迭代

        注意：在开始下一次迭代前，如果是条件循环，将验证条件表达式；
              如果是迭代循环，将验证是否还有元素可以迭代

* pass语句： pass语句什么都不做，仅用来占位    

"""

mylist = [1,2,3,[4,5,6]]
for var in mylist:
    print(var)

mylist2=[[1,2,3],[4,5,6]]
for var1 in mylist2:
    for var2 in var1:
        print(var2)

albums=('Poe','Gaudi','Freud','Poe2')
years=(1976, 1987, 1990, 2003)

for i, album in enumerate(albums):
    print(i,album)

for year, album in zip(years,albums):
    print(year,album)

"""
# *********************  迭代器 ************************
* 迭代是Python最强大的功能之一，是访问集合元素的一种方式

* 迭代器是一个可以记住遍历的位置的对象

* 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退

* 迭代器有两个基本的内建函数：iter()和next()

        * iter(): 迭代器工厂函数，把可迭代对象转成迭代器

        * next(): 得到迭代器的下一个项目

* 字符串，列表或元组对象都可用于创建迭代器

* 判断一个对象是否是迭代器的方法：

           from collections import Iterator 
           isinstance(s,iterator)

"""

list=[1,2,3,4]
it = iter(list)
print (next(it))
print (next(it))
    
