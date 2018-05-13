# -*- coding: utf-8 -*-

(a, b)= (0, 1)
i = 0
while i < 50:
    print(b)
    (a, b) = (b, a+b)
    i = i+1
#input()
  
print('name: {}, age: {}'.format('Liu xi',28))