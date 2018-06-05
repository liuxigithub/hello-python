"""
作用域的相关笔记
"""

"""
# *********************  作用域的相关知识 ************************

* Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的

* 变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称

* Python中只有模块(module),类(class)以及函数(def、lambda)才会引入新的作用域，
  其它的代码块(如 if/elif/else/、try/except、for/while等)是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问

* Python的作用域: 共四种

    * L (Local) 局部作用域  :  指当前函数或方法所在的作用域

    * E (Enclosing) 闭包函数外的函数中

    * G (Global) 全局作用域 : 当前代码所在模块的作用域

    * B (Built-in) 内建作用域

* LEGB原则：

        当变量在命名空间中查找对应的对象时，以 L –> E –> G –>B 的规则查找，
        即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找

* 局部作用域里的代码可以读外部作用域（包括全局作用域）里的变量，但不能更改它。
    一旦进行更改，就会将其看成是一个局部变量。而如果在更改前又进行了读取操作，则会抛出异常

* global关键字： 可以利用global关键字来声明一个变量是全局变量，它的作用范围为整个模块

        * global可实现在函数内修改外部变量，如

            gcount = 0

            def global_test():
                global gcount
                gcount +=1
                print (gcount)
            global_test()

* nonlocal关键字： 用来在函数或其他作用域中使用外层(非全局)变量

        * 如：

            def make_counter(): 
                count = 0 
                def counter(): 
                    nonlocal count 
                    count += 1 
                    return count 
                return counter 

            def make_counter_test(): 
                mc = make_counter()
                print(mc())
                 print(mc())
                print(mc())

            make_counter_test()

* 相关网页：

    https://blog.csdn.net/youngbit007/article/details/64905070
    https://www.cnblogs.com/itech/archive/2011/12/31/2308640.html

"""

#%% 全局变量与局域变量

total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total

sum( 10, 20 )
print ("函数外是全局变量 : ", total)

#%% global语句

gcount = 0

def global_test():
    global gcount
    gcount +=1
    print (gcount)
global_test()

#%% nonlocal语句
def make_counter(): 
    count = 0 
    def counter(): 
        nonlocal count 
        count += 1 
        return count 
    return counter 

def make_counter_test(): 
  mc = make_counter()
  print(mc())
  print(mc())
  print(mc())

make_counter_test()