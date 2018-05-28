# -*- coding: utf-8 -*-
'''
找方程x^n+y^n+z^n=w^n 的解
'''

N=101
pw = 2
print('N=',N)
num = 0

print('-'*12+' start '+'-'*12)
for x in range(1,N):
  for y in range(x,N):
    for z in range(y,N):
      for w in range(z,N):
        if x**pw+y**pw+z**pw == w**pw:
          print('x=',x,', y=',y,', z=',z,', w=',w)
          num +=1

print('-'*12+' end '+'-'*12)
print('num=',num)
input()
