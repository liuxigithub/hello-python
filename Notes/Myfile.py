"""
Python文件演示
"""
# -*- coding: utf-8 -*-
#encoding=utf-8

"""
# ********************************  文件用法汇总  ********************************
# 工厂函数： open()和file() [这两个函数的功能完全一样,两者都是返回一个文件对象, 利用 encoding = "utf-8"来指示编码，默认用的ansi]

# 内建方法：
#    读取： (1) .read(): 从当前指针处开始读取字节, 默认情况下读到文件尾，也可用size参数指定最大读取大小, 返回读取文本的字符串.
#          (2) .readline(): 从当前指针读取直到下一个行结束符，也可用size参数指定最大读取大小, 返回读取文本的字符串.
#          (3) .readlines(): 从当前指针读取直至文件尾，返回一个字符串列表，每项字符串都是所读取的一行.
#    写入： (1) .write(): 把含有文本数据或二进制数据块的字符串写入到文件中去.
#          (2) .writelines(): 接收字符串列表将其写入文件。注意，行结束符并不会被自动加入,所以如果需要的话，必须在调用writelines()前给每行结尾加上行结束符.
#    特别注意： (1)读取和写入字符串时用的都用的是open中指定的编码格式 (2)如果是以二进制方式打开的文件,则读取和写入都是二进制类型的,而不是字符串或字符串列表

# 文件内指针的移动：
#    .seek(offset [,from]): 移动文件内指针到某一位置，from是指偏移量的参考位置，0(默认)代表从文件首算起，1代表从当前位置算起，2代表从文件尾算起; offset是指的偏移量, 正表示往文件尾方向，负表示往文件头方向.
#    .tell(): 返回当前文件内指针的位置，从文件首算起，单位为字节.

# 文件迭代: 
#       file是一个可迭代类型，迭代方式是依次读取每行得到的字符串赋值给迭代变量.
#       文件迭代格式： for eachline in file_obj

# 其它方法:
#   (1) .close(): 关闭文件.
#   (2) .fileno(): 返回打开文件的描述符，用于一些底层操作.
#   (3) .flush():  直接把内部缓冲区中的数据立刻写入文件，而不是被动地等待输出缓冲区被写入(刷新缓存区).
#   (4) .truncate(): 将文件截取到当前指针位置.

# 文件内建属性:
#   (1) .closed: 判断文件是否关闭.
#   (2) .encoding: 文件编码方式.
#   (3) .mode: 访问模式.
#   (4) .name: 文件名.
#   (5) .newlines: 未读到行分隔符时为None, 只有一种行分隔符时返时一个字符串，有多种时是所有行分隔符的字符串列表.
"""



f = open('Abstract.txt','r+', encoding="utf-8")
print("read()方法： "+f.read())

print('')
f.seek(0)
print("readline()方法： "+f.readline())

print('')
f.seek(0)
print("readlines()方法： ", f.readlines())

print("")
print("write()方法： " )
f.write(u"\n\n 测试write()方法 \n")

print("writelines()方法： " )
f.writelines(['writelines()方法测试1',' writelines()方法测试2'])

print("tell()方法：", f.tell())

#print("truncate()方法:")
#f.truncate(780)

# 文件对象是一个迭代器，具有__next__()方法
f.seek(0)
print(f.__next__())
print(f.__next__())

# 文件属性
print("closed属性：", f.closed)
print("encoding属性：", f.encoding)
print("mode属性：", f.mode)
print("name属性：", f.name)
print("newlines属性:",repr(f.newlines))

f.colse()
