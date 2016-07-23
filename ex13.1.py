#coding:utf-8
'''将input和argv一起使用'''

from sys import argv


canshu1 ,canshu2, canshu3 = argv
canshu0 = input("请输入内容：")

print "你从键盘输入的:", canshu0
print "程序开始的第一个参数，也就是名字：", canshu1
print "程序后面根的第一个参数：", canshu2
print "程序最后一个参数：", canshu3
