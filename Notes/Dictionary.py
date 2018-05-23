"""
字典的相关笔记
"""

"""
# ********************* 字典的基本知识 ************************

* 字典是Python中唯一的映射类型，它是一个可变的容器对象

* 字典类型和序列类型的区别是存储和访问数据的方式不同，序列只能用数字类型的偏移量作键，而字典则可用其它类型作键

* 映射类型中的数据是无序排列的

* 字典数据以键-值对的形式组织，即(key:value,...), 

        如: dict={'name':'lx','age':28,'gender':'male'}

* 字典的工厂函数是dict()

        如：    >>> adict = dict((['name','lx'],['age',28],['gender','male']))
                {'name': 'lx', 'age': 28, 'gender': 'male'}

* 字典对象也可使用.fromkeys()方法来初始化,字典中元素具有相同的值，如果没给出，则默认为None

        如：    >>> ddict = {}.fromkeys(('x','y'),-1)
                {'x': -1, 'y': -1}

                >>> edict = {}.fromkeys(('x','y'))
                {'x': None, 'y': None}

* 字典的访问

        * 字典通过键值对的方式访问，即dict[key]=value,此时[]称为键查找操作符

        * 字典是可迭代典型，会直接迭代字典的key

            如：    >>> dict={'name':'lx','age':28,'gender':'male'}
                    >>> for key in dict:
                            print(key,dict[key])

        * 利用成员关系操作符in/not in 可以直接某个键是否存在于字典中

* 比较运算符作用下的字典：先比较长度，再比较键，最后比较值

* 字典中的每个键只能对应一个值，当有键发生冲突，即字典键重复赋值，取最后或最近的赋值

            如：    >>> dict={'age':10,'age':12}
                    {'age': 12}

* 删除字典元素

    * del dict['key']  # 删除键为'key'的条目

    * dict.clear()     # 删除字典dict中的所有条目

    * dict.pop('key')  # 删除并返回键为'key'的条目

* 字典类型的键必须要是可哈希的，一般采用数字或字符串类型

* 对象能否哈希可采用内建函数hash()来判断，它用返回对象的哈希值

        如：    >>> hash(1)             >>> hash([1,2])
                1                       TypeError: unhashable type: 'list'

* 字典的长度可用内建函数len()来查看

* 字典的内建方法

    .clear(): 删除字典中的所有条目

    .copy(): 深拷贝一个字典的父对象，而浅拷贝其子对象，也就是说新建了一个字典对象，但是里面的值还是原字典对像值的引用

    .fromkeys(seq.val=None): 创建并返回一个新字典，以seq中的元素做该字典的键，val做该字典中所有键对应的初始值

    .get(key,default=None): 对字典dict中的键key,返回它对应的值value，如果字典中不存在此键，则返回default的值

    .items(): 返回一个包含字典中键值对元组的dict_items类型对象，它是一个可迭代对象

    .keys(): 返回一个包含字典中键的dict_keys类型对象，它是一个可迭代对象
    
    .values(): 返回一个包含字典中值的dict_values类型对象，它是一个可迭代对象

    .pop(key[,default]): 如果字典中key键存在，删除并返回dict[key],如果key键不存在，且没有给出
                         default的值，则引发KeyError异常

    .popitem()：随机返回并删除字典中的一对键和值(一般删除末尾对)，如果字典已经为空，却调用了此方法，就报出KeyError异常

    .update(dict2): 将字典dict2的键-值对添加到字典中

    .setdefault(key,default=None): 如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值default，
                                   并返回 default ，default 默认值为 None。


"""

adict={'name':'lx','age':28,'gender':'male'}
print(adict['name'])
print('name' in adict)
for key in adict:
    print(key,adict[key],end=' ')

print()
print(hash(1))
print(len(adict))

for i in adict.items():
    print(i[0], i[1],end=' ')

print(adict.values(),'\n',adict.keys(),'\n',adict.items())

#%%
# .copy()方法
dict1 =  {'user':'runoob','num':[1,2,3]}
dict2 = dict1
dict3 = dict1.copy()
print(dict1 is dict3)

for x in dict1:
    print(id(x))

for x in dict3:
    print(id(x))

dict1['user']='root'
dict1['num'].remove(1)
print(dict1)
print(dict2)
print(dict3)