"""
字符串对象的相关方法
ref: http://www.cnblogs.com/Xavierr/articles/3655897.html
ref: 《Python核心编程(第二版)》P122
"""
import string
Str = 'Mr Liu Hello'

# 大小写转换
print(Str.lower()) # 转化成小写
print(Str.upper()) # 转化成大写
print(Str.swapcase()) # 大小写互换
print(Str.capitalize()) # 首字母大写
print(Str.title()) # 所有首字母大写, 其它字母小写
print(string.capwords(Str)) # 功能同str.title(),但这是string模块中的方法

# 字符串在输出时的对齐
print(Str.ljust(12)) # .ljust(width,[fillchar]), 输出width个字符，S左对齐，不足部分用fillchar填充，默认的为空格
print(Str.rjust(12)) # .rjust(width,[fillchar]), 同上，右对齐
print(Str.center(12))# .center(width,[fillchar]), 同上，中间对齐
print(Str.zfill(12)) # .zfill(width), 把Str变成width长，并在右对齐，不足部分用0补足 

# 字符串中的搜索和替换
print(Str.find('L')) # .find(substr, [start, [end]]), 返回Str中出现substr的第一个字母的标号，如果Str中没有substr则返回-1。start和end作用就相当于在S[start:end]中搜索
print(Str.index('L')) # .index(substr, [start, [end]]), 与.find()相同，只是在Str中没有substr时，会返回一个运行时错误 
print(Str.rfind('l') ) # .rfind(substr, [start, [end]]), 返回Str中最后出现的substr的第一个字母的标号，如果Str中没有substr则返回-1，也就是说从右边算起的第一次出现的substr的首字母标号
print(Str.rindex('l')) # .rindex(substr, [start, [end]]), 与.rfind()相同，只是在Str中没有substr时，会返回一个运行时错误
print(Str.count('ell')) # .count(substr, [start, [end]]), 计算substr在Str中出现的次数 
print(Str.replace('l','L',2)) # .replace(oldstr, newstr, [count]), 把Str中的oldstar替换为newstr，count为替换次数
print('')
Str2 = ''*4+Str+''*3+'\n'
print(Str2)
print(Str2.strip(),Str2.strip('\n')) # .strip(rm), 删除Str字符串中开头、结尾处，位于rm删除序列的字符，直至不能找到相应的字符为准,当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
print(Str2.lstrip(),Str2.lstrip('\n')) # .lstrip(rm), 删除Str字符串中开头处，位于rm删除序列的字符，直至不能找到相应的字符为准,当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
print(Str2.rstrip(),Str2.rstrip('\n')) # .rstrip(rm), 删除Str字符串中结尾处，位于rm删除序列的字符，直至不能找到相应的字符为准,当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
Str3 = '\t'+Str
print(Str3,Str3.expandtabs(4)) # .expandtabs([tabsize]), 把Str中的tab字符替换没空格，每个tab替换为tabsize个空格，默认是8个 

# 字符串的分割和组合
print(Str.split(),Str.split(None,1)) # .split([sep, [maxsplit]]), 以sep为分隔符，把Str分成一个list。maxsplit表示最大分割的次数。默认的分割符为空白字符,此时输入为None, 总是全部分完， 此时maxsplit=-1
print(Str.rsplit(),Str.rsplit(' ',1)) # 相比于./split(), 它是从右边开始分的
Str4 = """
Mr
Liu
Hello
"""
Str5 = Str4.splitlines()
print(Str5) # .splitlines([keepends]), 把Str按照行分割符分为一个list，keepends是一个bool值，如果为真每行后而会保留行分割符
print(' '.join(Str5)) # 把seq代表的字符串序列，用S连接起来

# 字符串编码
Bytes = Str.encode('utf-8') # ./encode(encoding), 字符串按照encoding格式编码
print(Bytes.decode('utf-8'))

# 字符串的测试函数
# 这一类函数在string模块中没有，这些函数返回的都是bool值
print(Str.startswith("Mr"),Str.startswith("Li",3,5)) # .startswith(prefix[,start[,end]]), 是否以prefix开头
print(Str.endswith("llo"),Str.endswith("iu",2,6)) # .endswith(suffix[,start[,end]]), 是否以以suffix结尾
print(Str.isalnum()) # .isalnum(), 是否全是字母和数字，并至少有一个字符
print(Str.isalpha()) # .isalpha(), 是否全是字母，并至少有一个字符
print(Str.isdigit())  # .isdigit(), 是否全是数字，并至少有一个字符
print(Str.isspace()) # .isspace(), 是否全是空白字符，并至少有一个字符
print(Str.islower()) # .islower(), 字母是否全是小写
print(Str.isupper()) # .isupper(), 字母是否全是大写
print(Str.istitle()) # .istitle(), 是否是首字母大写的
