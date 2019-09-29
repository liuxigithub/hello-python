
"""
计算加减法
"""

from operator import add, sub
from random import randint, choice

ops = {'+': add, '-': sub}
MAXTRIES = 2

def doprob():
    op = choice('+-')
    nums = [ randint(1,10) for i in range(2) ] # 生成一个具有两个随机元素的列表，列表解析的又一个好例子
    nums.sort(reverse=True)
    ans = ops[op](*nums)
    pr = '%d %s %s = ' % (nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(input(pr)) == ans:
                print('correct')
                break
            if oops == MAXTRIES:
                print('sorry... the answer is\n%s%d' % (pr, ans))
            else:
                print('incorrect... try again')
                oops += 1
        except (KeyboardInterrupt,
                EOFError, ValueError):
            print('invalid input... try again')

def main():
    while True:
        doprob()
        try:
            opt = input('Again? [y] ').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == '__main__':
    main()
