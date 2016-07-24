# -*-  coding: utf-8 -*-

#建立一个函数   添加参数的  传的地址
def print_two(*args):       #函数必须要用：冒号结尾
    arg1, arg2 = args       #赋值   地址里面一次放入
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#可以这样 两个参数
def print_two_again(arg1, arg2):
    print "arg1: %r , arg2: %r " % (arg1, arg2)

#一个参数的
def print_one(arg1):
    print "arg1: %r" % arg1

#不要参数的
def print_none():
    print "I got nothin'."

#调用函数，加参数
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
