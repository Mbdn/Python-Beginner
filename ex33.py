#   -*- coding: utf-8  -*-

i = 0
#申请空列表
numbers = []

#while循环直到i = 6 时终止循环
while i < 6 :
     print "At the top i is %d" % i
     #写数据
     numbers.append(i)
    
    #i = i + 1
     i += 1
     print "Numbers now: ", numbers
     print "At the bottom i is %d" % i


print "The numbers: "

#单独打印数numbers里面的所有元素
for num in numbers:
    print num
