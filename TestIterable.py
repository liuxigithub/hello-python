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
print(isinstance(enumerate(range(5)),Iterable)) # enumerate 对象
print(isinstance(zip([],[]),Iterable))  # zip对象
print(isinstance(reversed([]),Iterable)) # reversed 对象
