"""
列表和元组的相关笔记
"""

"""
# ********************* 列表的基本知识 ************************

* 列表list的方法：

    .count(obj)方法： 返回对象在列表中出现的次数

    .index(obj,i=0,j=len(list)): 返回list[k]=obj的第一个k值，并且k的范围在i<=k<j;否则引发ValueError异常

    .append(obj)方法： 追加一个或几个元素到列表中

    .extend(iter)方法： 把可迭代对象iter添加到列表中

    .remove(obj)方法： 从列表中删除对象obj

    .insert(index,obj)方法：在索引量为index的位置插入对象obj

    .pop(index=-1)方法： 删除并返回指定位置的对象，默认是最后一个对象

    .reverse()方法: 原地翻转列表

    .sort(func=None,key=None,reverse=False): 以指定的方式排序列表中的成员，如果func和key参数指定，则按照指定的方式比较各个元素，
                                             如果reverse标志被置为True,则列表以反序排列

* 浅拷贝与深拷贝：

    * 对于不可变类型来说，a=b意味着a对b的深拷贝
    
        如：>>> a=1                 >>> a='abc'             >>> a=(1,2,3)
            >>> b=a                 >>> b=a                 >>> b=a
            >>> a=2                 >>> a='cdf'             >>> a=(4,5,6)
            >>> b                   >>> b                   >>> b
            1                       abc                     (1,2,3)

    * 对可变类型列表来说，a=b只是a对b的浅拷贝，当b变化时，a也随之变化

        如：>>> a=[1,2,3]
            >>> b=a
            >>> a.append(4,5,6)
            >>> b
            [1,2,3,4,5,6]

        注意：
        
            * 浅拷贝是列表类型的默认拷贝方式，对列表来说，子对象与父对象同时作的是浅拷贝
        
            * 完全的切片操作(b=a[:])和工厂函数(b=list(a))也都是浅拷贝

            * 如果要实现深拷贝的话，要用copy模块中的.deepcopy()函数，
                
                如：>>> import copy
                    >>> a=[1,2,3]
                    >>> b=copy.deepcopy(a)
                    >>> a.append(4,5,6)
                    >>> b
                    [1,2,3] 
  
"""
#%%
alist = [1,2,3,4,5]
print(alist.count(2))
print(alist.index(3))
alist.append(6)
print(alist)
alist.remove(3)
print(alist)
alist.reverse()
print(alist)
alist.sort()
print(alist)

a=[1,2,3]
b=a
a.append(4)
print(a,b)
import copy
c=copy.deepcopy(a)
a.append(5)
print(a,c)

"""
# ********************* 元组的基本知识 ************************

* 元组tuple是不可变类型，但是元组包含的可变对象却是可以改变的

    如： t=([1,2],3,4), 可以令t[0][1]=5, 则t=([1,5],3,4)

* 单元素元组：如果元组中只包含一个对象obj，即len(t)=1，则该元组应记为

                    t = (obj,) [注意后面的逗号]
             如果不用逗号的话，(obj)表示的就是obj对象本身，而不是只有一个对象的元组

* 元组的方法：

    .count(obj)方法： 返回对象在元组中出现的次数

    .index(obj,i=0,j=len(tuple)): 返回tuple[k]=obj的第一个k值，并且k的范围在i<=k<j;否则引发ValueError异常
    
"""

atuple = ([1,2],3,4)
print(atuple)
atuple[0][1]=5
print(atuple)
print(type((1)),type((1,)))
print(len(atuple))
print(atuple.count(3))


