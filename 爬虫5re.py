import re
lst=re.findall(r"\d+","我的电话号码是：18906507616，我妈的电话是15355535321")#匹配字符串中所有符合正则的内容
print(lst)

print("  ")

#最重要
it=re.finditer(r"\d+","我的电话号码是：18906507616，我妈的电话是15355535321")#匹配字符串中所有符合正则的内容(返回迭代器)
for i in it:
    print(i.group())

print("  ")

#search,找到一个结果就返回，返回结果是match对象，拿数据用group()
s=re.search(r"\d+","我的电话号码是：18906507616，我妈的电话是15355535321")
print(s.group())
print(s.group())

print("  ")

#match是从头开始匹配（从头部开始就的是数字，否则报错）
s=re.match(r"\d+","18906507616，我妈的电话是15355535321")
print(s.group())

print("  ")

#预加载正则表达式
obj=re.compile(r"\d+")
resp=obj.finditer("我的电话号码是：18906507616，我妈的电话是15355535321")
for i in resp:
    print(i.group())

s=obj.findall('哈哈哈哈哈哈哈666666666666')
print(s)

print("  ")

s ="""
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋铁</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说八道</span></div>
"""
obj=re.compile(r"<div class='.*?'><span id='\d+'>.*?</span></div>",re.S)#re.S让‘.’可以匹配换行符
result=obj.finditer(s)
for i in result:
    print(i.group())
#(?P<分组名字>正则表达式)
obj=re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<xingming>.*?)</span></div>",re.S)#re.S让‘.’可以匹配换行符
result=obj.finditer(s)
for i in result:
    print(i.group('id'))
    print(i.group('xingming'))