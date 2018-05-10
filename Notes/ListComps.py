"""
演示列表解析和生成器表达式的用法
"""

"""
# ************************************************************  列表解析  ************************************************************
# 语法：   
# 基本：               [expr(iter_var)  for iter_var in iterable]         {在for迭代前面加一个迭代变量的表达式}
# 带if的：             [expr(iter_var)  for iter_var in iterable if cond_expr]  {可以用if语句加一个判断条件，判断是否代入表达式}
# 可以嵌套：            [expr(iter_var1,inter_var2)  for iter_var1 in iterable1 for inter_var2 in iterable2] 

# 说明： (1) 列表解析相当于在for的迭代结构前面加了一个表达式，在循环时迭代变量分别代入表达式形成一个列表，这其中可以利用if来判断下每次是否要代入。
#       (2) 列表解析功能与lambda表达式类似，但用起来较lambda简单



# ************************************************************  生成器表达式  ************************************************************
# 语法： 将中括号改为小括号   
# 基本：               (expr(iter_var)  for iter_var in iterable)         
# 带if的：             (expr(iter_var)  for iter_var in iterable if cond_expr)
# 可以嵌套：            (expr(iter_var1,inter_var2)  for iter_var1 in iterable1 for inter_var2 in iterable2) 
# 说明：  (1)相比于列表解析，生成器表达式并不会生成一个像列表一样的实实在在的可能占据很大内存容器，生成器只会记录用来迭代的迭代变量的项以及用来解析的算法，
#           等生成器具体"被用到"时，再依次去解析出它的项来。
#        (2)显然，生成器表达式和列表解析的效果是一样的，但是生成器表达式更节约内存些，更适用于较大的迭代。
#        (3)生成器表达式会返回一个生成器对象，这是一个可迭代对象,所以可以用于for的迭代结构中。
#        (4)生成器可用函数netx()依次取得下一个元素。
"""

print(type([x**2 for x in range(10)]))
print([x**2 for x in range(10)])
print([x for x in range(10) if x%2]) # 选出奇数
print([(x,y) for x in range(5) for y in range(5)])

# ********************   统计一个文本中有多少行，多个单词和字符    ********************
f = open('Abstract.txt','r')
print('lines:', len([eachline for eachline in f])) # 统计行

f.seek(0) # 文件指针重新位于文件首
print('words:', len([eachword for eachline in f for eachword in eachline.split()])) # 统计单词数

f.seek(0) # 文件指针重新位于文件首
print('chars:', len([eachchar for eachline in f for eachword in eachline.split() for eachchar in eachword])) # 统计字符数
f.seek(0) # 文件指针重新位于文件首
print('chars:', sum([len(eachword) for eachline in f for eachword in eachline.split()])) # 统计字符数


# 生成器表达式
print(type(x**2 for x in range(10)))
g = (x**2 for x in range(10))
print(next(g))
print(next(g))
print(next(g))
for i in g:
    print(i)
