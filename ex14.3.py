#coding:utf-8

from sys import argv

script, jisuan0, user_name = argv
prompt = '>'    #赋值

print "Hi %s, I'm the %s script." % (user_name,script)      #输出程序名字（script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name                      #输出第一个参数(user_name)
likes = raw_input(prompt)                                   #显示提示信息”>“并输入第一个参数

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you heve?"
computer = raw_input(prompt)

#将输入的数字转化为数值型
jisuan1 = int(input("输入计算的数2：")) 
jisuan0 = int (jisuan0)
ss = jisuan0 +jisuan1
print "计算结果是: %s" % ss


#输出所有输入的信息
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

