"""
利用collections模块的Iterable类型判断来判断一个对象是否是可迭代对象
"""
from collections import Iterable

print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance("",Iterable))
print(isinstance(range(10),Iterable))
print(isinstance({},Iterable))
print(isinstance({}.keys(),Iterable))
print(isinstance({}.values(),Iterable))
print(isinstance({}.items(),Iterable))
print(isinstance(set(''),Iterable))
