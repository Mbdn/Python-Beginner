#  -*-  coding:utf-8   -*-

from sys import argv
#两个参数一个是文件名
script, input_file = argv

#定义函数输出文件
def print_all(f):
    print f.read()          #输出内容

#定义函数作用指定位置
def rewind(f):
    f.seek(0)

#读取函数输出那一行
def print_a_line(line_count, f):
    print line_count, f.readline()      #打印第一行从头开始

#打开文件给current_file
current_file = open(input_file)

print ("首先让我们打印整个文件:\n")

#调用函数打印整个文件
print_all(current_file)

print "Now let's rewind, kind of like a tape让我们返回开始位置."

#条用函数
rewind(current_file)

print "Let's print three lines“让我们打印三行:"

current_line = 1                #赋值为一，表示从第一行
print_a_line(current_line, current_file)    

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
