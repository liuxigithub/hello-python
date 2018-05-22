a=[1,2,3]
b=a
a.append(4)
print(a,b)
import copy
c=copy.deepcopy(a)
a.append(5)
print(a,c)