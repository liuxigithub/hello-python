"""
利用collections模块的Iterable类型判断来判断一个对象是否是可迭代对象
"""
from collections import Iterable

print(isinstance([],Iterable)) # list对象
print(isinstance((),Iterable)) # tuple对象
print(isinstance("",Iterable)) # string对象
print(isinstance(range(10),Iterable)) # range对象
print(isinstance({},Iterable)) # dict对象
print(isinstance({}.keys(),Iterable)) # keys对象
print(isinstance({}.values(),Iterable)) # values对象
print(isinstance({}.items(),Iterable)) # items对象
print(isinstance(set(''),Iterable)) # set对象
print(isinstance((x for x in range(5)),Iterable)) # generator 对象

# 迭代器
print(isinstance(zip([],[]),Iterable))  # zip对象, 迭代器
print(isinstance(reversed([]),Iterable)) # reversed 对象, 迭代器
print(isinstance(enumerate(range(5)),Iterable)) # enumerate 对象， 迭代器
print(isinstance(open('.txt','w'),Iterable)) # 文件对象, 迭代器, 迭代方式为读取文件的每行并赋值给迭代变量

# iter()生成的迭代器的各种对象，iter()对迭代器返回的是相当类型的迭代器，即不做任何操作
print(isinstance(iter([]),Iterable)) # iter生成的迭代器, list_iterator对象
print(isinstance(iter(()),Iterable)) # iter生成的迭代器, tuple_iterator对象
print(isinstance(iter(""),Iterable)) # iter生成的迭代器, str_iterator对象
print(isinstance(iter(range(10)),Iterable)) # iter生成的迭代器, range_iterator对象
print(isinstance(iter({}),Iterable),isinstance(iter({}.keys()),Iterable)) # iter生成的迭代器, dict_keyiterator对象
print(isinstance(iter({}.values()),Iterable)) # iter生成的迭代器, dict_valueiterator对象
print(isinstance(iter({}.items()),Iterable)) # iter生成的迭代器, dict_itemiterator对象
print(isinstance(iter(set('')),Iterable)) # iter生成的迭代器, set_iterator对象


