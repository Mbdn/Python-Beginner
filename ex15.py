# -*-  coding:utf-8 -*-
from sys import argv

script, filename = argv 

#打开输入的文件到txt
txt = open(filename)

#打印文件名称
print "Here's your file%r:" % filename
print txt.read()        #打印文件内容  read是读取整个文件
txt.close()         #关闭文件

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()      
txt_again.close()

