#!/usr/bin/env python
'''
作为习题6.2的解，补充了单字符和关键字的情形
'''

import string
import keyword

alphas = string.ascii_letters + '_'
nums = string.digits

print('Welcome to the Identifier Checker v1.0')
print('Testees must be at least 2 chars long.')
inp = input('Identifier to test? ')

flag = 0

if len(inp) > 1:

    if inp[0] not in alphas:
        print('''invalid: first symbol must be alphabetic''')
    elif inp in keyword.kwlist:
        '关键字判断'
        print('The keyword can not be an identifier')
    else:
        for otherChar in inp[1:]:

            if otherChar not in alphas + nums:
                print('''invalid: remaining symbols must be alphanumeric''')  
                flag = 1
                break
   
        if flag !=1 :
            print("okay as an identifier")
else:
    
    '单字符串情形'
    if inp in alphas:
        print("okay as an identifier")
    else:
        print('''invalid: remaining symbols must be alphanumeric''')
        
        
