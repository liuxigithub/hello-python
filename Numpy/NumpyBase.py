"""
Numpy的基本操作
"""
#%% 创建数组
import numpy as np

# 由list或者tuple构建
a_list = np.array([[1,2],[3,4]],np.float)
a_tuple = np.array((1,2,3,4),np.float)
print('a_list=',a_list)
print('a_tuple=',a_tuple)

# 由函数构建
a_zeros = np.zeros((2,3),np.complex) # zeros()
print('a_ones=',a_zeros)
a_arange = np.arange(1,10,2) # arange()
print('a_arange=',a_arange)
a_ones = np.ones((2,4),np.complex) # ones()
print('a_ones=',a_ones)
a_linspace = np.linspace(0,1,10) # linspace
print('a_linspace=',a_linspace)
a_x = np.arange(1,10,2)
a_y = np.arange(1,10,2)
a_meshgrid = np.meshgrid(a_x,a_y)
print(a_meshgrid)

#%% 数组属性
import numpy as np
a_exa = np.array([[1,2],[3,4]],np.float)
# dtype:数据类型
print(a_exa.dtype) 
# ndim：数据维数
print(a_exa.ndim)
# shape: 形状
print(a_exa.shape)
# size: 总元素的个数
print(a_exa.size)
# itemsize: 数组中各个元素所占用的字节数大小
print(a_exa.itemsize)
# nbytes: 整个数组所需的字节数量
print(a_exa.nbytes)
# T属性:数组的转置数组
print(a_exa)
print(a_exa.T)
# real/imag: 数且的实部/虚部
print(a_exa.real)
print(a_exa.imag)

#%% 运算符
import numpy as np
# numpy对python的基本运算符都作了重载，其意义与Matlab中的一致
exa_a = np.array([[1,2],[3,4]],np.int)
exa_b = np.array([[5,6],[7,8]],np.int)
print(exa_a+exa_b)  # +
print(exa_a-exa_b)  # -
print(exa_a*exa_b)  # *
print(exa_a/exa_b)  # /
print(exa_a//exa_b) # //
print(exa_a**2)     # **

#%% 索引和切片
import numpy as np
from matplotlib import pyplot as plt
# numpy对象的索引和切片的方法与原生python一致
exa = np.array([[1,2,3,4],[5,6,7,8]],np.int)
print(exa[1,2],exa[1:2,0:3])






