#-*-  coding:utf-8  -*-
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that. hit CTRL-C (^C)."
print "If you do want that,hit RETURN."

print "源文件将被覆盖，如果想保留请退出"
raw_input("?")

print "Opening the file..."
target = open(filename,'w')     #以写的方式打开文件给target

print "truncating the file . Goodbye!"
target.truncate()   #规定大小然后用truncate方法把这个文件清空(即删除文件内容)    

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm goung to weite these to the file ."

target.write(line1)         #向文件中写入内容
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we clise it."
target.close()          #关闭文件
