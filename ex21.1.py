#coding:utf-8

from sys import argv

def fan(can1,can2):
    return can1 + can2      #返回给jiguo

bens, cansu1, cansu2 = argv

jiguo = fan(cansu1,cansu2)      #传参给函数，返回值给jiguo

print jiguo
