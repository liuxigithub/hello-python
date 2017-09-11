"""
示例Python中的命令行参数(Command Line Arguments)的使用
"""

# python中是通过sys模块中的sys.argv来实现命令行参数的，sys.argv是命令行参数的例表，和C语言一样，它接收到的参数转化为字符串列表, 但不一样的是它不需要指定参数个数。
# 输入格式：python para1(文件路径), para2, para3,...
# python中自带两个命令行参数的辅助模块：getopt模块和optparse模块。


# 求两个数的最大公约数
import sys
import math
gcd = math.gcd(int(sys.argv[1]),int(sys.argv[2])) # 因为是字符串列表，所以使用前要先转化为整数
print("The GCD of {0} and {1} is {2}".format(sys.argv[1], sys.argv[2], gcd))