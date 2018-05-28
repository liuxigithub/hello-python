"""
关于序列的一些知识学习
"""

"""
# ********************* 关于序列的基本知识 ************************

* 序列： 成员有序排列，并且可以通过下标偏移量访问到它的一个或者几个成员，这类Python类型统称为序列，包括字符串，列表和元组类型

* 序列的操作符：

    * 成员关系操作符： in   not in   [obj in seq : 判断obj元素是否包含在seq中]

        注意：当seq是字符串，in用于判断字符串obj中的所有字符是否包含在seq中，not in用于判断obj中是否存在不包含在seq中的字符，
             成员操作不是用来判断字符串的包含关系的

    * 连接操作符： +  [seq1 + seq2 : 连接序列seq1和seq2]

    * 重复操作符： *  [seq*expr/expr*seq: 序列重复expr次]

    * 索引/切片操作符： [],[:],[::]

            0    1    2    3    4    5        <--正向索引序号
            a    b    c    d    e    f 
           -6   -5   -4   -3   -2   -1        <--逆向索引序号

            * 索引[]: seq[index]   
                
                注意:  1. index可正可负，对应于正索引与反向索引，如seq[1]=b,seq[-2]=e
                      2. 可连续索引：如：x=['abc','df']；x[0][1]

            * 切片[:]: seq[sta_ind:end_ind]

                注意： 1. sta_ind和end_ind可用正向也可用逆向索引，但要保证总顺序还是从左向右的，否则返回空，如seq[4:-5]=''
                      2. sta_ind 和 end_ind可缺省，则默认为最开始或最末尾

            * 步长切片[::]: [::ins], ins表示步长，可正可负,如seq[::-1]表示逆序

* 序列可能用到的内建函数：

    * enumerate(iter): 接受一个可迭代对象，返回一个enumerate对象(也是一个可迭代对象)，该对象成生由iter的每个元素的index值和item值组成的元组

    * len(seq): 返回序列的长度

    * max(iter): 返回可迭代对象中的最大值

    * min(iter): 返回可迭代对象中的最小值

    * reversed(seq): 返回一个序列的逆序的迭代器

    * sorted(iter): 返回可迭代对象的一个有序列表

    * sum(seq,init=0): 返回序列和可选参数init的总和
"""

print('*'*5 + 'Hello'+' '+'World'+'*'*5)
print('ax' in 'abc','ab' in 'abc','ax' not in 'abc')
x='abcdef'
print(x[1:-1])
print(x[-2:1])
print(len(x))
print(list(reversed(x)))
