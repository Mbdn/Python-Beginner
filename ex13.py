#coding:utf-8
#sys.argv 是需要参数的  定义几个参数，执行时就是定义减一
#如 python ex13.py 参数1 参数2 参数3            有一个参数是默认参数脚本本身
from sys import argv        #引用sys包argv模块

script, first, second ,third = argv     #一共四个参数 argv第一个参数是程序名本身.定义argv 

print "The script is called:", script           #输出参数
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
