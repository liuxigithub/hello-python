"""
在一定范围内验定哥德巴赫猜想
"""
import math

Max_even = 10000  # 偶数的上限,Max_even>=6

# 一列语句生成素数列表
PrimeList = list(filter(lambda x: all(map(lambda p: x % p != 0,range(2, int(math.sqrt(x))+1))), range(2, Max_even))) 

EvenList = list(range(6,Max_even+1,2)) # 偶数列表

Spec_case = 0 # 不满足的个数

print('*'*8+'验证哥德巴赫猜想'+'*'*8)

for i_even in EvenList:
    for i_prime in PrimeList:
        if i_even-i_prime in PrimeList:
            print('%d = %d + %d'%(i_even,i_prime,i_even-i_prime))
            break
    else:
        Spec_case = Spec_case + 1

print()
print('Max_even = %d, Spec_case = %d'%(Max_even, Spec_case))

