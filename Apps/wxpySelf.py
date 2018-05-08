"""
wxpy使用尝试
ref:https://zhuanlan.zhihu.com/p/27566793
wxpy官方手册：http://wxpy.readthedocs.io/zh/latest/index.html
主要只学习了如何自己给自己发信息
"""
from wxpy import *

# 初始化机器人
bot = Bot(cache_path=True)  # cache_path设为True表明使用登陆缓存
#bot = Bot(console_qr=True,cache_path=True) # 使用终端登陆时会在终端上打印二维码

# 通过文件助手给自己发信息
bot.file_helper.send('hello from wxpy!')


# 通过添加自身为好友来给自己发信息
friends = bot.friends() # 获取所有好友
while bot.self not in friends: # 如果自己还没有添加自己为好友，则在这里添加
    bot.self.add()
    bot.self.accept()
# 发信息给自己
bot.self.send('能收到吗？')
bot.self.send('Hello World, I am from wxpy!')

print("ending")