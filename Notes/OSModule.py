"""
os模块和os.path模块的介绍
"""

"""
# ********************************  os模块  ********************************
ref: http://www.runoob.com/python3/python3-os-file-methods.html

* 在python内部，文件系统的访问大都通过os模块来实现

* os模块的访问函数(常用)

        * os.chdir(path)： 改变当前工作目录

        * os.chmod(path, mode)：更改权限

        * os.getcwd()： 返回当前工作目录

        * os.listdir(path)： 返回path指定的文件夹包含的文件或文件夹的名字的列表

        * os.mkdir(path[, mode])： 以数字mode的mode创建一个名为path的文件夹

        * os.remove(path): 删除路径为path的文件。如果path是一个文件夹，将抛出OSError

        * os.removedirs(path): 递归删除目录

        * os.rename(src, dst): 重命名文件或目录，从src到dst

        * os.renames(old, new): 递归地对目录进行更名，也可以对文件进行更名

        * os.rmdir(path): 删除path指定的空目录，如果目录非空，则抛出一个OSError异常

"""


"""
# ********************************  os模块  ********************************
ref: https://www.cnblogs.com/renpingsheng/p/7065565.html

* os.path模块的访问函数:

        * abspath(): 返回一个目录的绝对路径

        * basename(): 返回一个目录的基名

        * dirname(): 返回一个目录的目录名

        * exists(): 测试指定文件是否存在

        * getatime(): 得到指定文件最后一次的访问时间

        * getctime(): 得到指定文件最后一次的改变时间

        * getmtime(): 得到指定文件最后一次的修改时间

        * getsize(): 得到得到文件的大小

        * isabs(): 测试参数是否是绝对路径

        * isdir(): 测试指定参数是否是目录名

        * isfile(): 测试指定参数是否是一个文件

        * islink(): 测试指定参数是否是一个软链接

        * ismount(): 测试指定参数是否是挂载点

        * join(): 将目录名和文件的基名拼接成一个完整的路径

        * realpath(): 返回指定文件的标准路径，而非软链接所在的路径

        * samefile(): 测试两个路径是否指向同一个文件

        * sameopenfile(): 测试两个打开的文件是否指向同一个文件

        * split(): 分割目录名，返回由其目录名和基名给成的元组

        * splitext(): 分割文件名，返回由文件名和扩展名组成的元组

"""