"""
利用以下事实求pi的值：在自然数中随机取两数，其互质的概率为6/(pi^2)
"""
from random import randint
import math

N_Sample = 10000000 # 样本数
N_Prime = N_Sample*1000 # N_Prime是所取素数的范围 

print('样本数N_sample=',N_Sample)

N_Coprime = 0 # 互素的数

print('*'*16)
for i in range(1,N_Sample+1):
    num_a = randint(1,N_Prime)
    num_b = randint(1,N_Prime) 
    if math.gcd(num_a,num_b) == 1:
        N_Coprime = N_Coprime + 1
    if i%100000 == 0:
        print('i = ',i,'       N_Coprime = ',N_Coprime,'       Pi = ',math.sqrt(6*i/N_Coprime))

print('*'*16+'done'+'*'*16+'\n')

Pi = math.sqrt(6*N_Sample/N_Coprime)

print('标准的Pi值为： ',math.pi)
print('计算得到的Pi值为： ',Pi)
input()