"""
利用collections模块的Iterable类型判断来判断一个对象是否是可迭代对象
"""
from collections import Iterable
from collections import Iterator

# 可迭代对象而不是迭代器
print(isinstance([],Iterable),isinstance([],Iterator)) # list对象
print(isinstance((),Iterable),isinstance((),Iterator)) # tuple对象
print(isinstance("",Iterable),isinstance("",Iterator)) # string对象
print(isinstance(range(10),Iterable),isinstance(range(10),Iterator)) # range对象
print(isinstance({},Iterable),isinstance({},Iterator)) # dict对象
print(isinstance({}.keys(),Iterable),isinstance({}.keys(),Iterator)) # keys对象
print(isinstance({}.values(),Iterable),isinstance({}.values(),Iterator)) # values对象
print(isinstance({}.items(),Iterable),isinstance({}.items(),Iterator)) # items对象
print(isinstance(set(''),Iterable),isinstance(set(''),Iterator)) # set对象

print()

# 迭代器
print(isinstance(zip([],[]),Iterable),isinstance(zip([],[]),Iterator))  # zip对象, 迭代器
print(isinstance(reversed([]),Iterable),isinstance(reversed([]),Iterator)) # reversed 对象, 迭代器
print(isinstance(enumerate(range(5)),Iterable),isinstance(enumerate(range(5)),Iterator)) # enumerate 对象,迭代器
print(isinstance(open('.txt','w'),Iterable),isinstance(open('.txt','w'),Iterator)) # 文件对象, 迭代器, 迭代方式为读取文件的每行并赋值给迭代变量
print(isinstance((x for x in range(5)),Iterable),isinstance((x for x in range(5)),Iterator)) # generator对象,迭代器

print()

# iter()生成的迭代器的各种对象，iter()对迭代器返回的是相当类型的迭代器，即不做任何操作
print(isinstance(iter([]),Iterable),isinstance(iter([]),Iterator)) # iter生成的迭代器, list_iterator对象
print(isinstance(iter(()),Iterable),isinstance(iter(()),Iterator)) # iter生成的迭代器, tuple_iterator对象
print(isinstance(iter(""),Iterable),isinstance(iter(""),Iterator)) # iter生成的迭代器, str_iterator对象
print(isinstance(iter(range(10)),Iterable),isinstance(iter(range(10)),Iterator)) # iter生成的迭代器, range_iterator对象
print(isinstance(iter({}),Iterable),isinstance(iter({}.keys()),Iterable), \
      isinstance(iter({}),Iterator),isinstance(iter({}.keys()),Iterator)) # iter生成的迭代器, dict_keyiterator对象
print(isinstance(iter({}.values()),Iterable),isinstance(iter({}.values()),Iterator)) # iter生成的迭代器, dict_valueiterator对象
print(isinstance(iter({}.items()),Iterable),isinstance(iter({}.items()),Iterator)) # iter生成的迭代器, dict_itemiterator对象
print(isinstance(iter(set('')),Iterable),isinstance(iter(set('')),Iterator)) # iter生成的迭代器, set_iterator对象
