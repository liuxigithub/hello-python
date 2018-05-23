"""
集合的相关笔记
a good ref.: https://blog.csdn.net/liang19890820/article/details/72654921
"""

"""
# ********************* 集合的基本知识 ************************

* 集合对象是一组无序排列的可哈希的值,即集合中的元素必须是不可变类型

* 集合有两种不同的类型，可变集合(set)和不可变集合(frozenset)

* 对可变集合，可以添加和删除元素(不可哈希)，对不可变集合则不能(可哈希)

* 集合支持用in/not in成员关系操作符检查成员

* 集合长度可用len()查看

* 集合是一个可迭代类型

* 集合中的元素具有互异性,相同的元素会自动合一

* 要创建集合set，需要将所有项（元素）放在花括号{}内，以逗号分隔

        如：        >>> s={1,2,3}
                    >>> s
                    {1,2,3}

* 利用工厂方法set()/frozenset()也可以创建集合, 接受的是可迭代对象
    即： set([iterable])/frozenset([iterable])

        如：        >>> t=set('hello')
                    >>> t
                    {'e', 'o', 'l', 'h'}

* 适用于集合的操作符

    * 适用所有集合：

                obj in s           成员测试，obj是集合s的成员吗？  
                obj not in s       成员测试，obj不是集合s的成员吗？  
                  s == t           等价测试，s和t是否具有完全相同的元素
                  s != t           不等价测试
                  s < t            真子集测试，s是否是t的真子集
                  s <=t            子集测试，s是否是t的真子集，等价于方法 s.issubset(t)
                  s > t            真超集测试，s是否是t的真超集
                  s >=t            超集测试，s是否是t的超集，等价于方法 s.issuperset(t)
                  s | t            得到s和t的并集，等价于方法 s.union(t)
                  s & t            得到s和t的交集，等价于方法 s.intersection(t)
                  s - t            补集操作，是s中的元素，而不是t中的元素，等价于方法 s.difference(t)
                   s^t             对称差分操作，是s或t中的元素，但不是s和t的共有元素，等价于s.symmetric_difference(t)

    * 仅适用于可变集合：

                s |= t              将t中的成员添加到s，相当于s=s|t,等价于s.update(t)
                s &= t              将s修改为s和t的交集，相当于 s=s&t, 等价于s.intersection_update(t)
                s -= t              将s修改为s与t的补集，相当于 s=s-t, 等价于s.difference_update(t)
                s ^= t              将s修改为s对t的对称差分集，相当于s=s^t, 等价于s.symmetric_difference_update(t)

* 集合的内建方法

    * 适用所有集合：

            s.issubset(t)               作用： 返回s<t
            s.issuperset(t)             作用： 返回s>t
            s.union(t)                  作用： 返回s|t
            s.intersection(t)           作用： 返回s&t
            s.difference(t)             作用： 返回s-t
            s.symmetric_difference(t)   作用： 返回s^t
            s.isdisjoint(t)             作用： 如果s与t交集为空则返回True,否则Flase
            s.copy()                    作用： 返回一个新集合，它是s的浅复制,即深拷贝父对象，浅拷贝子对象

    * 仅适用于可变集合：

            s.update(t)                         作用： s |= t
            s.intersection_update(t)            作用： s &= t
            s.difference_update(t)              作用： s -= t
            s.symmetric_difference_update(t)    作用： s ^= t
            s.add(obj)                          作用： 将对象obj添加到s
            s.remove(obj)                       作用： 将对象obj从s中删除，如果obj不是s的元素，则报KeyError错误
            s.discard(obj)                      作用： 从s中删除对象obj,如果obj不是s的元素，则不作任何操作
            s.pop()                             作用： 删除并返回任意的集合元素（如果集合为空，会引发 KeyError）
            s.clear()                           作用： 删除集合中的所有元素

* 集合可能用到的内建函数： all(), any(), enumerate(), len(), max(), min(), sorted(), sum()...

"""

s={1,2,3}
print(type(s),type(frozenset(s)))
print(1 in s)

t=set('hello')
print(t)