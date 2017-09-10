"""
演示列表解析的用法
"""

# ************************************************************  列表解析  ************************************************************
# 语法：   
# 基本：               [expr(iter_var)  for iter_var in iterable]         {在for迭代前面加一个迭代变量的表达式}
# 带if的：             [expr(iter_var)  for iter_var in iterable if cond_expr]  {可以用if语句加一个判断条件，判断是否代入表达式}
# 可以嵌套：            [expr(iter_var1,inter_var2)  for iter_var1 in iterable1 for inter_var2 in iterable2] 

# 说明： (1) 列表解析相当于在for迭带器前面加了一个表达式，在循环时迭代变量分别代入表达式形成一个列表，这其中可以利用if来判断下每次是否要代入。
#       (2) 列表解析功能与lambda表达式类似，但用起来较lambda简单


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
