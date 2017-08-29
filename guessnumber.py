# -*- coding: utf-8 -*-
'''
猜数字游戏
'''
import time

result = 30
print("input your number(1~100):")
guess = int(input())

while guess != result:
	if guess > result:
		print("your input is bigger,please input again:")
	elif guess < result:
		print("your input is smaller,please input again:")
	guess = int(input())
print("Congratulation! you get it")
print("result = {}".format(result))
time.sleep(10)
exit()