from collections import Iterable
from collections import Iterator


print(isinstance([],Iterable),isinstance([],Iterator)) # list对象
print(isinstance((),Iterable),isinstance((),Iterator)) # tuple对象
print(isinstance("",Iterable),isinstance("",Iterator)) # string对象