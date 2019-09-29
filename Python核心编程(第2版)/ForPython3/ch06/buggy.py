#!/usr/bin/env python

#
#
while True:

    #
    num_str = input('Enter a number: ')

    #
    try:
        #
        num_num = int(num_str)

        #
        break

    #
    except ValueError:
        print("invalid input... try again")

#
fac_list = list(range(1, num_num+1))
print("BEFORE:", repr(fac_list))

#
i = 0

#
while i < len(fac_list):

    #
    if num_num % fac_list[i] == 0:
        del fac_list[i]
        i = i -1 

    #
    i = i+1

#
print("AFTER:", repr(fac_list))
